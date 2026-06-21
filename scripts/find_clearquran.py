# scripts/find_clearquran.py
# ─────────────────────────────────────────────────────────────────────────────
# Tests multiple APIs and sources for Mustafa Khattab / The Clear Quran
# Usage: python scripts/find_clearquran.py
# ─────────────────────────────────────────────────────────────────────────────

import urllib.request, json, ssl, time

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

def fetch(url, label=""):
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "QuranAuditor/1.0", "Accept": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=15, context=SSL_CTX) as r:
            return json.loads(r.read().decode("utf-8")), None
    except Exception as e:
        return None, str(e)

print("\n" + "="*70)
print("  Searching for Mustafa Khattab / The Clear Quran across APIs")
print("="*70 + "\n")

# ── Test 1: api.qurancdn.com ──────────────────────────────────────────────────
print("[1] Testing api.qurancdn.com editions...")
data, err = fetch("https://api.qurancdn.com/api/qdc/translations?language=en")
if data:
    translations = data.get("translations", [])
    for t in translations:
        name = (t.get("name") or "").lower()
        author = (t.get("author_name") or "").lower()
        if any(k in name+author for k in ["khattab","clear quran","clearquran"]):
            print(f"  FOUND → ID:{t['id']}  Name:{t.get('name')}  Author:{t.get('author_name')}")
else:
    print(f"  Error: {err}")

# ── Test 2: cdn.jsdelivr.net quran-json ───────────────────────────────────────
print("\n[2] Testing cdn.jsdelivr.net/gh/fawazahmed0/quran-api...")
data, err = fetch("https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.json")
if data:
    for key, val in data.items():
        name = str(val).lower() if isinstance(val, str) else ""
        if isinstance(val, dict):
            name = (val.get("name","") + val.get("author","")).lower()
        if any(k in key.lower()+name for k in ["khattab","clearquran","clear-quran"]):
            print(f"  FOUND → key:{key}  val:{val}")
    # Also try listing all english
    print("  Checking all entries with 'en' in key...")
    count = 0
    for key in data.keys():
        if "khattab" in key.lower() or "clear" in key.lower():
            print(f"    {key}: {data[key]}")
            count += 1
    if count == 0:
        print("  Not found in this API")
else:
    print(f"  Error: {err}")

# ── Test 3: quranapi.pages.dev ────────────────────────────────────────────────
print("\n[3] Testing quranapi.pages.dev...")
data, err = fetch("https://quranapi.pages.dev/api/surah.json")
if data:
    print(f"  Accessible — checking structure: {str(data)[:100]}")
else:
    print(f"  Error: {err}")

# ── Test 4: alquran.cloud all editions ────────────────────────────────────────
print("\n[4] Testing alquran.cloud full editions list for Khattab...")
data, err = fetch("https://api.alquran.cloud/v1/edition?language=en&type=translation")
if data:
    editions = data.get("data", [])
    print(f"  Found {len(editions)} English translation editions")
    for e in editions:
        name   = (e.get("name","") or "").lower()
        eng    = (e.get("englishName","") or "").lower()
        ident  = (e.get("identifier","") or "").lower()
        if any(k in name+eng+ident for k in ["khattab","clear quran","clearquran"]):
            print(f"  FOUND → identifier:{e.get('identifier')}  name:{e.get('name')}  englishName:{e.get('englishName')}")
    # print all identifiers for reference
    print("\n  All available English identifiers on alquran.cloud:")
    for e in editions:
        print(f"    {e.get('identifier',''):<30} {e.get('englishName','')}")
else:
    print(f"  Error: {err}")

# ── Test 5: raw GitHub quran-json repo ────────────────────────────────────────
print("\n[5] Testing raw GitHub quran-json (risan/quran-json)...")
data, err = fetch("https://raw.githubusercontent.com/risan/quran-json/main/data/translations/en.json")
if data:
    print(f"  Accessible — type:{type(data)}, keys sample: {list(data.keys())[:5]}")
else:
    print(f"  Error: {err}")

print("\n" + "="*70)
print("  Done. Paste full output to Claude.")
print("="*70 + "\n")
