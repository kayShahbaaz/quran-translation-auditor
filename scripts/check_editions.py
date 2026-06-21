# scripts/check_editions.py
# ─────────────────────────────────────────────────────────────────────────────
# Run this to find which edition identifiers on alquran.cloud
# actually return ENGLISH text for the 4 translations we need.
#
# Usage: python scripts/check_editions.py
# ─────────────────────────────────────────────────────────────────────────────

import urllib.request, json, ssl, time

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

BASE = "https://api.alquran.cloud/v1/ayah/1:1/"

# All known English edition identifiers to test
CANDIDATES = [
    "en.sahih",
    "en.abdulhaleem",
    "en.ahmedali",
    "en.arberry",
    "en.asad",
    "en.clearquran",
    "en.daryabadi",
    "en.hilali",
    "en.itani",
    "en.maududi",
    "en.mubarakpuri",
    "en.pickthall",
    "en.qaribullah",
    "en.sarwar",
    "en.shakir",
    "en.transliteration",
    "en.wahiduddin",
    "en.yusufali",
    "en.bridges",
    "en.khattab",
]

print("\nTesting all English edition identifiers on alquran.cloud")
print("Ayah 1:1 — should return: 'All praise is...' or similar\n")
print(f"{'Edition':<30} {'Status':<10} {'Text preview'}")
print("-" * 80)

for edition in CANDIDATES:
    url = BASE + edition
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
        with urllib.request.urlopen(req, timeout=10, context=SSL_CTX) as r:
            data = json.loads(r.read().decode("utf-8"))
        if data.get("code") == 200:
            text = data["data"]["text"]
            # Check if it's actually English (simple heuristic: starts with ASCII)
            is_english = text and ord(text[0]) < 128
            status = "✅ English" if is_english else "❌ Arabic"
            print(f"{edition:<30} {status:<10} {text[:50]}")
        else:
            print(f"{edition:<30} {'❌ '+str(data.get('code')):<10}")
    except Exception as e:
        print(f"{edition:<30} {'❌ Error':<10} {str(e)[:40]}")
    time.sleep(0.3)

print("\nDone. Use the ✅ English editions in fetch_full_quran.py")
