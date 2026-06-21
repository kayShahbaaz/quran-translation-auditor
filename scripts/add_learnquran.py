# scripts/add_learnquran.py
# ─────────────────────────────────────────────────────────────────────────────
# Adds the trans_learnquran column to the ayat table (if not present)
# and seeds the finalised Al-Fatiha (1:1–1:7) LearnQuran translations.
#
# Remaining Ayat (1:8 onward) keep trans_learnquran = '' (empty string)
# until future batches are added.
#
# Usage:
#   python scripts/add_learnquran.py
#
# Safe to re-run — uses idempotent ALTER/UPDATE.
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, sqlite3

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

# Al-Fatiha LearnQuran translations — finalised from al-fatiha-draft.md
# Edit these strings here if you make changes during your review,
# then re-run this script to update the database.
FATIHA_LEARNQURAN = {
    "1:1": "The praise is for Allah, Lord of the worlds.",
    "1:2": "The Most Merciful, the Ever-Merciful.",
    "1:3": "Owner of the Day of Recompense.",
    "1:4": "You [alone] we worship, and You [alone] we ask for help.",
    "1:5": "Guide us to the straight path \u2014",
    "1:6": "the path of those You have blessed \u2014",
    "1:7": "not the path of those who have incurred [Your] anger, nor of those who have gone astray.",
}


def add_column_if_missing(conn):
    cur  = conn.cursor()
    cols = [row[1] for row in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "trans_learnquran" not in cols:
        cur.execute("ALTER TABLE ayat ADD COLUMN trans_learnquran TEXT NOT NULL DEFAULT ''")
        conn.commit()
        print("[DB] Added trans_learnquran column.")
    else:
        print("[DB] trans_learnquran column already exists.")


def seed_fatiha(conn):
    cur = conn.cursor()
    updated = 0
    for ayah_key, text in FATIHA_LEARNQURAN.items():
        cur.execute(
            "UPDATE ayat SET trans_learnquran = ? WHERE ayah_key = ?",
            (text, ayah_key)
        )
        if cur.rowcount > 0:
            updated += 1
    conn.commit()
    print(f"[DB] Seeded {updated}/{len(FATIHA_LEARNQURAN)} Al-Fatiha LearnQuran entries.")


def verify(conn):
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT ayah_key, arabic, trans_learnquran
        FROM ayat
        WHERE ayah_key LIKE '1:%'
        ORDER BY id
        LIMIT 7
    """).fetchall()

    filled_total = cur.execute(
        "SELECT COUNT(*) FROM ayat WHERE trans_learnquran != ''"
    ).fetchone()[0]

    print(f"\n{'='*72}")
    print(f"  LEARNQURAN VERIFICATION — {filled_total} Ayat filled (of 6,236)")
    print(f"{'='*72}")
    for r in rows:
        print(f"\n  Ayah {r['ayah_key']}")
        print(f"  Arabic     : {r['arabic']}")
        lq = r['trans_learnquran'] or "(not yet translated)"
        print(f"  LearnQuran : {lq}")
    print(f"\n{'='*72}")


if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print(f"[ERROR] Database not found at {DB_PATH}")
        print("Run scripts/fetch_full_quran.py and scripts/fetch_kanzuliman.py first.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    add_column_if_missing(conn)
    seed_fatiha(conn)
    verify(conn)
    conn.close()

    print(f"\n  \u2705  Done! Al-Fatiha (1:1\u20131:7) LearnQuran translations loaded.")
    print(f"  \u25b6   Run: python run.py\n")
