#!/usr/bin/env python3
"""
scripts/seed_fatiha_roots.py
────────────────────────────
Re-seeds roots for Al-Fatiha 1:1–1:7 into auditor.db.

mock_data.py only has 1:1, 1:2, 1:3 — the remaining four ayat
(1:4–1:7) are defined inline here from the standard Arabic root lexicon.

Run from the project root:
    python scripts/seed_fatiha_roots.py
"""
import sys, os, json, sqlite3
from pathlib import Path

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"

# ── Roots for all 7 Al-Fatiha ayat ─────────────────────────────────────────
# 1:1–1:3 match mock_data.py exactly.
# 1:4–1:7 added here (were never in mock_data.py).

FATIHA_ROOTS = {
    "1:1": {
        "الْحَمْدُ":     "ح-م-د",
        "لِلَّهِ":       "أ-ل-ه",
        "رَبِّ":         "ر-ب-ب",
        "الْعَالَمِينَ": "ع-ل-م",
    },
    "1:2": {
        "الرَّحْمَٰنِ": "ر-ح-م",
        "الرَّحِيمِ":   "ر-ح-م",
    },
    "1:3": {
        "مَالِكِ":   "م-ل-ك",
        "يَوْمِ":    "ي-و-م",
        "الدِّينِ":  "د-ي-ن",
    },
    "1:4": {
        "إِيَّاكَ":  "أ-ي-ك",   # you / thee (pronoun root)
        "نَعْبُدُ":  "ع-ب-د",   # we worship
        "نَسْتَعِينُ": "ع-و-ن",  # we seek help
    },
    "1:5": {
        "اهْدِنَا":     "ه-د-ي",   # guide us
        "الصِّرَاطَ":   "ص-ر-ط",   # the path/way
        "الْمُسْتَقِيمَ": "ق-و-م",  # the straight
    },
    "1:6": {
        "صِرَاطَ":      "ص-ر-ط",   # path of
        "أَنْعَمْتَ":   "ن-ع-م",   # you have blessed
        "عَلَيْهِمْ":   "ع-ل-و",   # upon them
    },
    "1:7": {
        "الْمَغْضُوبِ": "غ-ض-ب",   # those who have incurred wrath
        "الضَّالِّينَ": "ض-ل-ل",   # those who are astray
    },
}


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] Database not found at {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    # Verify the ayat exist before touching anything
    keys = list(FATIHA_ROOTS.keys())
    placeholders = ",".join("?" * len(keys))
    existing = cur.execute(
        f"SELECT ayah_key, roots FROM ayat WHERE ayah_key IN ({placeholders}) ORDER BY id",
        keys
    ).fetchall()

    if not existing:
        print("[ERROR] No Al-Fatiha rows found in ayat table. Check DB.")
        conn.close()
        sys.exit(1)

    print(f"\nFound {len(existing)}/7 Al-Fatiha rows in DB:\n")
    for row in existing:
        current = row["roots"]
        print(f"  {row['ayah_key']}  current roots = {current[:60]}{'...' if len(current) > 60 else ''}")

    print("\nSeeding roots...\n")
    updated = 0
    for row in existing:
        key   = row["ayah_key"]
        roots = FATIHA_ROOTS.get(key)
        if not roots:
            print(f"  SKIP {key} — no roots defined (unexpected)")
            continue

        cur.execute(
            "UPDATE ayat SET roots = ? WHERE ayah_key = ?",
            (json.dumps(roots, ensure_ascii=False), key)
        )
        print(f"  ✓ {key}  →  {list(roots.keys())}")
        updated += 1

    conn.commit()
    conn.close()

    print(f"\n{'─'*50}")
    print(f"Done. {updated}/{len(existing)} rows updated.")
    if len(existing) < 7:
        missing = set(keys) - {r["ayah_key"] for r in existing}
        print(f"[WARN] Missing from DB: {sorted(missing)}")
        print("       Run fix_fatiha_6_7.py first if 1:6/1:7 are missing.")


if __name__ == "__main__":
    main()