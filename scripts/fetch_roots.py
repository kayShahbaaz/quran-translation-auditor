# scripts/fetch_roots.py
# ─────────────────────────────────────────────────────────────────────────────
# Fetches Arabic root mappings for all 6,236 Ayat using the
# AbstractThinker0/quran-roots compilation (Zekr.org-based, Tanzil v1.1
# aligned), and maps them onto our existing ayat table.
#
# Data format of quranRoots.json:
#   [ { "id": int, "name": "<root word, e.g. آدم or حمد>",
#       "count": "<occurrence count>",
#       "occurences": ["<flat_ayah_idx>:<word_pos>[,<word_pos2>...]", ...] },
#     ... ]
#
# "flat_ayah_idx" = 1-based sequential Ayah index across the WHOLE Quran
#   (1 = Al-Fatiha 1:1 ... 6236 = An-Nas 114:6), following Tanzil v1.1
#   ordering. "word_pos" = 1-based word position within that Ayah.
#
# This script:
#   1. Builds a flat_index -> ayah_key lookup from the existing `ayat` table
#      (ordered by id, which is already sequential 1..6236)
#   2. Fetches quranRoots.json
#   3. For each root entry, for each occurrence, resolves flat_index -> ayah_key
#      and word_pos -> the Nth word of that Ayah's `arabic` text
#   4. Builds { ayah_key: { arabic_word: root } } and stores in `roots` column
#
# IMPORTANT CAVEAT: this script assumes flat_index 1 = Ayah 1:1 (Alhamdulillah)
# per Tanzil v1.1 convention (Bismillah is NOT counted as a separate ayah in
# Tanzil numbering - it's embedded as part of ayah 1:1's text in some
# editions, or simply not present). This may NOT align perfectly with our
# database's Bismillah-stripped Al-Fatiha. The verification output below
# checks Al-Fatiha specifically - REVIEW IT CAREFULLY before trusting
# results for the full Quran.
#
# Usage: python scripts/fetch_roots.py
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, json, ssl, sqlite3, re
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")
ROOTS_URL = "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/quranRoots.json"

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE


def fetch_url(url):
    req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
    with urllib.request.urlopen(req, timeout=60, context=SSL_CTX) as r:
        return r.read().decode("utf-8")


def normalize_arabic(text):
    """
    Strip diacritics (tashkeel) and normalise alef variants so that
    word-matching between our `arabic` column and the root list's
    word forms is more robust to encoding differences.
    """
    # Remove Arabic diacritics (tashkeel) - Unicode range 0610-061A, 064B-065F, 0670, 06D6-06ED
    text = re.sub(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]', '', text)
    # Normalise alef variants to bare alef
    text = re.sub(r'[\u0622\u0623\u0625\u0671]', '\u0627', text)  # آ أ إ ٱ -> ا
    # Normalise yaa variants
    text = text.replace('\u0649', '\u064A')  # ى -> ي
    # Remove tatweel
    text = text.replace('\u0640', '')
    return text


def build_flat_index_map(conn):
    """
    Build flat_index (1-based, Tanzil v1.1 sequential) -> ayah_key
    from the existing ayat table, which is already in correct
    sequential order via the `id` column.
    """
    cur = conn.cursor()
    rows = cur.execute("SELECT id, ayah_key, arabic FROM ayat ORDER BY id").fetchall()
    flat_map = {}
    arabic_map = {}
    for i, (db_id, ayah_key, arabic) in enumerate(rows, start=1):
        flat_map[i] = ayah_key
        arabic_map[ayah_key] = arabic
    return flat_map, arabic_map


def get_word_at_position(arabic_text, word_pos):
    """
    Return the word at 1-based word_pos in arabic_text (split on whitespace).
    Returns None if out of range.
    """
    words = arabic_text.split()
    if 1 <= word_pos <= len(words):
        return words[word_pos - 1]
    return None


def to_hyphenated_root(root_word):
    """
    Convert a root word (e.g. 'حمد', 'علم') into our lexicon's
    hyphenated format (e.g. 'ح-م-د', 'ع-ل-م') by joining each
    Arabic character (after normalisation) with '-'.
    """
    normalized = normalize_arabic(root_word)
    # Filter to Arabic letters only (skip any stray marks)
    letters = [ch for ch in normalized if '\u0621' <= ch <= '\u064A']
    return "-".join(letters)


def parse_occurrences(occ_string):
    """
    Parse one occurrence string like "50:1,9" or "37:2" into
    a list of (flat_ayah_idx, word_pos) tuples.
    "50:1,9" means ayah 50, words 1 AND 9 both have this root.
    """
    results = []
    ayah_part, word_part = occ_string.split(":")
    flat_idx = int(ayah_part)
    for wp in word_part.split(","):
        results.append((flat_idx, int(wp)))
    return results


def main():
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database not found at {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)

    print("Building flat-index -> ayah_key map from database...")
    flat_map, arabic_map = build_flat_index_map(conn)
    print(f"  {len(flat_map)} Ayat indexed (flat 1..{len(flat_map)})")

    print("\nFetching quranRoots.json...")
    raw = fetch_url(ROOTS_URL)
    root_entries = json.loads(raw)
    print(f"  {len(root_entries)} root entries loaded")

    # Build { ayah_key: { arabic_word: hyphenated_root } }
    roots_by_ayah = {key: {} for key in flat_map.values()}

    unmatched_count = 0
    matched_count   = 0

    for entry in root_entries:
        root_word = entry["name"]
        hyphenated = to_hyphenated_root(root_word)
        if not hyphenated:
            continue

        for occ in entry.get("occurences", []):
            try:
                pairs = parse_occurrences(occ)
            except Exception:
                continue

            for flat_idx, word_pos in pairs:
                ayah_key = flat_map.get(flat_idx)
                if not ayah_key:
                    unmatched_count += 1
                    continue

                arabic_text = arabic_map[ayah_key]
                word = get_word_at_position(arabic_text, word_pos)
                if word:
                    roots_by_ayah[ayah_key][word] = hyphenated
                    matched_count += 1
                else:
                    unmatched_count += 1

    print(f"\n  Matched word positions  : {matched_count}")
    print(f"  Unmatched word positions: {unmatched_count}")

    # ── VERIFICATION: Al-Fatiha (1:1 - 1:7) ────────────────────────────────────
    print(f"\n{'='*72}")
    print("  AL-FATIHA VERIFICATION (review carefully before trusting full data)")
    print(f"{'='*72}")
    for s in range(1, 8):
        key = f"1:{s}"
        arabic = arabic_map.get(key, "")
        roots  = roots_by_ayah.get(key, {})
        print(f"\n  Ayah {key}")
        print(f"  Arabic words : {arabic.split()}")
        print(f"  Roots found  : {roots}")

    # ── Ask before writing to DB ────────────────────────────────────────────────
    print(f"\n{'='*72}")
    print("  Does the Al-Fatiha verification above look CORRECT?")
    print("  (Compare each Arabic word to its expected root, e.g.")
    print("   الْحَمْدُ should map to ح-م-د, لِلَّهِ to أ-ل-ه, etc.)")
    print(f"{'='*72}")
    print("\n  This script has NOT written anything to the database yet.")
    print("  If Al-Fatiha looks correct, re-run with --write to save all 6,236 Ayat:")
    print("  python scripts/fetch_roots.py --write\n")

    if "--write" in sys.argv:
        print("Writing to database...")
        cur = conn.cursor()
        updated = 0
        for ayah_key, word_roots in roots_by_ayah.items():
            if word_roots:
                cur.execute(
                    "UPDATE ayat SET roots = ? WHERE ayah_key = ?",
                    (json.dumps(word_roots, ensure_ascii=False), ayah_key)
                )
                if cur.rowcount > 0:
                    updated += 1
        conn.commit()
        print(f"  Updated {updated}/{len(roots_by_ayah)} Ayat with root data")
        print(f"\n  \u2705 Done! Run: python run.py")

    conn.close()


if __name__ == "__main__":
    main()
