# scripts/fetch_gloss.py
# ─────────────────────────────────────────────────────────────────────────────
# Fetches word-by-word English glosses for all 6,236 Ayat from quran.com API v4
# (sourced from the Quranic Arabic Corpus morphology data).
#
# Adds a `gloss` column to the ayat table — stores a JSON list of per-word
# gloss strings for each Ayah, used by fidelity_engine.gloss_fidelity_score()
# as the Layer 1 "Literal Accuracy" baseline.
#
# Usage: python scripts/fetch_gloss.py
# Time:  ~3-5 minutes (114 Surahs)
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, json, time, sqlite3, ssl
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

DB_PATH  = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")
BASE_URL = "https://api.quran.com/api/v4"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE


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
            if attempt < 3:
                time.sleep(2)
            else:
                print(f"\n  ERROR fetching {label}: {e}")
                return None


# ── Fetch word-by-word gloss for one Surah ───────────────────────────────────

# Gloss words that mark the start of Ayah 1:7 (the word ghayri / "not/other than")
# Used to split quran.com's merged 6+7 verse into two separate Ayat.
AYAH_7_START_MARKERS = ["not (of)", "not of", "other than", "not", "(of)not"]


def split_fatiha_6_7(glosses):
    """
    quran.com merges Al-Fatiha Ayat 6 and 7 into a single verse entry.
    Split the combined gloss list into two lists at the word that
    corresponds to ghayri (start of Ayah 1:7: "ghayril maghdoobi...").

    Returns (ayah_6_glosses, ayah_7_glosses)
    """
    for i, g in enumerate(glosses):
        gl = g.lower().strip()
        if gl.startswith("not") or "other than" in gl or gl == "ghayri":
            return glosses[:i], glosses[i:]
    # Fallback: if marker not found, split roughly in half
    mid = len(glosses) // 2
    return glosses[:mid], glosses[mid:]


def fix_fatiha_gloss(gloss_map):
    """
    quran.com's verses/by_chapter/1 endpoint has TWO issues for Surah 1:

    1. Bismillah is returned as verse 1:1 (should be dropped/excluded).
    2. Ayat 6 and 7 are merged into a SINGLE verse entry (likely
       returned as key "1:6" or "1:7" depending on response, containing
       both Ayat's words combined).

    This function:
      - Drops the Bismillah entry (first entry, "1:1" in raw data)
      - Shifts remaining raw entries down by one ayah number
      - Splits the merged 6/7 entry into two separate Ayat using
        split_fatiha_6_7(), at the word "ghayri" (not/other than)
        which marks the start of Ayah 1:7

    Result: clean 1:1 through 1:7, aligned with project convention
    (1:1 = Alhamdulillah) used for all translation columns.
    """
    # Sort raw keys numerically to process in order
    raw_keys = sorted(gloss_map.keys(), key=lambda k: int(k.split(":")[1]))

    # Drop the first entry (Bismillah)
    raw_keys = raw_keys[1:]

    fixed = {}
    next_ayah = 1

    for key in raw_keys:
        glosses = gloss_map[key]

        # Detect if this entry contains BOTH ayah 6 and 7
        # (heuristic: it's the entry that, after shifting, would land
        #  on ayah 6, AND contains a "not"/"ghayri"-type marker partway through)
        if next_ayah == 6:
            a6, a7 = split_fatiha_6_7(glosses)
            if a7:  # split found a second part
                fixed[f"1:{next_ayah}"]     = a6
                fixed[f"1:{next_ayah + 1}"] = a7
                next_ayah += 2
                continue

        fixed[f"1:{next_ayah}"] = glosses
        next_ayah += 1

    return fixed


def fetch_surah_gloss(surah_num):
    """
    Fetch all verses of a Surah with word-by-word data including
    the 'translation' field for each word (the gloss).

    Returns dict: { "surah:ayah" -> [list of word gloss strings] }
    """
    url  = (f"{BASE_URL}/verses/by_chapter/{surah_num}"
            f"?language=en&words=true&word_fields=text_uthmani"
            f"&translation_fields=text&per_page=300")
    data = fetch_url(url, f"Surah {surah_num} gloss")
    if not data:
        return {}

    gloss_map = {}
    for verse in data.get("verses", []):
        key   = verse["verse_key"]
        words = verse.get("words", [])
        glosses = []
        for w in words:
            # Skip end-of-ayah marker words (char_type "end")
            if w.get("char_type_name") == "end":
                continue
            translation = w.get("translation", {})
            text = translation.get("text", "") if isinstance(translation, dict) else ""
            if text:
                glosses.append(text)
        gloss_map[key] = glosses

    # Apply Bismillah/Fatiha fix only for Surah 1
    if surah_num == 1:
        gloss_map = fix_fatiha_gloss(gloss_map)

    return gloss_map


# ── Database ──────────────────────────────────────────────────────────────────

def add_column_if_missing(conn):
    cur  = conn.cursor()
    cols = [row[1] for row in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "gloss" not in cols:
        cur.execute("ALTER TABLE ayat ADD COLUMN gloss TEXT NOT NULL DEFAULT '[]'")
        conn.commit()
        print("[DB] Added gloss column.")
    else:
        print("[DB] gloss column already exists.")


def update_gloss(conn, gloss_data):
    cur = conn.cursor()
    updated = 0
    for key, words in gloss_data.items():
        cur.execute(
            "UPDATE ayat SET gloss = ? WHERE ayah_key = ?",
            (json.dumps(words, ensure_ascii=False), key)
        )
        if cur.rowcount > 0:
            updated += 1
    conn.commit()
    return updated


def verify(conn):
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()
    filled = cur.execute("SELECT COUNT(*) FROM ayat WHERE gloss != '[]'").fetchone()[0]
    samples = cur.execute("""
        SELECT ayah_key, arabic, gloss, trans_sahih
        FROM ayat WHERE ayah_key IN ('1:1','1:2','2:255','112:1')
        ORDER BY id
    """).fetchall()

    print(f"\n{'='*72}")
    print(f"  GLOSS VERIFICATION — {filled} Ayat filled (of 6,236)")
    print(f"{'='*72}")
    for r in samples:
        gloss = json.loads(r["gloss"])
        print(f"\n  Ayah {r['ayah_key']}")
        print(f"  Arabic  : {r['arabic']}")
        print(f"  Gloss   : {gloss}")
        print(f"  Sahih   : {r['trans_sahih'][:70]}")
    print(f"\n{'='*72}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database not found at {DB_PATH}")
        print("Run scripts/fetch_full_quran.py first.")
        sys.exit(1)

    print("\n" + "="*72)
    print("  GLOSS FETCH — Word-by-word English glosses (Quranic Arabic Corpus)")
    print("  Source: quran.com API v4")
    print("  SSL: auto-fixed for macOS")
    print("="*72 + "\n")

    conn = sqlite3.connect(DB_PATH)
    add_column_if_missing(conn)

    all_gloss = {}
    failed    = []

    for s in range(1, 115):
        print(f"  [{s:>3}/114] Surah {s} ...", end=" ", flush=True)
        gloss_map = fetch_surah_gloss(s)
        if gloss_map:
            all_gloss.update(gloss_map)
            print(f"OK ({len(gloss_map)} Ayat)")
        else:
            print("WARNING — 0 Ayat parsed")
            failed.append(s)
        time.sleep(0.1)

    print(f"\n  Total parsed: {len(all_gloss)} Ayat")
    if failed:
        print(f"  Failed Surahs: {failed}")

    if len(all_gloss) < 100:
        print("\n  ERROR: Too few Ayat parsed. Aborting.")
        sys.exit(1)

    print("\nUpdating database...")
    updated = update_gloss(conn, all_gloss)
    print(f"  Updated {updated} Ayat with word-by-word gloss")

    verify(conn)
    conn.close()

    print(f"\n  \u2705  Done! Run: python run.py\n")
