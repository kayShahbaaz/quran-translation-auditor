#!/usr/bin/env python3
"""
scripts/fix_sahih_encoding.py
─────────────────────────────
Fixes two classes of corruption in fetched translation text:

  CLASS A — Unicode transliteration chars (allāh → Allah, lām → lam, mīm → mim)
             These crept in from the source HTML before encoding was normalised.

  CLASS B — Footnote/superscript digits scraped without their HTML tags:
             "Recompense.1"     → "Recompense."      (trailing after punctuation)
             "Allah1 -"         → "Allah -"           (trailing before space/dash)
             "signs1of"         → "signs of"          (no-space join artifact)
             "formed 1\\n"      → "formed"            (trailing at end of string)

Run from the project root:
    python scripts/fix_sahih_encoding.py           # dry run (safe)
    python scripts/fix_sahih_encoding.py --write   # apply fixes
"""
import sys, re, sqlite3, unicodedata
from pathlib import Path

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"
WRITE   = "--write" in sys.argv
DIVIDER = "─" * 60

# ── Unicode transliteration map ──────────────────────────────────────────────
_UNICODE_MAP = str.maketrans({
    "ā": "a", "Ā": "A",
    "ī": "i", "Ī": "I",
    "ū": "u", "Ū": "U",
    "ṭ": "t", "Ṭ": "T",
    "ḥ": "h", "Ḥ": "H",
    "ḍ": "d", "Ḍ": "D",
    "ẓ": "z", "Ẓ": "Z",
    "ṣ": "s", "Ṣ": "S",
    "ʿ": "",  "ʾ": "",
    "\u02be": "", "\u02bf": "",
})

# ── Footnote digit patterns ──────────────────────────────────────────────────
# Applied in order — each targets a specific scrape artifact.
_FOOTNOTE_PATTERNS = [
    # "signs1of"  →  "signs of"   (word-digit-word, no spaces — join artifact)
    (re.compile(r'([a-zA-Z])\d+([a-zA-Z])'), r'\1 \2'),

    # "Allāh1 "   →  "Allah "     (digit directly after a word char, before space/punct/end)
    (re.compile(r'([a-zA-Z])\d+(\s|[.!?,;:\-–—]|$)'), r'\1\2'),

    # " 1\n" / " 1$"  →  ""       (isolated trailing footnote number)
    (re.compile(r'\s+\d+\s*$'), ''),
]


def fix_text(text: str) -> str:
    if not text:
        return text

    # 1. Unicode transliteration chars → plain ASCII
    text = text.translate(_UNICODE_MAP)

    # 2. Footnote digit cleanup (order matters)
    for pattern, replacement in _FOOTNOTE_PATTERNS:
        text = pattern.sub(replacement, text)

    # 3. Collapse any double-spaces created by fixes
    text = re.sub(r'  +', ' ', text).strip()

    # 4. NFC normalise
    text = unicodedata.normalize("NFC", text)

    return text


# ── Detection query — catches both corruption classes ────────────────────────
_DETECT_SQL = """
    SELECT id, ayah_key, {col}
    FROM ayat
    WHERE {col} LIKE '%ā%'
       OR {col} LIKE '%ī%'
       OR {col} LIKE '%ū%'
       OR {col} LIKE '%ṭ%'
       OR {col} LIKE '%ḥ%'
       OR {col} LIKE '%ṣ%'
       OR {col} LIKE '%ʿ%'
       OR {col} LIKE '%ʾ%'
       OR {col} REGEXP '\w\d+(\w|\s|[[:punct:]]|$)'
"""

# SQLite doesn't have REGEXP by default — use Python-side filtering instead
_DETECT_SIMPLE_SQL = "SELECT id, ayah_key, {col} FROM ayat WHERE {col} IS NOT NULL"

_FOOTNOTE_RE = re.compile(r'[a-zA-Z]\d')  # quick pre-filter


def needs_fixing(text: str) -> bool:
    if not text:
        return False
    # Unicode chars
    for ch in "āĀīĪūŪṭṬḥḤḍḌẓẒṣṢʿʾ\u02be\u02bf":
        if ch in text:
            return True
    # Digit immediately after a letter
    if _FOOTNOTE_RE.search(text):
        return True
    return False


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    TRANS_COLS = [
        "trans_sahih", "trans_haleem", "trans_khattab",
        "trans_soliman", "trans_kanzuliman",
    ]

    print(f"\n{DIVIDER}")
    print(f"  FIX TRANSLATION ENCODING — {'DRY RUN' if not WRITE else 'WRITE MODE'}")
    print(DIVIDER)

    grand_total = 0

    for col in TRANS_COLS:
        all_rows = cur.execute(
            _DETECT_SIMPLE_SQL.format(col=col)
        ).fetchall()

        affected = [(r["id"], r["ayah_key"], r[col])
                    for r in all_rows if needs_fixing(r[col])]

        if not affected:
            print(f"\n  {col}: no issues found ✓")
            continue

        print(f"\n  {col}: {len(affected)} rows to fix (showing first 5):\n")
        for row_id, key, original in affected[:5]:
            fixed = fix_text(original)
            changed = original != fixed
            marker = "✓" if changed else "≈ (no visible change)"
            print(f"    [{key}] {marker}")
            # Show a 120-char window around the first difference
            for i, (a, b) in enumerate(zip(original, fixed)):
                if a != b:
                    start = max(0, i - 20)
                    print(f"      BEFORE: ...{original[start:start+80]}...")
                    print(f"      AFTER : ...{fixed[start:start+80]}...")
                    break
            else:
                if len(original) != len(fixed):
                    print(f"      BEFORE (tail): ...{original[-60:]}")
                    print(f"      AFTER  (tail): ...{fixed[-60:]}")

        grand_total += len(affected)

        if WRITE:
            fixed_count = 0
            for row_id, key, original in affected:
                fixed = fix_text(original)
                if fixed != original:
                    cur.execute(f"UPDATE ayat SET {col}=? WHERE id=?", (fixed, row_id))
                    fixed_count += 1
            print(f"\n    → {fixed_count} rows actually changed in {col}")

    print(f"\n{DIVIDER}")
    if not WRITE:
        print(f"  DRY RUN complete. {grand_total} total rows flagged.")
        print(f"  Inspect the BEFORE/AFTER diffs above, then run:")
        print(f"    python scripts/fix_sahih_encoding.py --write")
    else:
        conn.commit()
        print(f"  DONE. Committed all fixes.")
    conn.close()
    print(DIVIDER + "\n")


if __name__ == "__main__":
    main()