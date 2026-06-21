# scripts/find_translation_ids.py
# ─────────────────────────────────────────────────────────────────────────────
# Finds the correct translation resource IDs on quran.com API v4
# Tests Ayah 1:2 (Alhamdulillah) to verify English output
# Usage: python scripts/find_translation_ids.py
# ─────────────────────────────────────────────────────────────────────────────

import urllib.request, json, ssl, time

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

BASE = "https://api.quran.com/api/v4"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
        return json.loads(r.read().decode("utf-8"))

# Step 1 — get all available English translations
print("Fetching all available translations from quran.com...\n")
data = fetch(f"{BASE}/resources/translations?language=en")
translations = data.get("translations", [])
print(f"Found {len(translations)} English translations\n")

# Step 2 — search for our 4 specific translators
targets = ["sahih", "haleem", "khattab", "bridges", "soliman", "clear quran", "clearquran"]

print(f"{'ID':<8} {'Name':<55} {'Author'}")
print("-" * 100)
for t in translations:
    name   = (t.get("name") or "").lower()
    author = (t.get("author_name") or "").lower()
    combined = name + " " + author
    if any(kw in combined for kw in targets):
        print(f"{t['id']:<8} {t.get('name',''):<55} {t.get('author_name','')}")

print("\n--- All English translations (full list) ---\n")
for t in translations:
    print(f"{t['id']:<8} {t.get('name',''):<55} {t.get('author_name','')}")
