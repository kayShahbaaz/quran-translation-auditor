# scripts/check_fatiha_gloss.py
# ─────────────────────────────────────────────────────────────────────────────
# Diagnostic: inspect the raw quran.com gloss response for Surah 1
# to see exactly how Ayat are numbered/merged, so we can write the
# correct fix for fetch_gloss.py
#
# Usage: python scripts/check_fatiha_gloss.py
# ─────────────────────────────────────────────────────────────────────────────

import json, ssl, urllib.request

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

BASE_URL = "https://api.quran.com/api/v4"

url = (f"{BASE_URL}/verses/by_chapter/1"
       f"?language=en&words=true&word_fields=text_uthmani"
       f"&translation_fields=text&per_page=300")

req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0", "Accept": "application/json"})
with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
    data = json.loads(r.read().decode("utf-8"))

print(f"\nTotal verses returned for Surah 1: {len(data['verses'])}\n")

for verse in data["verses"]:
    key = verse["verse_key"]
    words = verse.get("words", [])
    glosses = []
    arabic_words = []
    for w in words:
        if w.get("char_type_name") == "end":
            continue
        translation = w.get("translation", {})
        text = translation.get("text", "") if isinstance(translation, dict) else ""
        arabic_words.append(w.get("text_uthmani", ""))
        if text:
            glosses.append(text)

    print(f"=== {key} ===")
    print(f"  Arabic words ({len(arabic_words)}): {arabic_words}")
    print(f"  Glosses ({len(glosses)}): {glosses}")
    print()
