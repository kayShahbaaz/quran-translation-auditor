# scripts/check_quranroots_format.py
# ─────────────────────────────────────────────────────────────────────────────
# Diagnostic: inspect the structure of AbstractThinker0/quran-roots JSON data
# (root list aligned with Tanzil Quran text v1.1) to confirm format before
# building the real fetch_roots.py fetcher.
#
# Source repo: https://github.com/AbstractThinker0/quran-roots
#
# Usage: python scripts/check_quranroots_format.py
# ─────────────────────────────────────────────────────────────────────────────

import json, ssl, urllib.request

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

# Candidate raw URLs to try - repo structure may vary
CANDIDATE_URLS = [
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/quran.json",
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/master/quran.json",
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/data/quran.json",
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/roots.json",
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/quran-roots.json",
]


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
        with urllib.request.urlopen(req, timeout=20, context=SSL_CTX) as r:
            return r.read().decode("utf-8")
    except Exception as e:
        return f"__ERROR__: {e}"


print("\n" + "="*72)
print("  Checking AbstractThinker0/quran-roots structure")
print("="*72 + "\n")

for url in CANDIDATE_URLS:
    print(f"Trying: {url}")
    raw = fetch(url)
    if raw.startswith("__ERROR__"):
        print(f"  {raw}\n")
        continue

    print(f"  OK - {len(raw)} bytes")
    try:
        data = json.loads(raw)
        print(f"  Parsed JSON. Type: {type(data)}")
        if isinstance(data, dict):
            keys = list(data.keys())
            print(f"  Top-level keys (first 10): {keys[:10]}")
            first_key = keys[0]
            print(f"  data['{first_key}'] = {data[first_key]!r}"[:300])
        elif isinstance(data, list):
            print(f"  List length: {len(data)}")
            print(f"  First 3 items: {data[:3]}"[:500])
    except Exception as e:
        print(f"  JSON parse error: {e}")
        print(f"  First 300 chars: {raw[:300]}")
    print()

# Also try listing repo contents via GitHub API
print("="*72)
print("  Listing repo file tree via GitHub API")
print("="*72 + "\n")

api_url = "https://api.github.com/repos/AbstractThinker0/quran-roots/git/trees/main?recursive=1"
raw = fetch(api_url)
if raw.startswith("__ERROR__"):
    print(raw)
    # Try master branch
    api_url = "https://api.github.com/repos/AbstractThinker0/quran-roots/git/trees/master?recursive=1"
    raw = fetch(api_url)
    if raw.startswith("__ERROR__"):
        print(raw)

if not raw.startswith("__ERROR__"):
    try:
        tree = json.loads(raw)
        for item in tree.get("tree", []):
            print(f"  {item['path']}  ({item.get('type')})")
    except Exception as e:
        print(f"  Parse error: {e}")
        print(raw[:500])
