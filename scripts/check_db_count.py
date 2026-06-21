# scripts/check_db_count.py
# Quick diagnostic: confirm total row count in ayat table and check
# for any gaps in ayah_key sequence (e.g. missing 1:7 or similar)

import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()

total = cur.execute("SELECT COUNT(*) FROM ayat").fetchone()[0]
print(f"Total rows in ayat table: {total}")
print(f"Expected: 6236\n")

# Check Al-Fatiha specifically
print("Al-Fatiha rows (surah_name = 'Al-Fatiha'):")
rows = cur.execute("SELECT id, ayah_key, arabic FROM ayat WHERE surah_name = 'Al-Fatiha' ORDER BY id").fetchall()
for r in rows:
    print(f"  id={r[0]:5}  ayah_key={r[1]:5}  arabic={r[2][:40]}")
print(f"  Total Al-Fatiha rows: {len(rows)} (expected 7)\n")

# Check for any duplicate ayah_keys
print("Checking for duplicate ayah_key values...")
dupes = cur.execute("""
    SELECT ayah_key, COUNT(*) as cnt FROM ayat
    GROUP BY ayah_key HAVING cnt > 1
""").fetchall()
print(f"  Duplicates found: {len(dupes)}")
for d in dupes[:10]:
    print(f"    {d[0]}: {d[1]} occurrences")

# Check first 10 and last 10 rows by id
print("\nFirst 10 rows by id:")
for r in cur.execute("SELECT id, ayah_key FROM ayat ORDER BY id LIMIT 10").fetchall():
    print(f"  id={r[0]:5}  ayah_key={r[1]}")

print("\nLast 5 rows by id:")
for r in cur.execute("SELECT id, ayah_key FROM ayat ORDER BY id DESC LIMIT 5").fetchall():
    print(f"  id={r[0]:5}  ayah_key={r[1]}")

conn.close()
