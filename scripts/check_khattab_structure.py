# scripts/check_khattab_structure.py
# Inspects the actual JSON structure of the Khattab edition from jsdelivr
# Usage: python scripts/check_khattab_structure.py

import urllib.request, json, ssl

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

URL = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/eng-mustafakhattaba.json"

print("Fetching Khattab JSON...")
req  = urllib.request.Request(URL, headers={"User-Agent": "QuranAuditor/1.0"})
with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
    data = json.loads(r.read().decode("utf-8"))

print(f"\nTop-level keys: {list(data.keys())}")
print(f"Type of data: {type(data)}")

# Show structure of first few entries
for key in list(data.keys())[:3]:
    val = data[key]
    print(f"\nKey: '{key}' → type: {type(val)}")
    if isinstance(val, dict):
        subkeys = list(val.keys())[:5]
        print(f"  Sub-keys (first 5): {subkeys}")
        for sk in subkeys[:2]:
            print(f"  [{sk}] → {str(val[sk])[:80]}")
    elif isinstance(val, list):
        print(f"  List length: {len(val)}")
        print(f"  First item: {str(val[0])[:80]}")
        if len(val) > 1:
            print(f"  Second item: {str(val[1])[:80]}")
    else:
        print(f"  Value: {str(val)[:80]}")
