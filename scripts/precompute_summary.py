#!/usr/bin/env python3
"""
scripts/precompute_summary.py
──────────────────────────────
Pre-computes per-surah per-translator average Literal Accuracy scores
and stores them in a `surah_summary` table in the DB.

This runs once (or when re-seeding). The /surahs page reads from this
table instead of scoring all 6236 ayat on every page load.

Run from project root:
    python scripts/precompute_summary.py
"""
import sys, os, json, sqlite3
from pathlib import Path

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"
sys.path.insert(0, str(ROOT / "src"))

from fidelity_engine import score_all_translators, TRANSLATOR_KEYS

DIVIDER = "─" * 60


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    # Create summary table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS surah_scores (
            surah_name      TEXT PRIMARY KEY,
            ayah_count      INTEGER,
            avg_sahih       REAL,
            avg_haleem      REAL,
            avg_khattab     REAL,
            avg_soliman     REAL,
            avg_kanzuliman  REAL,
            avg_overall     REAL,
            computed_at     TEXT DEFAULT (datetime('now'))
        )
    """)
    conn.commit()

    # Get distinct surahs in order
    surahs = [r[0] for r in cur.execute(
        "SELECT surah_name FROM ayat GROUP BY surah_name ORDER BY MIN(id)"
    ).fetchall()]

    print(f"\n{DIVIDER}")
    print(f"  PRECOMPUTE SURAH SCORES")
    print(f"  {len(surahs)} surahs to process")
    print(DIVIDER)

    for i, surah_en in enumerate(surahs, 1):
        ayat = cur.execute(
            "SELECT trans_sahih, trans_haleem, trans_khattab, "
            "trans_soliman, trans_kanzuliman, gloss "
            "FROM ayat WHERE surah_name=? ORDER BY id",
            (surah_en,)
        ).fetchall()

        ayah_count = len(ayat)
        sums   = {k: 0.0 for k in TRANSLATOR_KEYS}
        counts = {k: 0   for k in TRANSLATOR_KEYS}

        for row in ayat:
            gloss = json.loads(row["gloss"]) if row["gloss"] else []
            if not gloss:
                continue

            translations = {
                "sahih":      row["trans_sahih"]     or "",
                "haleem":     row["trans_haleem"]     or "",
                "khattab":    row["trans_khattab"]    or "",
                "soliman":    row["trans_soliman"]    or "",
                "kanzuliman": row["trans_kanzuliman"] or "",
            }

            scores = score_all_translators(translations, {}, gloss)

            for tkey in TRANSLATOR_KEYS:
                sdata  = scores.get(tkey) or {}
                gscore = sdata.get("gloss", {}).get("score") if sdata.get("gloss") else None
                if gscore is not None:
                    sums[tkey]   += gscore
                    counts[tkey] += 1

        avgs = {
            k: round(sums[k] / counts[k], 4) if counts[k] else None
            for k in TRANSLATOR_KEYS
        }

        valid   = [v for v in avgs.values() if v is not None]
        overall = round(sum(valid) / len(valid), 4) if valid else None

        cur.execute("""
            INSERT OR REPLACE INTO surah_scores
            (surah_name, ayah_count, avg_sahih, avg_haleem, avg_khattab,
             avg_soliman, avg_kanzuliman, avg_overall)
            VALUES (?,?,?,?,?,?,?,?)
        """, (
            surah_en, ayah_count,
            avgs.get("sahih"), avgs.get("haleem"), avgs.get("khattab"),
            avgs.get("soliman"), avgs.get("kanzuliman"), overall
        ))

        bar = "█" * int((i / len(surahs)) * 30)
        print(f"\r  [{bar:<30}] {i}/{len(surahs)} {surah_en[:20]:<20}", end="", flush=True)

    conn.commit()
    conn.close()
    print(f"\n\n{DIVIDER}")
    print(f"  DONE — {len(surahs)} surahs computed and stored in surah_scores table")
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()