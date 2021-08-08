# scripts/setup_db.py
# ─────────────────────────────────────────────────────────────────────────────
# Standalone script: initialise and seed the SQLite database.
# Run this once before starting the Flask server for the first time,
# or to reset the database to a clean state.
#
# Usage:
#   python scripts/setup_db.py          # init + seed
#   python scripts/setup_db.py --reset  # drop, recreate, reseed
# ─────────────────────────────────────────────────────────────────────────────

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from database import init_db, seed_db, reset_db, fetch_all_ayat

if __name__ == "__main__":
    if "--reset" in sys.argv:
        print("[SETUP] Resetting database...")
        reset_db()
    else:
        print("[SETUP] Initialising database...")
        init_db()
        seed_db()

    rows = fetch_all_ayat()
    print(f"\n[SETUP] Database ready — {len(rows)} Ayat loaded.")
    print(f"{'Ayah':>8}  {'Surah':<16}")
    print("-" * 28)
    for row in rows:
        print(f"{row['ayah_key']:>8}  {row['surah_name']:<16}")
    print("\n[SETUP] Done. Run `python run.py` to start the server.")
