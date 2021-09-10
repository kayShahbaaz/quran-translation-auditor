#!/usr/bin/env python3
"""
scripts/fetch_roots_all.py
───────────────────────────
Populates the `roots` column for all 6,236 ayat using
mustafa0x/quran-morphology — single file download, no API rate limits.

File format (4 tab-separated columns):
    surah:ayah:word:segment  arabic_text  POS  morph_tags
    e.g. 112:1:1:1  قُلْ  V  IMPV|VF:1|ROOT:قول|LEM:قالَ|2MS

Key facts (verified):
    - Surah 1:1 in file = Bismillah → skip; 1:N → our 1:(N-1)
    - All other surahs: file coordinates = our DB coordinates
    - ROOT is always in column 4 (index 3), format ROOT:xyz
    - ~50,000 of 130,000 lines have ROOT tags (rest are particles/prefixes)

Run:
    python scripts/fetch_roots_all.py --surah 112 --dry-run
    python scripts/fetch_roots_all.py --surah 112
    python scripts/fetch_roots_all.py           # full Quran (~30 seconds)
    python scripts/fetch_roots_all.py --resume  # skip already-populated
"""

import sys, os, json, sqlite3, re, argparse, urllib.request
from pathlib import Path
from collections import defaultdict

ROOT     = Path(__file__).parent.parent
DB_PATH  = ROOT / "data" / "auditor.db"
MORPH_URL = "https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt"
DIVIDER  = "─" * 60


def download_morphology():
    print("Downloading quran-morphology.txt (~3MB)...")
    req = urllib.request.Request(MORPH_URL, headers={"User-Agent": "QuranAuditor/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode("utf-8")
    lines = text.splitlines()
    print(f"  {len(lines):,} lines downloaded")
    return lines


def parse_morphology(lines):
    """
    Build {ayah_key: {arabic_word: root}} from morphology file.

    File has 4 tab-separated columns:
        col 0: surah:ayah:word:segment  (coordinate)
        col 1: arabic text of this segment
        col 2: POS type (V/N/P) — ignored
        col 3: morph tags — ROOT:xyz is here

    Per word: first segment that has a ROOT wins.
    Surah 1 only: file 1:1 = Bismillah (skip); file 1:N → our 1:(N-1).
    All other surahs: file coords = our DB coords.
    """
    word_roots = defaultdict(dict)   # {(surah, ayah): {word_pos: root}}
    word_texts = {}                  # {(surah, ayah, word_pos): arabic_text}

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) < 4:
            continue

        coord   = parts[0]
        ar_text = parts[1]
        morph   = parts[3]   # ROOT is in column 4 (index 3)

        coord_parts = coord.split(":")
        if len(coord_parts) != 4:
            continue

        try:
            surah = int(coord_parts[0])
            ayah  = int(coord_parts[1])
            word  = int(coord_parts[2])
        except ValueError:
            continue

        # Extract ROOT from morph tags
        root_match = re.search(r'ROOT:([^\|]+)', morph)
        if not root_match:
            continue
        root = root_match.group(1).strip()

        # Surah 1 offset: file 1:1 = Bismillah → skip; 1:N → our 1:(N-1)
        if surah == 1:
            if ayah == 1:
                continue
            ayah -= 1

        # First ROOT per word position wins
        key = (surah, ayah)
        if word not in word_roots[key]:
            word_roots[key][word] = root
            word_texts[(surah, ayah, word)] = ar_text

    # Build final dict
    result = {}
    for (surah, ayah), words in word_roots.items():
        ayah_key = f"{surah}:{ayah}"
        roots_dict = {
            word_texts[(surah, ayah, w)]: r
            for w, r in words.items()
            if word_texts.get((surah, ayah, w))
        }
        if roots_dict:
            result[ayah_key] = roots_dict

    print(f"  Parsed roots for {len(result):,} ayat")
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Show without writing")
    parser.add_argument("--surah",   type=int,  default=None, help="Single surah only")
    parser.add_argument("--resume",  action="store_true", help="Skip already-populated")
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    print(f"\n{DIVIDER}")
    print(f"  FETCH ROOTS — {'DRY RUN' if args.dry_run else 'WRITE MODE'}")
    print(DIVIDER)

    lines     = download_morphology()
    all_roots = parse_morphology(lines)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    if args.surah:
        rows = cur.execute(
            "SELECT ayah_key, roots FROM ayat WHERE ayah_key LIKE ? ORDER BY id",
            (f"{args.surah}:%",)
        ).fetchall()
    else:
        rows = cur.execute(
            "SELECT ayah_key, roots FROM ayat ORDER BY id"
        ).fetchall()

    written  = 0
    skipped  = 0
    no_roots = 0

    for row in rows:
        ayah_key = row["ayah_key"]

        if args.resume:
            current = json.loads(row["roots"]) if row["roots"] else {}
            if current:
                skipped += 1
                continue

        roots_dict = all_roots.get(ayah_key, {})

        if not roots_dict:
            no_roots += 1
            if args.dry_run:
                print(f"  {ayah_key}: no roots")
            continue

        roots_json = json.dumps(roots_dict, ensure_ascii=False)

        if args.dry_run:
            print(f"  {ayah_key}: {len(roots_dict)} roots → {roots_json[:120]}")
        else:
            cur.execute(
                "UPDATE ayat SET roots=? WHERE ayah_key=?",
                (roots_json, ayah_key)
            )
            written += 1

    if not args.dry_run:
        conn.commit()

    conn.close()

    print(f"\n{DIVIDER}")
    print(f"  DONE")
    print(f"  Written  : {written:,}")
    print(f"  Skipped  : {skipped:,}  (already had roots)")
    print(f"  No roots : {no_roots:,}  (particles / muqatta'at)")
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()