# scripts/export_csv.py
# ─────────────────────────────────────────────────────────────────────────────
# Export the full audited Ayat dataset (including divergence scores) to CSV.
# Output is saved to data/exports/audit_results.csv
#
# Usage:
#   python scripts/export_csv.py
# ─────────────────────────────────────────────────────────────────────────────

import sys
import os
import csv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from database import fetch_all_ayat

EXPORT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "data", "exports", "audit_results.csv"
)

FIELDS = [
    "id", "ayah_key", "surah_name", "arabic",
    "trans_sahih", "trans_haleem", "trans_khattab", "trans_soliman",
    "divergence_score"
]

if __name__ == "__main__":
    rows = fetch_all_ayat()
    os.makedirs(os.path.dirname(EXPORT_PATH), exist_ok=True)

    with open(EXPORT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row))

    print(f"[EXPORT] Exported {len(rows)} rows → {EXPORT_PATH}")
