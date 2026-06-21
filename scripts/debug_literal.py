#!/usr/bin/env python3
"""
scripts/debug_literal.py
────────────────────────
Diagnoses why Literal Accuracy (gloss Jaccard) scores are wrong.

Shows exactly what is stored in the gloss column, how it parses,
and what the tokenizer produces for both gloss and each translation.

Run from the project root:
    python scripts/debug_literal.py
"""
import sys, os, json, sqlite3
from pathlib import Path

ROOT    = Path(__file__).parent.parent
DB_PATH = ROOT / "data" / "auditor.db"
sys.path.insert(0, str(ROOT / "src"))

from fidelity_engine import clean_text, jaccard

DIVIDER = "─" * 60

def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    row = cur.execute(
        "SELECT * FROM ayat WHERE ayah_key = '1:1'"
    ).fetchone()
    conn.close()

    if not row:
        print("[ERROR] Ayah 1:1 not found in DB.")
        sys.exit(1)

    print(f"\n{DIVIDER}")
    print("  AYAH 1:1 — LITERAL ACCURACY DEBUG")
    print(DIVIDER)

    # ── 1. Show raw gloss column ─────────────────────────────────────────────
    raw_gloss = row["gloss"]
    print(f"\n[1] RAW gloss column (first 300 chars):")
    print(f"    type  = {type(raw_gloss).__name__}")
    print(f"    value = {repr(raw_gloss[:300]) if raw_gloss else 'NULL / empty'}")

    # ── 2. Attempt to parse gloss ────────────────────────────────────────────
    print(f"\n[2] Parsing gloss:")
    gloss_list = []
    if not raw_gloss:
        print("    [!] gloss is NULL or empty → Jaccard will always be 0.0")
    else:
        try:
            parsed = json.loads(raw_gloss)
            print(f"    json.loads() → {type(parsed).__name__}")
            if isinstance(parsed, list):
                gloss_list = parsed
                print(f"    list length = {len(gloss_list)}")
                print(f"    first 5 items: {gloss_list[:5]}")
            elif isinstance(parsed, str):
                gloss_list = [parsed]
                print(f"    [!] Stored as JSON string, not list → treating as single gloss")
                print(f"    value: {parsed[:200]}")
            elif isinstance(parsed, dict):
                print(f"    [!] Stored as JSON dict — unexpected structure")
                print(f"    keys: {list(parsed.keys())[:10]}")
            else:
                print(f"    [!] Unexpected type after json.loads: {type(parsed)}")
        except (json.JSONDecodeError, TypeError) as e:
            print(f"    [!] json.loads() FAILED: {e}")
            print(f"    Treating as plain string")
            gloss_list = [raw_gloss]

    # ── 3. Tokenise gloss ────────────────────────────────────────────────────
    gloss_combined = " ".join(str(g) for g in gloss_list)
    gloss_words    = clean_text(gloss_combined)
    print(f"\n[3] Gloss word set after clean_text() ({len(gloss_words)} words):")
    print(f"    {sorted(gloss_words)}")

    # ── 4. Per-translator scores ─────────────────────────────────────────────
    trans_cols = {
        "sahih":      row["trans_sahih"],
        "haleem":     row["trans_haleem"],
        "khattab":    row["trans_khattab"],
        "soliman":    row["trans_soliman"],
        "kanzuliman": row["trans_kanzuliman"],
    }
    try:
        learnquran = row["trans_learnquran"]
    except IndexError:
        learnquran = None
    if learnquran:
        trans_cols["learnquran"] = learnquran

    print(f"\n[4] Per-translator Jaccard against gloss:\n")
    for name, text in trans_cols.items():
        if not text or not text.strip():
            print(f"    {name:<15} (no translation)")
            continue
        words     = clean_text(text)
        score     = jaccard(words, gloss_words)
        matched   = words & gloss_words
        missing   = gloss_words - words
        extra     = words - gloss_words
        print(f"    {name:<15} score={score:.4f}")
        print(f"      trans_words  ({len(words)}): {sorted(words)}")
        print(f"      matched      ({len(matched)}): {sorted(matched)}")
        print(f"      missing      ({len(missing)}): {sorted(missing)}")
        print(f"      extra        ({len(extra)}): {sorted(extra)}")
        print()

    # ── 5. Sanity check: expected score using hardcoded gloss ────────────────
    print(f"\n[5] Sanity check with HARDCODED gloss (same as fidelity_engine __main__):")
    hardcoded_gloss = ["all praise", "is", "to allah", "lord of", "the worlds"]
    hg_words = clean_text(" ".join(hardcoded_gloss))
    sahih_words = clean_text(row["trans_sahih"] or "")
    score_hardcoded = jaccard(sahih_words, hg_words)
    print(f"    hardcoded gloss words: {sorted(hg_words)}")
    print(f"    sahih words:           {sorted(sahih_words)}")
    print(f"    Jaccard (hardcoded):   {score_hardcoded:.4f}")
    print(f"\n    → If this is ~0.6–0.8 but [4] shows 0.0, the DB gloss format is the bug.")
    print(f"    → If both are 0.0, the tokeniser itself is stripping too many words.")
    print(f"\n{DIVIDER}\n")


if __name__ == "__main__":
    main()