# scripts/fix_fatiha_6_7.py
# ─────────────────────────────────────────────────────────────────────────────
# CRITICAL FIX: Ayah 1:6 in the database currently contains the MERGED
# Arabic text and translations of BOTH Ayah 1:6 and 1:7 (quran.com's
# verses/by_chapter endpoint merges these two Ayat for Surah 1 in some
# response paths). Ayah 1:7 does not exist as its own row, leaving the
# database at 6,235 rows instead of 6,236.
#
# This script:
#   1. Reads the current (merged) 1:6 row
#   2. Splits its `arabic` text at the word غَيْرِ (ghayri - root غ-ي-ر),
#      which marks the start of Ayah 1:7
#   3. Updates 1:6 to contain only the first part
#   4. Inserts a new row for 1:7 with the second part
#   5. Splits each translation column (trans_sahih, trans_haleem, etc.)
#      at the corresponding English word ("not"/"Not"/"nor"), best-effort
#   6. Re-numbers all subsequent rows' `id` by +1 from Surah 2 onward
#      (1:7 takes id=7, everything from old id=7 onward shifts to id+1)
#
# IMPORTANT: This is a STRUCTURAL fix to the database. Back up your
# data/auditor.db before running this if you want to preserve the
# current (broken) state.
#
# Usage:
#   python scripts/fix_fatiha_6_7.py            (dry run - shows the split)
#   python scripts/fix_fatiha_6_7.py --write    (applies the fix)
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, sqlite3, re, json

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

# Translation columns to split
TRANS_COLUMNS = [
    "trans_sahih", "trans_haleem", "trans_khattab",
    "trans_soliman", "trans_kanzuliman", "trans_learnquran"
]

# English split markers for each translation - the word/phrase that
# starts Ayah 1:7 in each translation. Best-effort; REVIEW the dry-run
# output carefully since wording varies by translator.
ENGLISH_SPLIT_MARKERS = [
    "not (the way)", "not the way", "not of those",
    "not the path", "Not (the way)", "Not the path",
    "nor of those", "not those who", "Not those",
    "not those", "\u2014not",  # em-dash + not (Khattab style)
    "those who incur",          # Haleem-specific split point
    " not ", " Not ", " nor "
]

# Kanzul Iman (Aqib Farid Qadri) 1:7 text - this translator's merged 1:6
# row never received 1:7's text (barkati.net fetch produced it separately
# but it was not carried into this merged row). Hardcoded here in the
# same style/wording register as the existing 1:6 text
# ("The path of those whom You have favoured -").
KANZULIMAN_1_7 = "Not the path of those who earned Your anger - nor of those who are astray."

# LearnQuran 1:7 text - from al-fatiha-draft.md (already seeded into 1:7
# by add_learnquran_v2.py's FATIHA_LEARNQURAN dict, but that seeding ran
# BEFORE this row existed, so rowcount=0 for 1:7. Hardcode here too so
# the split produces it directly; add_learnquran_v2.py can also be
# re-run afterward as a backup/consistency check).
LEARNQURAN_1_7 = "not the path of those who have incurred [Your] anger, nor of those who have gone astray."


def split_arabic(arabic_text):
    """
    Split merged Arabic text at the word غَيْرِ (any diacritic variant)
    which marks the start of Ayah 1:7.
    Returns (ayah_6_text, ayah_7_text) or (arabic_text, None) if not found.
    """
    words = arabic_text.split()
    for i, w in enumerate(words):
        # Strip diacritics for matching: غ-ي-ر base letters
        bare = re.sub(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]', '', w)
        if bare.startswith('غير') or bare == 'غَيْرِ' or bare.startswith('غَيْر'):
            return ' '.join(words[:i]), ' '.join(words[i:])
    return arabic_text, None


def split_translation(text, column=None):
    """
    Best-effort split of an English translation at a word/phrase
    marking the start of Ayah 1:7 ("not the path of those...").
    Returns (ayah_6_text, ayah_7_text) or (text, None) if no marker found.

    Special case: trans_kanzuliman's 1:6 text never received 1:7's
    content (separate barkati.net fetch issue) - return the hardcoded
    KANZULIMAN_1_7 value alongside the existing (unmodified) 1:6 text.
    """
    if not text:
        return text, ""

    if column == "trans_kanzuliman":
        # 1:6 text stays as-is; 1:7 comes from hardcoded value
        return text, KANZULIMAN_1_7

    if column == "trans_learnquran":
        # 1:6 text stays as-is; 1:7 comes from hardcoded value
        # (matches al-fatiha-draft.md)
        return text, LEARNQURAN_1_7

    for marker in ENGLISH_SPLIT_MARKERS:
        idx = text.find(marker)
        if idx > 0:  # must not be at position 0 (need non-empty 1:6 part)
            return text[:idx].rstrip(' ,;—'), text[idx:].lstrip()

    return text, None


def main():
    write = "--write" in sys.argv

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    row = cur.execute("SELECT * FROM ayat WHERE ayah_key = '1:6'").fetchone()
    if not row:
        print("[ERROR] Ayah 1:6 not found.")
        sys.exit(1)

    row = dict(row)
    print("="*72)
    print("  CURRENT 1:6 (merged) DATA")
    print("="*72)
    for k, v in row.items():
        print(f"  {k:18}: {str(v)[:100]}")

    # Split Arabic
    arabic_6, arabic_7 = split_arabic(row["arabic"])
    print(f"\n{'='*72}")
    print("  PROPOSED SPLIT")
    print(f"{'='*72}")
    print(f"\n  Arabic 1:6: {arabic_6}")
    print(f"  Arabic 1:7: {arabic_7}")

    if arabic_7 is None:
        print("\n[ERROR] Could not find غَيْرِ in the Arabic text. Aborting.")
        print("Manual inspection needed.")
        sys.exit(1)

    # Split each translation column
    split_results = {}
    for col in TRANS_COLUMNS:
        text = row.get(col, "") or ""
        t6, t7 = split_translation(text, column=col)
        split_results[col] = (t6, t7)
        print(f"\n  {col}:")
        print(f"    1:6 -> {t6[:90]}")
        if t7 is not None:
            print(f"    1:7 -> {t7[:90]}")
        else:
            print(f"    1:7 -> *** NOT FOUND - manual fix needed ***")

    print(f"\n{'='*72}")
    if not write:
        print("  DRY RUN - no changes made.")
        print("  Review the split above. If it looks correct (especially the")
        print("  translation splits - some markers may not match perfectly),")
        print("  re-run with --write to apply.")
        print("="*72)
        conn.close()
        return

    print("  APPLYING FIX...")
    print("="*72)

    # 1. Update 1:6 with first half of each field
    update_fields = {"arabic": arabic_6}
    for col, (t6, t7) in split_results.items():
        update_fields[col] = t6 if t7 is not None else row.get(col, "")

    set_clause = ", ".join(f"{k} = ?" for k in update_fields)
    cur.execute(f"UPDATE ayat SET {set_clause} WHERE ayah_key = '1:6'",
                list(update_fields.values()))

    # 2. Shift all rows with id >= 7 up by 1 (make room for new 1:7 at id=7)
    # SQLite enforces UNIQUE/PK constraints row-by-row during UPDATE, so a
    # single bulk UPDATE causes a collision (row 7 -> 8 collides with
    # existing row 8). Process in DESCENDING id order via a loop so each
    # row is moved out of the way before the next one needs its slot.
    ids_to_shift = [r[0] for r in cur.execute(
        "SELECT id FROM ayat WHERE id >= 7 ORDER BY id DESC"
    ).fetchall()]
    for old_id in ids_to_shift:
        cur.execute("UPDATE ayat SET id = ? WHERE id = ?", (old_id + 1, old_id))
    conn.commit()  # commit the shift before inserting

    # 3. Insert new row for 1:7 at id=7
    insert_fields = {
        "id": 7,
        "ayah_key": "1:7",
        "surah_name": "Al-Fatiha",
        "arabic": arabic_7,
        "roots": "{}",
        "divergence_score": 0.0,
        "gloss": "[]",
    }
    for col, (t6, t7) in split_results.items():
        insert_fields[col] = t7 if t7 is not None else ""

    cols_sql = ", ".join(insert_fields.keys())
    vals_sql = ", ".join("?" for _ in insert_fields)
    cur.execute(f"INSERT INTO ayat ({cols_sql}) VALUES ({vals_sql})",
                list(insert_fields.values()))

    conn.commit()

    # Verify
    total = cur.execute("SELECT COUNT(*) FROM ayat").fetchone()[0]
    print(f"\n  New total row count: {total} (expected 6236)")

    fatiha = cur.execute("SELECT id, ayah_key, arabic FROM ayat WHERE surah_name='Al-Fatiha' ORDER BY id").fetchall()
    print(f"\n  Al-Fatiha rows ({len(fatiha)}):")
    for r in fatiha:
        print(f"    id={r[0]:5}  {r[1]:5}  {r[2][:50]}")

    conn.close()
    print(f"\n  \u2705 Done. Now re-run: python scripts/fetch_roots.py")


if __name__ == "__main__":
    main()
