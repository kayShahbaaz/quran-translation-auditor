#!/usr/bin/env python3
"""
scripts/fix_gloss_1_7.py
─────────────────────────
Seeds the missing word-by-word gloss for Ayah 1:7 directly from the
Quranic Arabic Corpus (quran.com word-by-word data).

Ayah 1:7 — غَيْرِ الْمَغْضُوبِ عَلَيْهِمْ وَلَا الضَّالِّينَ
Word-by-word gloss (6 words):
  غَيْرِ         → "not"
  الْمَغْضُوبِ   → "those who earned (Your) wrath"
  عَلَيْهِمْ     → "on them"
  وَلَا          → "and not"
  الضَّالِّينَ   → "those who go astray"

Note: quran.com treats عَلَيْهِمْ as attached to الْمَغْضُوبِ in some
corpus versions and as a separate token in others. We use the 5-token
split that matches the fetch_gloss.py format used for other ayat.

Run from project root:
    python scripts/fix_gloss_1_7.py
"""
import sqlite3, json, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

GLOSS_1_7 = [
    "not",
    "those who earned (Your) wrath",
    "on them",
    "and not",
    "those who go astray",
]


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # Verify current state
    row = cur.execute(
        "SELECT ayah_key, gloss FROM ayat WHERE ayah_key='1:7'"
    ).fetchone()

    if not row:
        print("[ERROR] Ayah 1:7 not found in DB.")
        conn.close()
        sys.exit(1)

    current = json.loads(row[1]) if row[1] else []
    print(f"Current gloss for 1:7: {current}")

    if current:
        print("[WARN] Gloss already populated — overwriting with corpus data.")

    gloss_json = json.dumps(GLOSS_1_7, ensure_ascii=False)
    cur.execute(
        "UPDATE ayat SET gloss=? WHERE ayah_key='1:7'",
        (gloss_json,)
    )
    conn.commit()

    # Verify
    saved = json.loads(
        cur.execute("SELECT gloss FROM ayat WHERE ayah_key='1:7'").fetchone()[0]
    )
    conn.close()

    print(f"Seeded gloss for 1:7: {saved}")

    # Quick Jaccard preview using the same logic as fidelity_engine
    import string, unicodedata, re

    STOP = {
        "the","a","an","and","or","but","is","are","was","were","be","been",
        "being","have","has","had","do","does","did","will","would","should",
        "may","might","must","can","could","of","in","on","at","to","for",
        "with","by","from","up","about","into","it","its","he","she","they",
        "we","i","him","her","them","us","his","their","our","your","my",
        "so","if","as","both","few","more","most","other","some","such",
        "than","too","very","just","when","where","how","one","two","s","t",
    }
    SYNONYMS = {
        "earned": "anger", "wrath": "anger", "anger": "anger",
        "displeased": "anger", "incurred": "anger", "furious": "anger",
        "astray": "astray", "stray": "astray", "strayed": "astray",
        "gone": "astray", "lost": "astray", "go": "astray",
        "not": "not", "nor": "not", "neither": "not", "no": "not",
        "those": "those", "who": "those", "whom": "those",
    }

    def tokenise(text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        words = set()
        for w in text.split():
            w = re.sub(r'\d+$', '', w)
            if not w or w in STOP or len(w) < 2:
                continue
            words.add(SYNONYMS.get(w, w))
        return words

    gloss_words = tokenise(" ".join(GLOSS_1_7))
    sahih = "not of those who have earned [Your] anger or of those who are astray."
    sahih_words = tokenise(sahih)
    inter = gloss_words & sahih_words
    union = gloss_words | sahih_words
    score = len(inter) / len(union) if union else 0
    print(f"\nPreview Jaccard for Sahih 1:7:")
    print(f"  gloss_words : {sorted(gloss_words)}")
    print(f"  sahih_words : {sorted(sahih_words)}")
    print(f"  matched     : {sorted(inter)}")
    print(f"  score       : {score:.4f}")
    print(f"\nDone.")


if __name__ == "__main__":
    main()