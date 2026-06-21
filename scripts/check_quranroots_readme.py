# scripts/check_quranroots_readme.py
# ─────────────────────────────────────────────────────────────────────────────
# Fetches README.md from AbstractThinker0/quran-roots to understand the
# indexing scheme used in "occurences" (e.g. "37:2", "50:1,9").
#
# Also fetches the companion quran.json (Tanzil-aligned text) if it exists,
# to cross-reference position 1 = which Surah:Ayah.
#
# Usage: python scripts/check_quranroots_readme.py
# ─────────────────────────────────────────────────────────────────────────────

import json, ssl, urllib.request

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode    = ssl.CERT_NONE


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
        with urllib.request.urlopen(req, timeout=30, context=SSL_CTX) as r:
            return r.read().decode("utf-8")
    except Exception as e:
        return f"__ERROR__: {e}"


print("="*72)
print("  README.md")
print("="*72)
readme = fetch("https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/README.md")
print(readme[:3000])

print("\n" + "="*72)
print("  txt/README.md")
print("="*72)
txt_readme = fetch("https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/txt/README.md")
print(txt_readme[:3000])

# Try to find a companion "quran.json" with the text aligned to same indices
print("\n" + "="*72)
print("  Looking for companion quran text file (quran.json)")
print("="*72)
for candidate in ["quran.json", "data/quran.json", "txt/quran.json"]:
    url = f"https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/{candidate}"
    result = fetch(url)
    if not result.startswith("__ERROR__"):
        print(f"  FOUND: {url} ({len(result):,} bytes)")
        try:
            data = json.loads(result)
            if isinstance(data, list):
                print(f"  First 3 items: {data[:3]}")
            elif isinstance(data, dict):
                keys = list(data.keys())[:5]
                print(f"  First keys: {keys}")
        except:
            print(f"  First 300 chars: {result[:300]}")
    else:
        print(f"  Not found: {candidate}")

# Check root-word.txt format too (might have explicit surah:ayah:word format)
print("\n" + "="*72)
print("  txt/quran-root.txt (first 2000 chars)")
print("="*72)
roottxt = fetch("https://raw.githubusercontent.com/AbstractThinker0/quran-roots/main/txt/quran-root.txt")
print(roottxt[:2000])
