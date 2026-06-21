#!/usr/bin/env python3
"""
scripts/fix_short_gloss.py
───────────────────────────
Finds ayat where the stored gloss has fewer items than the ayah's
word count (indicating a truncated or failed fetch) and re-fetches
from quran.com.

Run from project root:
    python scripts/fix_short_gloss.py --dry-run
    python scripts/fix_short_gloss.py
"""
import sys, os, json, sqlite3, time, argparse, urllib.request, unicodedata
from pathlib import Path

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"
API     = "https://api.quran.com/api/v4/verses/by_key/{key}?words=true&word_fields=text_uthmani&translation_fields=text&translations=131"
DIVIDER = "─" * 60


def count_arabic_words(arabic: str) -> int:
    """Count content words in Arabic text (exclude punctuation markers)."""
    if not arabic:
        return 0
    words = []
    for w in arabic.split():
        # Skip standalone punctuation markers (ۚ ۖ ۗ etc.)
        if all(unicodedata.category(c) in ('Po','Mn','Cf','So','No','Zs')
               for c in w if c.strip()):
            continue
        words.append(w)
    return len(words)


def fetch_gloss(ayah_key: str) -> list:
    """Fetch word-by-word English gloss from quran.com."""
    # quran.com uses 1-based ayah within surah; Al-Fatiha offset handled below
    surah, ayah = ayah_key.split(":")
    # quran.com numbers Al-Fatiha with Bismillah as 1:1, so offset by +1
    if surah == "1":
        ayah = str(int(ayah) + 1)
    api_key = f"{surah}:{ayah}"

    url = API.format(key=api_key)
    req = urllib.request.Request(url, headers={"User-Agent": "QuranAuditor/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
    except Exception as e:
        print(f"    [ERROR] {ayah_key}: {e}")
        return []

    words = data.get("verse", {}).get("words", [])
    gloss = []
    for w in words:
        if w.get("char_type_name") == "word":
            trans = w.get("translation", {}).get("text", "").strip()
            if trans and trans not in ("(1)", "(2)", "(3)"):
                gloss.append(trans)
    return gloss


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--threshold", type=float, default=0.5,
                        help="Flag if gloss items < threshold * arabic_word_count (default 0.5)")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    rows = cur.execute(
        "SELECT ayah_key, arabic, gloss FROM ayat ORDER BY id"
    ).fetchall()

    flagged = []
    for row in rows:
        arabic_count = count_arabic_words(row["arabic"] or "")
        gloss_list   = json.loads(row["gloss"]) if row["gloss"] else []
        gloss_count  = len(gloss_list)

        if arabic_count > 0 and gloss_count < arabic_count * args.threshold:
            flagged.append({
                "key":           row["ayah_key"],
                "arabic_words":  arabic_count,
                "gloss_items":   gloss_count,
                "current_gloss": gloss_list[:3],
            })

    print(f"\n{DIVIDER}")
    print(f"  FIX SHORT GLOSS — {'DRY RUN' if args.dry_run else 'WRITE MODE'}")
    print(f"  Threshold: gloss < {args.threshold * 100:.0f}% of Arabic word count")
    print(DIVIDER)
    print(f"\n  Flagged: {len(flagged)} ayat with suspiciously short gloss\n")

    for item in flagged[:10]:
        print(f"  {item['key']}: {item['gloss_items']} gloss items, "
              f"{item['arabic_words']} arabic words  "
              f"→ {item['current_gloss']}")

    if len(flagged) > 10:
        print(f"  ... and {len(flagged) - 10} more")

    if args.dry_run:
        print(f"\n[DRY RUN] Would re-fetch {len(flagged)} ayat")
        return

    print(f"\nRe-fetching {len(flagged)} ayat...\n")
    fixed = 0
    for i, item in enumerate(flagged, 1):
        key = item["key"]
        new_gloss = fetch_gloss(key)

        if len(new_gloss) > item["gloss_items"]:
            cur.execute(
                "UPDATE ayat SET gloss=? WHERE ayah_key=?",
                (json.dumps(new_gloss, ensure_ascii=False), key)
            )
            fixed += 1
            print(f"  ✓ {key}: {item['gloss_items']} → {len(new_gloss)} items")
        else:
            print(f"  ~ {key}: no improvement ({len(new_gloss)} items)")

        if i % 50 == 0:
            conn.commit()
            print(f"    [{i}/{len(flagged)}] committed")
        time.sleep(0.3)

    conn.commit()
    conn.close()
    print(f"\n{DIVIDER}")
    print(f"  DONE — {fixed}/{len(flagged)} ayat improved")
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()