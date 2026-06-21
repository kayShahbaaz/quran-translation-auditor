# scripts/check_root_format.py
# ─────────────────────────────────────────────────────────────────────────────
# Diagnostic: inspect the raw 'root' field format returned by quran.com
# for known Al-Fatiha words, so we can build a correct transliteration map.
#
# Usage: python scripts/check_root_format.py
# ─────────────────────────────────────────────────────────────────────────────

import json, ssl, urllib.request

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

BASE_URL = "https://api.quran.com/api/v4"

url = (f"{BASE_URL}/verses/by_chapter/1"
       f"?language=en&words=true&word_fields=text_uthmani,root"
       f"&per_page=300")

req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0", "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
    data = json.loads(r.read().decode("utf-8"))

print(f"\nTotal verses: {len(data['verses'])}\n")

for verse in data["verses"]:
    key = verse["verse_key"]
    print(f"=== {key} ===")
    for w in verse.get("words", []):
        if w.get("char_type_name") == "end":
            continue
        arabic = w.get("text_uthmani", "")
        root   = w.get("root", "")
        print(f"  {arabic:20} root={root!r}")
    print()
