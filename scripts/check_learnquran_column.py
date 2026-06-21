# scripts/check_learnquran_column.py
# Quick diagnostic: check current ayat table schema and whether
# trans_learnquran exists, plus check if data/auditor.db path
# resolves correctly from scripts/ directory.

import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

print(f"Resolved DB_PATH: {os.path.abspath(DB_PATH)}")
print(f"File exists: {os.path.exists(DB_PATH)}")
print(f"File size: {os.path.getsize(DB_PATH) if os.path.exists(DB_PATH) else 'N/A'} bytes\n")

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()

cols = cur.execute("PRAGMA table_info(ayat)").fetchall()
print("Current ayat table columns:")
for c in cols:
    print(f"  {c[1]:20} {c[2]}")

col_names = [c[1] for c in cols]
print(f"\ntrans_learnquran present: {'trans_learnquran' in col_names}")

conn.close()
