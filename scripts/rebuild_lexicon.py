#!/usr/bin/env python3
"""
scripts/rebuild_lexicon.py
───────────────────────────
Rebuilds the auto-generated lexicon entries with cleaner semantic fields.

Problems with the initial expand_lexicon.py output:
  - High-frequency Quranic words (allah, indeed, lord, say, believe) appear
    in nearly every ayah so they pollute every root's semantic field
  - Stopwords weren't filtered before counting
  - Words that appear in >30% of all ayat are not root-specific

Fix:
  - Apply the same stopword + synonym filter from fidelity_engine.py
  - Filter out words that appear in more than MAX_AYAH_FREQ fraction of ayat
    (these are "Quran-wide" words, not root-specific)
  - Keep only words that are genuinely distinctive to that root's contexts

Run:
    python scripts/rebuild_lexicon.py --dry-run --show 20
    python scripts/rebuild_lexicon.py
"""

import sys, os, json, sqlite3, re, unicodedata, argparse
from pathlib import Path
from collections import Counter

ROOT     = Path(__file__).parent.parent
DB_PATH  = ROOT / "data" / "auditor.db"
LEX_PATH = ROOT / "src" / "root_lexicon.py"

sys.path.insert(0, str(ROOT / "src"))

DIVIDER = "─" * 60

# Words too common across Quran to be root-specific
# (appear in >25% of all ayat gloss data)
QURAN_COMMON = {
    "allah", "lord", "indeed", "say", "said", "verily", "surely",
    "believe", "believers", "disbelievers", "people", "among", "upon",
    "before", "day", "except", "most", "any", "see", "know", "come",
    "near", "certainly", "between", "given", "world", "whoever",
    "messenger", "those", "who", "whom", "that", "which",
    "well", "acquainted", "aware", "things", "thing", "made",
    "sent", "signs", "book", "whoever", "men", "women", "life",
    "take", "give", "think", "one", "two", "three", "good", "bad",
    "great", "own", "shall", "will", "let", "set", "put", "get",
    "go", "going", "gone", "came", "come", "coming",
}

# Standard English stopwords
STOP = {
    "the","a","an","and","or","but","is","are","was","were","be","been",
    "have","has","had","of","in","on","at","to","for","with","by","from",
    "it","its","he","she","they","we","you","i","him","her","them","us",
    "this","that","these","those","not","no","so","if","as","all","each",
    "every","some","such","when","where","how","then","will","would",
    "shall","should","may","might","must","can","could","do","does","did",
    "his","their","our","your","my","its","s","t","than","too","very",
    "just","also","only","still","both","few","more","most","other",
    "same","there","here","now",
}

ALL_FILTER = STOP | QURAN_COMMON


def to_hyphenated(root):
    root = root.strip()
    if '-' in root:
        return root
    chars = [c for c in root if not unicodedata.category(c).startswith('M')]
    return '-'.join(chars) if len(chars) >= 2 else root


def root_to_latin(root_hyphenated):
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
        lat = ''.join(MAP.get(c, c) for c in p
                      if not unicodedata.category(c).startswith('M'))
        latin_parts.append(lat)
    return '-'.join(latin_parts)


def clean_gloss(gloss_list):
    """Extract content words from gloss, applying all filters."""
    words = []
    for item in gloss_list:
        # Remove bracketed qualifiers like (be), (the), (of)
        text = re.sub(r'\(.*?\)', '', str(item))
        text = re.sub(r'[^\w\s]', ' ', text).lower()
        for w in text.split():
            if (w not in ALL_FILTER
                    and len(w) > 2
                    and w.isalpha()
                    and not w.isdigit()):
                words.append(w)
    return words


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run",  action="store_true")
    parser.add_argument("--show",     type=int, default=10,
                        help="Number of entries to preview in dry-run")
    parser.add_argument("--min-freq", type=int, default=2,
                        help="Min occurrences for a word to be in core (default 2)")
    args = parser.parse_args()

    print(f"\n{DIVIDER}")
    print(f"  REBUILD LEXICON — {'DRY RUN' if args.dry_run else 'WRITE MODE'}")
    print(DIVIDER)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    print("\nLoading all ayat roots and gloss data...")
    rows = cur.execute(
        "SELECT ayah_key, roots, gloss FROM ayat "
        "WHERE roots != '{}' AND roots IS NOT NULL AND gloss IS NOT NULL"
    ).fetchall()
    print(f"  {len(rows):,} ayat loaded")

    # Load current lexicon
    from root_lexicon import ROOT_LEXICON

    # Identify hand-curated vs auto-generated entries by reading the file
    # The auto-generated section starts after the MARKER comment
    MARKER = "# ── Auto-generated entries (expand_lexicon.py)"
    with open(LEX_PATH, 'r', encoding='utf-8') as _f:
        _lex_text = _f.read()

    if MARKER in _lex_text:
        # Parse only the keys defined BEFORE the marker (hand-curated)
        _before = _lex_text[:_lex_text.index(MARKER)]
        import re as _re
        # Extract keys defined before the marker using a simple pattern
        # extract keys before marker
        hand_curated = set()
        for _l in _before.split('\n'):
            _l = _l.strip()
            if _l.startswith('ROOT_LEXICON[') and '] =' in _l:
                _k = _l.split('[')[1].split(']')[0].strip("'\"")
                if _k:
                    hand_curated.add(_k)
        print(f"  Hand-curated entries (before marker): {len(hand_curated)}")
    else:
        # No marker found — treat ALL current entries as hand-curated
        # This means expand_lexicon.py hasn't been run yet
        hand_curated = set(ROOT_LEXICON.keys())
        print(f"  No auto-section marker found — all {len(hand_curated)} entries treated as hand-curated")

    # Step 1: build root → list of gloss word lists
    print("\nBuilding root → gloss word index...")
    root_word_counts  = {}   # {root: Counter}
    root_ayah_count   = {}   # {root: number of ayat it appears in}
    root_examples     = {}

    for row in rows:
        roots_dict = json.loads(row["roots"])
        gloss_list = json.loads(row["gloss"]) if row["gloss"] else []
        words      = clean_gloss(gloss_list)

        for _arabic, root in roots_dict.items():
            h = to_hyphenated(root)
            if h in hand_curated:
                continue  # don't touch hand-curated entries

            if h not in root_word_counts:
                root_word_counts[h] = Counter()
                root_ayah_count[h]  = 0
                root_examples[h]    = row["ayah_key"]

            root_word_counts[h].update(words)
            root_ayah_count[h] += 1

    total_ayat = len(rows)
    print(f"  {len(root_word_counts):,} auto-generated roots to rebuild")

    # Step 2: build clean entries
    # A word is "distinctive" if it appears in < MAX_DOC_FREQ fraction of
    # the ayat where this root occurs (avoids generic words that co-occur
    # with everything)
    MAX_DOC_FREQ = 0.7   # word must not appear in >70% of root's contexts

    new_entries = {}
    for root, counter in root_word_counts.items():
        ayah_n = root_ayah_count[root]

        # Get words with their raw count
        candidates = []
        for word, count in counter.most_common(60):
            # Skip if too generic within this root's own contexts
            doc_freq = count / ayah_n if ayah_n > 0 else 0
            if doc_freq > MAX_DOC_FREQ:
                continue
            if count < args.min_freq and ayah_n > 3:
                continue
            candidates.append(word)
            if len(candidates) >= 20:
                break

        core     = candidates[:8]
        extended = candidates[8:16]

        # Fallback: if we filtered too aggressively, use top words anyway
        if not core and counter:
            core = [w for w, _ in counter.most_common(4)
                    if w not in STOP]

        new_entries[root] = {
            "latin":    root_to_latin(root),
            "category": "Quranic",
            "core":     core,
            "extended": extended,
            "avoid":    [],
            "example":  root_examples.get(root, ""),
            "ayah_n":   ayah_n,
        }

    conn.close()

    # Preview
    if args.dry_run:
        print(f"\nPreview of first {args.show} rebuilt entries:\n")
        count = 0
        for root, entry in sorted(new_entries.items()):
            if count >= args.show:
                break
            print(f"  {root} ({entry['latin']}) — {entry['ayah_n']} ayat")
            print(f"    core:     {entry['core']}")
            print(f"    extended: {entry['extended']}")
            print(f"    example:  {entry['example']}")
            count += 1
        print(f"\n[DRY RUN] Would rebuild {len(new_entries)} auto entries in {LEX_PATH.name}")
        print("Run without --dry-run to apply.")
        return

    # Write: replace auto-generated section in root_lexicon.py
    print(f"\nReading {LEX_PATH.name}...")
    with open(LEX_PATH, 'r', encoding='utf-8') as f:
        original = f.read()

    # Find the auto-generated section marker and truncate there
    MARKER = "# ── Auto-generated entries (expand_lexicon.py)"
    if MARKER in original:
        original = original[:original.index(MARKER)]
        print(f"  Removed previous auto-generated section")
    else:
        print(f"  No previous auto section found — appending")

    # Write rebuilt entries
    print(f"  Writing {len(new_entries)} rebuilt entries...")
    with open(LEX_PATH, 'w', encoding='utf-8') as f:
        f.write(original.rstrip() + "\n\n\n")
        f.write(f"# ── Auto-generated entries (expand_lexicon.py) ──────────────────────────────\n")
        f.write(f"# Rebuilt by rebuild_lexicon.py — data-driven from quran.com gloss.\n")
        f.write(f"# Core/extended = most distinctive gloss words per root (filtered for Quran-common words).\n")
        f.write(f"# Hand-curated entries above are preserved unchanged.\n\n")

        for root, entry in sorted(new_entries.items()):
            f.write(f"ROOT_LEXICON[{repr(root)}] = {{\n")
            f.write(f"    \"latin\":    {repr(entry['latin'])},\n")
            f.write(f"    \"category\": \"Quranic\",\n")
            f.write(f"    \"core\":     {json.dumps(entry['core'], ensure_ascii=False)},\n")
            f.write(f"    \"extended\": {json.dumps(entry['extended'], ensure_ascii=False)},\n")
            f.write(f"    \"avoid\":    [],\n")
            f.write(f"}}\n")

    # Verify
    import importlib, root_lexicon as rl
    importlib.reload(rl)
    print(f"\n{DIVIDER}")
    print(f"  DONE")
    print(f"  Hand-curated entries : {len(hand_curated)}")
    print(f"  Auto entries rebuilt : {len(new_entries)}")
    print(f"  Total lexicon size   : {len(hand_curated) + len(new_entries)}")
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()