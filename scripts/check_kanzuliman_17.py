# scripts/check_kanzuliman_17.py
# ─────────────────────────────────────────────────────────────────────────────
# Before applying fix_fatiha_6_7.py, check whether trans_kanzuliman for 1:6
# already correctly contains ONLY 1:6 content (with 1:7 stored elsewhere,
# e.g. orphaned, or simply never written because row 1:7 never existed),
# OR whether it's been silently merged/truncated like the other columns.
#
# Also tests refined split markers for Haleem and Khattab against their
# actual stored text.
#
# Usage: python scripts/check_kanzuliman_17.py
# ─────────────────────────────────────────────────────────────────────────────

import sqlite3, os, re

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "auditor.db")

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
cur = conn.cursor()

row = dict(cur.execute("SELECT * FROM ayat WHERE ayah_key = '1:6'").fetchone())

print("="*72)
print("  trans_kanzuliman for 1:6 (full text)")
print("="*72)
print(f"  {row['trans_kanzuliman']!r}")
print(f"  Length: {len(row['trans_kanzuliman'])} chars")

print("\n" + "="*72)
print("  Expected from barkati.net fetch (Al-Fatiha 1:7 Kanzul Iman):")
print("  'Not the path of those who earned Your anger - nor of those")
print("   who are astray.' (or similar wording)")
print("="*72)

# ── Refined Haleem split test ─────────────────────────────────────────────────
print("\n" + "="*72)
print("  HALEEM - testing refined markers")
print("="*72)
haleem = row["trans_haleem"]
print(f"  Full text: {haleem!r}")

# Haleem's structure may be: "the path of those You have blessed,
#  those who incur no anger and who have not gone astray."
# This is a SINGLE sentence describing the whole path (1:6) with
# 1:7's negation embedded as a relative clause modifying "those" -
# i.e. Haleem may not have a clean syntactic split point at all,
# since "those who incur no anger and who have not gone astray"
# describes the SAME group differently than other translators.
#
# Try splitting at "those who incur" instead:
for marker in ["those who incur", ", those who", "and who have not"]:
    idx = haleem.find(marker)
    print(f"  marker {marker!r:30} -> idx={idx}")
    if idx > 0:
        print(f"    1:6: {haleem[:idx]!r}")
        print(f"    1:7: {haleem[idx:]!r}")

# ── Refined Khattab split test ──────────────────────────────────────────────────
print("\n" + "="*72)
print("  KHATTAB - testing refined markers")
print("="*72)
khattab = row["trans_khattab"]
print(f"  Full text: {khattab!r}")

for marker in ["—not", "\u2014not", "not those", "Not those"]:
    idx = khattab.find(marker)
    print(f"  marker {marker!r:30} -> idx={idx}")
    if idx > 0:
        print(f"    1:6: {khattab[:idx]!r}")
        print(f"    1:7: {khattab[idx:]!r}")

conn.close()
