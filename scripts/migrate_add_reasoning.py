#!/usr/bin/env python3
"""
scripts/migrate_add_reasoning.py
─────────────────────────────────
Adds a `reasoning` TEXT column to the ayat table.
Safe to run multiple times — skips if column already exists.

Run from project root:
    python scripts/migrate_add_reasoning.py
"""
import sqlite3, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # Check if column already exists
    cols = [r[1] for r in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "reasoning" in cols:
        print("[OK] `reasoning` column already exists — nothing to do.")
        conn.close()
        return

    cur.execute("ALTER TABLE ayat ADD COLUMN reasoning TEXT")
    conn.commit()
    conn.close()
    print("[OK] `reasoning` TEXT column added to ayat table.")

if __name__ == "__main__":
    main()