# scripts/check_quranroots_format2.py
# ─────────────────────────────────────────────────────────────────────────────
# Diagnostic: inspect the structure of quranRoots.json from
# AbstractThinker0/quran-roots (confirmed to exist at repo root).
#
# Usage: python scripts/check_quranroots_format2.py
# ─────────────────────────────────────────────────────────────────────────────

import json, ssl, urllib.request

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE

URLS = [
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/quranRoots.json",
    "https://raw.githubusercontent.com/AbstractThinker0/quran-roots/master/quranRoots.json",
]


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
            return r.read().decode("utf-8")
    except Exception as e:
        return f"__ERROR__: {e}"


for url in URLS:
    print(f"\nTrying: {url}")
    raw = fetch(url)
    if raw.startswith("__ERROR__"):
        print(f"  {raw}")
        continue

    print(f"  OK - {len(raw):,} bytes")
    data = json.loads(raw)
    print(f"  Top-level type: {type(data)}")

    if isinstance(data, dict):
        keys = list(data.keys())
        print(f"  Number of top-level keys: {len(keys)}")
        print(f"  First 10 keys: {keys[:10]}")
        # Show a sample entry
        first_key = keys[0]
        print(f"\n  Sample entry data['{first_key}']:")
        print(f"  {json.dumps(data[first_key], ensure_ascii=False, indent=2)[:500]}")

        # Try to find Al-Fatiha entries (keys starting with "1:")
        fatiha_keys = [k for k in keys if k.startswith("1:") or k.startswith("1_")][:10]
        print(f"\n  Keys matching Al-Fatiha pattern (1:* or 1_*): {fatiha_keys}")
        for fk in fatiha_keys[:3]:
            print(f"  data['{fk}'] = {json.dumps(data[fk], ensure_ascii=False)[:300]}")

    elif isinstance(data, list):
        print(f"  List length: {len(data)}")
        print(f"  First 5 items:")
        for item in data[:5]:
            print(f"    {json.dumps(item, ensure_ascii=False)[:200]}")

    break  # stop after first successful fetch
