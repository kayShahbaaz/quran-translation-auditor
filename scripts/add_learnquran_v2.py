# scripts/add_learnquran_v2.py
# ─────────────────────────────────────────────────────────────────────────────
# Standalone, verbose version: adds trans_learnquran column and seeds
# Al-Fatiha 1:1-1:6 (1:7 will be seeded in a follow-up run after
# fix_fatiha_6_7.py creates that row).
#
# This version prints at every step to diagnose why the previous run
# produced no output.
#
# Usage: python scripts/add_learnquran_v2.py
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, sqlite3

print("[1] Script started", flush=True)

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")
print(f"[2] DB_PATH = {os.path.abspath(DB_PATH)}", flush=True)
print(f"[3] Exists  = {os.path.exists(DB_PATH)}", flush=True)

if not os.path.exists(DB_PATH):
    print("[ERROR] Database not found.")
    sys.exit(1)

conn = sqlite3.connect(DB_PATH)
cur  = conn.cursor()
print("[4] Connected to database", flush=True)

cols = [row[1] for row in cur.execute("PRAGMA table_info(ayat)").fetchall()]
print(f"[5] Current columns: {cols}", flush=True)

if "trans_learnquran" not in cols:
    print("[6] Adding trans_learnquran column...", flush=True)
    cur.execute("ALTER TABLE ayat ADD COLUMN trans_learnquran TEXT NOT NULL DEFAULT ''")
    conn.commit()
    print("[7] Column added and committed.", flush=True)
else:
    print("[6] Column already exists - skipping ALTER.", flush=True)

# Re-check
cols_after = [row[1] for row in cur.execute("PRAGMA table_info(ayat)").fetchall()]
print(f"[8] Columns after: {cols_after}", flush=True)
print(f"[9] trans_learnquran present: {'trans_learnquran' in cols_after}", flush=True)

# Seed Al-Fatiha 1:1-1:6 (1:7 doesn't exist yet - will be seeded after
# fix_fatiha_6_7.py runs)
FATIHA_LEARNQURAN = {
    "1:1": "All Hamd belongs to ALLAH, Rabb of al-Alamin.",
    "1:2": "Al-Rahman, Al-Rahim.",
    "1:3": "Malik of Yawm al-Din.",
    "1:4": "You alone we do Ibadah to, and You alone we seek Istianah from.",
    "1:5": "Guide us to the Sirat al-Mustaqim \u2014",
    "1:6": "The Sirat of those upon whom You bestowed Niamah \u2014",
    "1:7": "Not those upon whom Ghadab incurred, nor al-Dallin.",
}


print("[10] Seeding Al-Fatiha entries...", flush=True)
updated = 0
for ayah_key, text in FATIHA_LEARNQURAN.items():
    cur.execute("UPDATE ayat SET trans_learnquran = ? WHERE ayah_key = ?", (text, ayah_key))
    print(f"     {ayah_key}: rowcount={cur.rowcount}", flush=True)
    if cur.rowcount > 0:
        updated += 1

conn.commit()
print(f"[11] Updated {updated} rows.", flush=True)

conn.close()
print("[12] Done.", flush=True)
