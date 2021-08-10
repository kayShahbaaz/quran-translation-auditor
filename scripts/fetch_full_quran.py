# scripts/fetch_full_quran.py
# ─────────────────────────────────────────────────────────────────────────────
# Full Quran Fetcher — 6,236 Ayat × 4 exact translations
#
# Sources:
#   quran.com API v4  — Arabic, Sahih International, Abdel Haleem, Bridges
#   jsdelivr CDN      — Mustafa Khattab / The Clear Quran (Allah Edition)
#
# Translation IDs:
#   Sahih International        → quran.com id=20
#   Abdel Haleem               → quran.com id=85
#   Mustafa Khattab (Allah Ed) → fawazahmed0/quran-api eng-mustafakhattaba
#   Fadel Soliman / Bridges    → quran.com id=149
#
# Usage:  python scripts/fetch_full_quran.py
# Time:   ~3–5 minutes
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, json, time, sqlite3, ssl, re
import urllib.request, urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

DB_PATH  = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

# ── APIs ──────────────────────────────────────────────────────────────────────
QURAN_COM   = "https://api.quran.com/api/v4"
JSDELIVR    = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions"

QURAN_COM_IDS = {
    "sahih":   20,    # Saheeh International
    "haleem":  85,    # M.A.S. Abdel Haleem (Oxford)
    "soliman": 149,   # Fadel Soliman / Bridges
}
KHATTAB_URL = f"{JSDELIVR}/eng-mustafakhattaba.json"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

SURAH_NAMES = [
    "Al-Fatiha","Al-Baqarah","Al-Imran","An-Nisa","Al-Maidah",
    "Al-Anam","Al-Araf","Al-Anfal","At-Tawbah","Yunus",
    "Hud","Yusuf","Ar-Rad","Ibrahim","Al-Hijr",
    "An-Nahl","Al-Isra","Al-Kahf","Maryam","Ta-Ha",
    "Al-Anbiya","Al-Hajj","Al-Muminun","An-Nur","Al-Furqan",
    "Ash-Shuara","An-Naml","Al-Qasas","Al-Ankabut","Ar-Rum",
    "Luqman","As-Sajdah","Al-Ahzab","Saba","Fatir",
    "Ya-Sin","As-Saffat","Sad","Az-Zumar","Ghafir",
    "Fussilat","Ash-Shura","Az-Zukhruf","Ad-Dukhan","Al-Jathiyah",
    "Al-Ahqaf","Muhammad","Al-Fath","Al-Hujurat","Qaf",
    "Adh-Dhariyat","At-Tur","An-Najm","Al-Qamar","Ar-Rahman",
    "Al-Waqiah","Al-Hadid","Al-Mujadila","Al-Hashr","Al-Mumtahanah",
    "As-Saf","Al-Jumuah","Al-Munafiqun","At-Taghabun","At-Talaq",
    "At-Tahrim","Al-Mulk","Al-Qalam","Al-Haqqah","Al-Maarij",
    "Nuh","Al-Jinn","Al-Muzzammil","Al-Muddaththir","Al-Qiyamah",
    "Al-Insan","Al-Mursalat","An-Naba","An-Naziat","Abasa",
    "At-Takwir","Al-Infitar","Al-Mutaffifin","Al-Inshiqaq","Al-Buruj",
    "At-Tariq","Al-Ala","Al-Ghashiyah","Al-Fajr","Al-Balad",
    "Ash-Shams","Al-Layl","Ad-Duha","Ash-Sharh","At-Tin",
    "Al-Alaq","Al-Qadr","Al-Bayyinah","Az-Zalzalah","Al-Adiyat",
    "Al-Qariah","At-Takathur","Al-Asr","Al-Humazah","Al-Fil",
    "Quraysh","Al-Maun","Al-Kawthar","Al-Kafirun","An-Nasr",
    "Al-Masad","Al-Ikhlas","Al-Falaq","An-Nas",
]

# ── HTTP helper ───────────────────────────────────────────────────────────────

def fetch_url(url, label=""):
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "QuranAuditor/1.0", "Accept": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:
            print(f"\n    Attempt {attempt} failed: {e}", end=" ")
            if attempt < 3:
                print("Retrying in 3s...")
                time.sleep(3)
            else:
                print(f"\n  ERROR fetching {label}. Aborting.")
                sys.exit(1)

def strip_html(text):
    """Remove HTML tags quran.com sometimes includes."""
    return re.sub(r"<[^>]+>", "", text or "").strip()

# ── Fetch Arabic (quran.com) ──────────────────────────────────────────────────

def fetch_arabic():
    print("  Fetching Arabic text (114 Surahs) ...", end=" ", flush=True)
    arabic_map = {}
    surah_map  = {}
    for s in range(1, 115):
        url  = f"{QURAN_COM}/verses/by_chapter/{s}?language=ar&words=false&per_page=300&fields=text_uthmani"
        data = fetch_url(url, f"Arabic Surah {s}")
        for v in data["verses"]:
            key = v["verse_key"]
            arabic_map[key] = v["text_uthmani"]
            surah_map[int(key.split(":")[0])] = SURAH_NAMES[s - 1]
        time.sleep(0.08)
    print(f"OK ({len(arabic_map)} ayat)")
    return arabic_map, surah_map

# ── Fetch one translation from quran.com ─────────────────────────────────────

def fetch_qurancom(resource_id, label):
    print(f"  Fetching {label} (quran.com id={resource_id}) ...", end=" ", flush=True)
    trans_map = {}
    for s in range(1, 115):
        url  = f"{QURAN_COM}/verses/by_chapter/{s}?language=en&words=false&per_page=300&translations={resource_id}"
        data = fetch_url(url, f"{label} Surah {s}")
        for v in data["verses"]:
            key  = v["verse_key"]
            text = v.get("translations", [{}])[0].get("text", "")
            trans_map[key] = strip_html(text)
        time.sleep(0.08)
    print(f"OK ({len(trans_map)} ayat)")
    return trans_map

# ── Fetch Khattab from jsdelivr/fawazahmed0 ───────────────────────────────────

def fetch_khattab():
    """
    Fetches Mustafa Khattab / The Clear Quran (Allah Edition)
    from fawazahmed0/quran-api on jsdelivr CDN.

    Actual data structure:
    { "quran": [ {"chapter":1, "verse":1, "text":"..."}, ... ] }
    Returns dict: { "surah:ayah" -> text }
    """
    print(f"  Fetching Mustafa Khattab / Clear Quran (jsdelivr) ...", end=" ", flush=True)
    data      = fetch_url(KHATTAB_URL, "Khattab")
    verses    = data.get("quran", [])
    trans_map = {}

    for item in verses:
        chapter = item.get("chapter")
        verse   = item.get("verse")
        text    = item.get("text", "")
        if chapter and verse:
            key = f"{chapter}:{verse}"
            trans_map[key] = strip_html(str(text))

    print(f"OK ({len(trans_map)} ayat)")
    return trans_map

# ── Bismillah / Al-Fatiha fix ─────────────────────────────────────────────────
# quran.com counts Bismillah as 1:1 in Al-Fatiha.
# Project convention: 1:1 = Alhamdulillah
# Fix: drop 1:1 (Bismillah), shift 1:2→1:1 … 1:7→1:6

def fix_fatiha(ayah_map):
    fixed = {}
    for key, text in ayah_map.items():
        if key == "1:1":
            continue                           # drop Bismillah
        elif key.startswith("1:"):
            n = int(key.split(":")[1]) - 1     # shift down by 1
            fixed[f"1:{n}"] = text
        else:
            fixed[key] = text
    return fixed

# Note: fawazahmed0 API already numbers Al-Fatiha correctly (1:1 = Alhamdulillah)
# so fix_fatiha is only applied to quran.com results

# ── Database ──────────────────────────────────────────────────────────────────

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS ayat")
    cur.execute("""
        CREATE TABLE ayat (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            ayah_key         TEXT    NOT NULL UNIQUE,
            surah_name       TEXT    NOT NULL,
            arabic           TEXT    NOT NULL,
            roots            TEXT    NOT NULL DEFAULT '{}',
            trans_sahih      TEXT    NOT NULL DEFAULT '',
            trans_haleem     TEXT    NOT NULL DEFAULT '',
            trans_khattab    TEXT    NOT NULL DEFAULT '',
            trans_soliman    TEXT    NOT NULL DEFAULT '',
            divergence_score REAL    DEFAULT 0.0
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Schema ready.")

def seed_db(arabic_map, surah_map, translations):
    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()
    rows = []
    for key, arabic_text in sorted(
        arabic_map.items(),
        key=lambda x: (int(x[0].split(":")[0]), int(x[0].split(":")[1]))
    ):
        s_num = int(key.split(":")[0])
        rows.append((
            key,
            surah_map.get(s_num, f"Surah {s_num}"),
            arabic_text,
            "{}",
            translations["sahih"].get(key,   ""),
            translations["haleem"].get(key,  ""),
            translations["khattab"].get(key, ""),
            translations["soliman"].get(key, ""),
            0.0,
        ))
    cur.executemany("""
        INSERT OR IGNORE INTO ayat
            (ayah_key, surah_name, arabic, roots,
             trans_sahih, trans_haleem, trans_khattab, trans_soliman,
             divergence_score)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, rows)
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM ayat").fetchone()[0]
    conn.close()
    return count

# ── Verification ──────────────────────────────────────────────────────────────

def verify_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()
    total   = cur.execute("SELECT COUNT(*) FROM ayat").fetchone()[0]
    samples = cur.execute("""
        SELECT ayah_key, surah_name, arabic,
               trans_sahih, trans_haleem, trans_khattab, trans_soliman
        FROM ayat WHERE ayah_key IN ('1:1','1:2','2:255','112:1')
        ORDER BY id
    """).fetchall()
    conn.close()
    print(f"\n{'='*72}")
    print(f"  VERIFICATION — {total} total Ayat")
    print(f"{'='*72}")
    for r in samples:
        print(f"\n  Ayah {r['ayah_key']}  [{r['surah_name']}]")
        print(f"  Arabic  : {r['arabic']}")
        print(f"  Sahih   : {r['trans_sahih']}")
        print(f"  Haleem  : {r['trans_haleem']}")
        print(f"  Khattab : {r['trans_khattab']}")
        print(f"  Soliman : {r['trans_soliman']}")
    print(f"\n{'='*72}")

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n" + "="*72)
    print("  FULL QURAN FETCH — 6,236 Ayat × 4 Exact Translations")
    print("  Sahih International  |  Abdel Haleem  |  Mustafa Khattab  |  Bridges")
    print("  Sources: quran.com API v4  +  fawazahmed0/quran-api (jsdelivr)")
    print("  SSL: auto-fixed for macOS")
    print("="*72 + "\n")

    # ── Arabic
    print("[1/6] Arabic text...")
    arabic_map, surah_map = fetch_arabic()
    arabic_map = fix_fatiha(arabic_map)
    time.sleep(1)

    # ── Sahih International
    print("\n[2/6] Sahih International...")
    sahih_map  = fix_fatiha(fetch_qurancom(QURAN_COM_IDS["sahih"], "Sahih International"))
    time.sleep(1)

    # ── Abdel Haleem
    print("\n[3/6] Abdel Haleem...")
    haleem_map = fix_fatiha(fetch_qurancom(QURAN_COM_IDS["haleem"], "Abdel Haleem"))
    time.sleep(1)

    # ── Mustafa Khattab / The Clear Quran (Allah Edition) — jsdelivr
    print("\n[4/6] Mustafa Khattab / The Clear Quran...")
    khattab_map = fix_fatiha(fetch_khattab())
    # fawazahmed0 also counts Bismillah as 1:1 — fix_fatiha applied
    time.sleep(1)

    # ── Fadel Soliman / Bridges
    print("\n[5/6] Fadel Soliman / Bridges...")
    soliman_map = fix_fatiha(fetch_qurancom(QURAN_COM_IDS["soliman"], "Fadel Soliman / Bridges"))
    time.sleep(1)

    # ── Seed
    print("\n[6/6] Seeding database...")
    init_db()
    count = seed_db(arabic_map, surah_map, {
        "sahih":   sahih_map,
        "haleem":  haleem_map,
        "khattab": khattab_map,
        "soliman": soliman_map,
    })

    verify_db()

    print(f"\n  ✅  Done! {count} Ayat loaded into data/auditor.db")
    print(f"  ▶   Run: python run.py\n")
