# scripts/fetch_kanzuliman.py
# ─────────────────────────────────────────────────────────────────────────────
# Fetches Kanzul Iman (English) by Aqib Farid Qadri
# Source: barkati.net — clean HTML, one page per Surah
# Format: [SurahName S:A] Translation text
#
# Usage: python scripts/fetch_kanzuliman.py
# Time:  ~3–5 minutes (114 pages)
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, re, sqlite3, ssl, time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

DB_PATH  = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")
BASE_URL = "https://www.barkati.net/quran/Translation/holyquran{:03d}.htm"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

# ── Fetch one Surah page ──────────────────────────────────────────────────────

def fetch_surah(surah_num):
    url = BASE_URL.format(surah_num)
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": "Mozilla/5.0 QuranAuditor/1.0"}
            )
            with urllib.request.urlopen(req, timeout=20, context=SSL_CTX) as r:
                return r.read().decode("utf-8", errors="ignore")
        except Exception as e:
            if attempt < 3:
                time.sleep(2)
            else:
                print(f"\n  ERROR fetching Surah {surah_num}: {e}")
                return ""

# ── Parse ayat from one Surah page ───────────────────────────────────────────
# Matches any bracket label like:
#   [Fatihah 1:1]       [A/I`mran 3:1]      [Ana`am 6:1]
#   [Bani Israel 17:1]  [H.M.Sajdah 41:1]   [Jum`a 62:1]
# Key fix: [^\]]+ matches ANY characters inside brackets (including backticks,
# slashes, apostrophes, dots, spaces) instead of only \w\s\.

AYAH_RE = re.compile(
    r'\[[^\]]+\s+(\d+)\s*:\s*(\d+)\]\s*(.+?)(?=\[[^\]]+\s+\d+\s*:\s*\d+\]|END OF SURAH|$)',
    re.DOTALL
)

def parse_surah(html, surah_num):
    """Extract all Ayat from one Surah HTML page."""
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'&nbsp;', ' ', text)
    text = re.sub(r'&amp;', '&', text)
    text = re.sub(r'&#\d+;', '', text)
    text = re.sub(r'\s+', ' ', text)

    ayat = {}
    for m in AYAH_RE.finditer(text):
        s   = int(m.group(1))
        a   = int(m.group(2))
        raw = m.group(3).strip()
        raw = re.sub(r'\s+', ' ', raw).strip()
        raw = re.sub(r'END OF SURAH.*$', '', raw, flags=re.IGNORECASE).strip()
        raw = re.sub(r'Return to.*$',    '', raw, flags=re.IGNORECASE).strip()
        if raw and s == surah_num:
            ayat[f"{s}:{a}"] = raw

    return ayat

# ── Database ──────────────────────────────────────────────────────────────────

def add_column_if_missing():
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    cols = [row[1] for row in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "trans_kanzuliman" not in cols:
        cur.execute("ALTER TABLE ayat ADD COLUMN trans_kanzuliman TEXT NOT NULL DEFAULT ''")
        conn.commit()
        print("[DB] Column trans_kanzuliman added.")
    else:
        print("[DB] Column trans_kanzuliman already exists.")
    conn.close()

def update_kanzuliman(ayah_map):
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    updated = 0
    for key, text in ayah_map.items():
        cur.execute(
            "UPDATE ayat SET trans_kanzuliman = ? WHERE ayah_key = ?",
            (text, key)
        )
        if cur.rowcount > 0:
            updated += 1
    conn.commit()
    conn.close()
    return updated

def verify():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()
    filled  = cur.execute(
        "SELECT COUNT(*) FROM ayat WHERE trans_kanzuliman != ''"
    ).fetchone()[0]
    samples = cur.execute("""
        SELECT ayah_key, trans_sahih, trans_khattab, trans_kanzuliman
        FROM ayat WHERE ayah_key IN ('1:1','1:2','1:3','2:255','112:1')
        ORDER BY id
    """).fetchall()
    conn.close()

    print(f"\n{'='*72}")
    print(f"  KANZUL IMAN VERIFICATION — {filled} Ayat filled")
    print(f"{'='*72}")
    for r in samples:
        print(f"\n  Ayah {r['ayah_key']}")
        print(f"  Sahih     : {r['trans_sahih'][:70]}")
        print(f"  Khattab   : {r['trans_khattab'][:70]}")
        print(f"  KanzulIman: {r['trans_kanzuliman'][:70]}")
    print(f"\n{'='*72}")

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*72)
    print("  KANZUL IMAN FETCH — Aqib Farid Qadri")
    print("  Source: barkati.net (clean HTML, 114 pages)")
    print("  SSL: auto-fixed for macOS")
    print("="*72 + "\n")

    all_ayat = {}
    failed   = []

    for s in range(1, 115):
        print(f"  [{s:>3}/114] Surah {s} ...", end=" ", flush=True)
        html = fetch_surah(s)
        ayat = parse_surah(html, s)
        if ayat:
            all_ayat.update(ayat)
            print(f"OK ({len(ayat)} Ayat)")
        else:
            print("WARNING — 0 Ayat parsed")
            failed.append(s)
        time.sleep(0.3)

    print(f"\n  Total parsed: {len(all_ayat)} Ayat")
    if failed:
        print(f"  Failed Surahs: {failed}")

    if len(all_ayat) < 100:
        print("\n  ERROR: Too few Ayat parsed. Aborting.")
        sys.exit(1)

    print("\nUpdating database...")
    add_column_if_missing()
    updated = update_kanzuliman(all_ayat)
    print(f"  Updated {updated} Ayat with Kanzul Iman translation")

    verify()
    print(f"\n  ✅  Done! Run: python run.py\n")
