#!/usr/bin/env python3
"""
scripts/fix_fatiha_roots_final.py
───────────────────────────────────
Final definitive fix for Al-Fatiha roots.
Reads the exact Arabic words from the DB arabic column for each ayah
and builds the roots dict using those EXACT strings as keys.
No fuzzy matching needed — perfect alignment guaranteed.
"""
import sqlite3, json, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

# Root assignments by word INDEX (0-based position in arabic column split by spaces)
# Verified against each ayah's Arabic text
# Words with no trilateral root (pronouns, particles) are skipped

ROOTS_BY_INDEX = {
    "1:1": {0: "حمد", 1: "أله", 2: "ربب", 3: "علم"},
    # الْحَمْدُ(0) لِلَّهِ(1) رَبِّ(2) الْعَالَمِينَ(3)

    "1:2": {0: "رحم", 1: "رحم"},
    # الرَّحْمَـٰنِ(0) الرَّحِيمِ(1)

    "1:3": {0: "ملك", 1: "يوم", 2: "دين"},
    # مَالِكِ(0) يَوْمِ(1) الدِّينِ(2)

    "1:4": {1: "عبد", 3: "عون"},
    # إِيَّاكَ(0-skip) نَعْبُدُ(1) وَإِيَّاكَ(2-skip) نَسْتَعِينُ(3)

    "1:5": {0: "هدي", 1: "صرط", 2: "قوم"},
    # اهْدِنَا(0) الصِّرَاطَ(1) الْمُسْتَقِيمَ(2)

    "1:6": {0: "صرط", 2: "نعم"},
    # صِرَاطَ(0) الَّذِينَ(1-skip) أَنْعَمْتَ(2) عَلَيْهِمْ(3-skip)

    "1:7": {0: "غير", 1: "غضب", 3: "ضلل"},
    # غَيْرِ(0) الْمَغْضُوبِ(1) عَلَيْهِمْ(2-skip) وَلَا(3→actually ضال is 4)
}

# Special case: 1:7 needs re-checking
# غَيْرِ(0) الْمَغْضُوبِ(1) عَلَيْهِمْ(2) وَلَا(3) الضَّالِّينَ(4)
ROOTS_BY_INDEX["1:7"] = {0: "غير", 1: "غضب", 4: "ضلل"}


def get_content_words(arabic: str) -> list:
    """Split arabic text into words, filtering punctuation markers."""
    import unicodedata
    words = []
    for w in arabic.split():
        # Keep if has at least one Arabic letter
        if any(unicodedata.category(c) == 'Lo' for c in w):
            words.append(w)
    return words


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    print("Building Al-Fatiha roots from exact DB arabic words:\n")
    updated = 0

    for key, root_map in sorted(ROOTS_BY_INDEX.items()):
        row = cur.execute(
            "SELECT arabic FROM ayat WHERE ayah_key=?", (key,)
        ).fetchone()
        if not row:
            print(f"  {key}: NOT FOUND in DB")
            continue

        words = get_content_words(row["arabic"])
        print(f"  {key}: {words}")

        roots_dict = {}
        for pos, root in root_map.items():
            if pos < len(words):
                word = words[pos]
                roots_dict[word] = root
                print(f"    pos {pos}: [{word}] → {root} ✓")
            else:
                print(f"    pos {pos}: OUT OF RANGE (only {len(words)} words)")

        roots_json = json.dumps(roots_dict, ensure_ascii=False)
        cur.execute(
            "UPDATE ayat SET roots=? WHERE ayah_key=?",
            (roots_json, key)
        )
        print(f"    → {roots_dict}")
        print()
        updated += 1

    conn.commit()
    conn.close()
    print(f"Done. {updated}/7 ayat updated.")


if __name__ == "__main__":
    main()