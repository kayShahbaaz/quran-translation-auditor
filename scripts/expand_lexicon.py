#!/usr/bin/env python3
"""
scripts/expand_lexicon.py
──────────────────────────
Auto-generates root_lexicon entries for roots found in the DB
but not yet in root_lexicon.py.

Strategy:
  For each uncovered root, find all ayat that contain it,
  collect the English gloss words for those ayat positions,
  and use the most frequent content words as the 'core' semantic field.
  This gives a data-driven lexicon extension rather than manual entry.

Output: appends new entries to src/root_lexicon.py

Run from project root:
    python scripts/expand_lexicon.py --dry-run   # show what would be added
    python scripts/expand_lexicon.py             # write to root_lexicon.py
"""
import sys, os, json, sqlite3, re, unicodedata, argparse
from pathlib import Path
from collections import Counter

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"
LEX_PATH = ROOT / "src" / "root_lexicon.py"

sys.path.insert(0, str(ROOT / "src"))
from root_lexicon import ROOT_LEXICON

STOP = {
    "the","a","an","and","or","but","is","are","was","were","be","been",
    "have","has","had","of","in","on","at","to","for","with","by","from",
    "it","its","he","she","they","we","you","i","him","her","them","us",
    "this","that","these","those","not","no","so","if","as","all","each",
    "every","some","such","who","which","what","when","where","how","then",
    "will","would","shall","should","may","might","must","can","could",
    "do","does","did","one","two","s","t","his","their","our","your","my",
}

def to_hyphenated(root):
    root = root.strip()
    if '-' in root:
        return root
    chars = [c for c in root if not unicodedata.category(c).startswith('M')]
    return '-'.join(chars) if len(chars) >= 2 else root

def clean_gloss_words(gloss_list):
    words = set()
    for item in gloss_list:
        text = re.sub(r'\(.*?\)', '', str(item))  # remove bracketed text
        text = re.sub(r'[^\w\s]', ' ', text).lower()
        for w in text.split():
            if w not in STOP and len(w) > 2 and w.isalpha():
                words.add(w)
    return words

def root_to_latin(root_hyphenated):
    """Convert ح-م-د style root to latin transliteration."""
    MAP = {
        'ا':'a','أ':'a','إ':'a','آ':'a','ب':'b','ت':'t','ث':'th',
        'ج':'j','ح':'h','خ':'kh','د':'d','ذ':'dh','ر':'r','ز':'z',
        'س':'s','ش':'sh','ص':'s','ض':'d','ط':'t','ظ':'z','ع':'a',
        'غ':'gh','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n',
        'ه':'h','و':'w','ي':'y','ى':'a','ة':'h','ء':'\'','ئ':'y',
        'ؤ':'w','ٱ':'a',
    }
    parts = root_hyphenated.split('-')
    latin_parts = []
    for p in parts:
        lat = ''.join(MAP.get(c, c) for c in p if not unicodedata.category(c).startswith('M'))
        latin_parts.append(lat)
    return '-'.join(latin_parts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--min-freq", type=int, default=2,
                        help="Min frequency for a gloss word to be included (default 2)")
    parser.add_argument("--max-new", type=int, default=500,
                        help="Max new entries to add (default 500)")
    args = parser.parse_args()

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # Collect all roots in DB
    print("Scanning DB for all roots...")
    rows = cur.execute(
        "SELECT ayah_key, roots, gloss FROM ayat WHERE roots != '{}' AND roots IS NOT NULL"
    ).fetchall()

    # Build: hyphenated_root -> list of gloss word sets
    root_glosses = {}   # {root: Counter of gloss words}
    root_examples = {}  # {root: first ayah_key seen}

    for row in rows:
        roots_dict = json.loads(row["roots"])
        gloss_list = json.loads(row["gloss"]) if row["gloss"] else []
        gloss_words = clean_gloss_words(gloss_list)

        for _word, root in roots_dict.items():
            h = to_hyphenated(root)
            if h not in ROOT_LEXICON:
                if h not in root_glosses:
                    root_glosses[h] = Counter()
                    root_examples[h] = row["ayah_key"]
                root_glosses[h].update(gloss_words)

    conn.close()

    uncovered = len(root_glosses)
    print(f"Roots in DB not in lexicon: {uncovered}")
    print(f"Existing lexicon size: {len(ROOT_LEXICON)}")

    if uncovered == 0:
        print("Lexicon already covers all roots — nothing to do.")
        return

    # Generate entries
    new_entries = []
    for root, word_counter in sorted(root_glosses.items()):
        # Take top words by frequency as core field
        top = [w for w, count in word_counter.most_common(20) if count >= args.min_freq]
        core     = top[:8]   # top 8 as core
        extended = top[8:16] # next 8 as extended

        if not core:
            # Even if frequency too low, take top 4 for coverage
            core = [w for w, _ in word_counter.most_common(4)]

        latin = root_to_latin(root)
        entry = {
            "root":     root,
            "latin":    latin,
            "category": "Quranic",  # generic category for auto-generated
            "core":     core,
            "extended": extended,
            "avoid":    [],
        }
        new_entries.append(entry)

        if args.dry_run and len(new_entries) <= 20:
            print(f"\n  {root} ({latin})")
            print(f"    core:     {core}")
            print(f"    extended: {extended}")
            print(f"    example:  {root_examples[root]}")

        if len(new_entries) >= args.max_new:
            break

    if args.dry_run:
        print(f"\n[DRY RUN] Would add {len(new_entries)} new entries to root_lexicon.py")
        print("Run without --dry-run to apply.")
        return

    # Append to root_lexicon.py
    print(f"\nAppending {len(new_entries)} entries to {LEX_PATH}...")

    with open(LEX_PATH, 'a', encoding='utf-8') as f:
        f.write("\n\n# ── Auto-generated entries (expand_lexicon.py) ──────────────────────────────\n")
        f.write("# Generated from quran.com word-by-word gloss data.\n")
        f.write("# Core/extended fields are data-driven (most frequent gloss words per root).\n")
        f.write("# Review and refine manually for accuracy.\n\n")
        for e in new_entries:
            f.write(f"ROOT_LEXICON[{repr(e['root'])}] = {{\n")
            f.write(f"    \"latin\":    {repr(e['latin'])},\n")
            f.write(f"    \"category\": {repr(e['category'])},\n")
            f.write(f"    \"core\":     {json.dumps(e['core'], ensure_ascii=False)},\n")
            f.write(f"    \"extended\": {json.dumps(e['extended'], ensure_ascii=False)},\n")
            f.write(f"    \"avoid\":    [],\n")
            f.write(f"}}\n")

    print(f"Done. Lexicon expanded from {len(ROOT_LEXICON)} to {len(ROOT_LEXICON) + len(new_entries)} roots.")
    print("Restart the app to pick up the new entries.")


if __name__ == "__main__":
    main()