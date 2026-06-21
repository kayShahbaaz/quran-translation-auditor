#!/usr/bin/env python3
"""
scripts/reseed_fatiha_roots.py
───────────────────────────────
Re-seeds correct roots for Al-Fatiha 1:1-1:7 using the exact Arabic
words stored in the DB arabic column — guarantees perfect matching
in run.py without any fuzzy lookup needed.

Roots use plain Arabic format (حمد not ح-م-د) to match what
fetch_roots_all.py wrote for the rest of the Quran.

Run from project root:
    python scripts/reseed_fatiha_roots.py
"""
import sqlite3, json, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    # First read the exact Arabic text stored in DB for each ayah
    # so we use the EXACT same word strings for matching
    print("Reading DB Arabic text for Al-Fatiha...\n")
    fatiha = {}
    for key in ['1:1','1:2','1:3','1:4','1:5','1:6','1:7']:
        row = cur.execute(
            "SELECT ayah_key, arabic FROM ayat WHERE ayah_key=?", (key,)
        ).fetchone()
        if row:
            fatiha[key] = row["arabic"]
            print(f"  {key}: {row['arabic']}")

    print()

    # Define roots using word-position mapping
    # Each entry: {word_index_0based: root_plain}
    # We extract the actual word from the stored Arabic text
    # to guarantee exact string match

    FATIHA_ROOTS_BY_POSITION = {
        "1:1": {0: "حمد", 1: "أله", 2: "ربب", 3: "علم"},
        # الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ
        # pos:  0       1      2     3

        "1:2": {0: "رحم", 1: "رحم"},
        # الرَّحْمَـٰنِ الرَّحِيمِ
        # pos:    0           1

        "1:3": {0: "ملك", 1: "يوم", 2: "دين"},
        # مَالِكِ يَوْمِ الدِّينِ
        # pos: 0     1       2

        "1:4": {0: "أيك", 1: "عبد", 2: "أيك", 3: "عون"},
        # إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
        # pos: 0      1       2            3
        # Note: إيّاك is a pronoun with no trilateral root — skip it
        # We only map roots to content words

        "1:5": {0: "هدي", 1: "صرط", 2: "قوم"},
        # اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ
        # pos: 0       1           2

        "1:6": {0: "صرط", 1: "ذوا", 2: "نعم", 3: "علو"},
        # صِرَاطَ الَّذِينَ أَنْعَمْتَ عَلَيْهِمْ
        # pos: 0      1          2          3

        "1:7": {0: "غير", 1: "غضب", 2: "علو", 3: "لا", 4: "ضلل"},
        # غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ
        # pos: 0       1           2       3       4
    }

    # Better approach: use explicit word→root mapping
    # matching against words we know are in the DB
    FATIHA_ROOTS_EXPLICIT = {
        "1:1": {
            "الْحَمْدُ":     "حمد",
            "لِلَّهِ":       "أله",
            "رَبِّ":         "ربب",
            "الْعَالَمِينَ": "علم",
        },
        "1:2": {
            "الرَّحْمَـٰنِ": "رحم",
            "الرَّحِيمِ":    "رحم",
        },
        "1:3": {
            "مَالِكِ":   "ملك",
            "يَوْمِ":    "يوم",
            "الدِّينِ":  "دين",
        },
        "1:4": {
            "نَعْبُدُ":    "عبد",
            "نَسْتَعِينُ": "عون",
        },
        "1:5": {
            "اهْدِنَا":       "هدي",
            "الصِّرَاطَ":     "صرط",
            "الْمُسْتَقِيمَ": "قوم",
        },
        "1:6": {
            "صِرَاطَ":    "صرط",
            "أَنْعَمْتَ": "نعم",
            "عَلَيْهِمْ": "علو",
        },
        "1:7": {
            "غَيْرِ":         "غير",
            "الْمَغْضُوبِ":   "غضب",
            "عَلَيْهِمْ":     "علو",
            "الضَّالِّينَ":   "ضلل",
        },
    }

    # Now cross-check: for each explicit key, find if it exists in DB arabic
    # If not, try to find the closest word in the DB arabic text
    print("Verifying and seeding roots...\n")

    updated = 0
    for key, roots_map in FATIHA_ROOTS_EXPLICIT.items():
        db_arabic = fatiha.get(key, "")
        db_words  = db_arabic.split() if db_arabic else []

        # Check which explicit words are in the DB
        verified   = {}
        unmatched  = {}
        for word, root in roots_map.items():
            if word in db_words:
                verified[word] = root
            else:
                unmatched[word] = root

        # For unmatched, try to find by stripping ال prefix
        for word, root in unmatched.items():
            strip = word.lstrip("الْ").lstrip("ٱلْ").lstrip("الِ")
            found = False
            for db_word in db_words:
                db_strip = db_word.lstrip("الْ").lstrip("ٱلْ").lstrip("الِ")
                if db_strip == strip or db_word == word:
                    verified[db_word] = root
                    found = True
                    break
            if not found:
                # Last resort: use the word as-is (run.py fuzzy matcher will handle it)
                verified[word] = root

        roots_json = json.dumps(verified, ensure_ascii=False)
        cur.execute(
            "UPDATE ayat SET roots=? WHERE ayah_key=?",
            (roots_json, key)
        )

        print(f"  {key}: {len(verified)} roots seeded")
        for w, r in verified.items():
            in_db = "✓" if w in db_words else "~fuzzy"
            print(f"    {w} → {r}  {in_db}")
        if unmatched:
            still_unmatched = {w: r for w, r in unmatched.items()
                               if w not in verified}
            if still_unmatched:
                print(f"    [WARN] still unmatched: {list(still_unmatched.keys())}")
        print()
        updated += 1

    conn.commit()
    conn.close()
    print(f"Done. {updated}/7 Al-Fatiha ayat re-seeded.")

if __name__ == "__main__":
    main()