# src/auditor.py
# ─────────────────────────────────────────────────────────────────────────────
# Quranic Cross-Lingual Translation Auditor — Divergence Engine
# Now supports 5 translations: C(5,2) = 10 pairwise scores
#
# Algorithm: Pairwise Macro-Averaged Jaccard Divergence Friction Score
#   1. Clean + tokenise each translation into a content-word set
#   2. Compute Jaccard similarity across all C(5,2)=10 unique pairs
#   3. Macro-average the 10 scores → macro_similarity
#   4. Divergence Friction Score = 1.0 − macro_similarity
# ─────────────────────────────────────────────────────────────────────────────

import string
from itertools import combinations

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "will", "would", "shall", "should", "may", "might", "must", "can",
    "could", "of", "in", "on", "at", "to", "for", "with", "by", "from",
    "up", "about", "into", "through", "during", "before", "after",
    "above", "below", "between", "out", "off", "over", "under", "then",
    "that", "this", "these", "those", "it", "its", "he", "she", "they",
    "we", "you", "i", "him", "her", "them", "us", "his", "their", "our",
    "your", "my", "no", "not", "so", "if", "as", "all", "each", "every",
    "both", "few", "more", "most", "other", "some", "such", "than",
    "too", "very", "just", "there", "here", "when", "where", "who",
    "which", "what", "how", "one", "two", "s", "t", "say", "said",
}

TRANSLATOR_KEYS = ["sahih", "haleem", "khattab", "soliman", "kanzuliman"]
TRANSLATOR_LABELS = {
    "sahih":      "Sahih International",
    "haleem":     "Abdel Haleem",
    "khattab":    "Mustafa Khattab",
    "soliman":    "Fadel Soliman / Bridges",
    "kanzuliman": "Kanzul Iman (Aqib Farid Qadri)",
}


def clean_text(text: str) -> set:
    extra = "\u2014\u2013\u2018\u2019\u201c\u201d\u060c\u061b\u061f\u02be\u02bf"
    translator = str.maketrans("", "", string.punctuation + extra)
    cleaned = text.translate(translator).lower()
    return {w for w in cleaned.split() if w not in STOP_WORDS and len(w) > 1}


def jaccard_similarity(set_a: set, set_b: set) -> float:
    if not set_a and not set_b:
        return 1.0
    union = set_a | set_b
    return len(set_a & set_b) / len(union) if union else 0.0


def compute_divergence(trans_sahih: str, trans_haleem: str,
                       trans_khattab: str, trans_soliman: str,
                       trans_kanzuliman: str = "") -> dict:
    """
    Run the full divergence audit for one Ayah across 5 translations.
    C(5,2) = 10 pairwise Jaccard scores macro-averaged.
    trans_kanzuliman defaults to "" for backward compatibility with
    Ayat not yet covered by Kanzul Iman.
    """
    texts = {
        "sahih":      trans_sahih,
        "haleem":     trans_haleem,
        "khattab":    trans_khattab,
        "soliman":    trans_soliman,
        "kanzuliman": trans_kanzuliman,
    }

    # Only include translators that have non-empty text
    active_keys = [k for k in TRANSLATOR_KEYS if texts[k].strip()]
    word_sets   = {k: clean_text(texts[k]) for k in active_keys}

    pair_scores = []
    pairs_log   = []

    for t1, t2 in combinations(active_keys, 2):
        sim = jaccard_similarity(word_sets[t1], word_sets[t2])
        pair_scores.append(sim)
        pairs_log.append({
            "pair":         f"{t1} vs {t2}",
            "label":        f"{TRANSLATOR_LABELS[t1]} vs {TRANSLATOR_LABELS[t2]}",
            "sim":          round(sim, 4),
            "shared":       sorted(word_sets[t1] & word_sets[t2]),
            "exclusive_t1": sorted(word_sets[t1] - word_sets[t2]),
            "exclusive_t2": sorted(word_sets[t2] - word_sets[t1]),
        })

    macro_sim = sum(pair_scores) / len(pair_scores) if pair_scores else 0.0
    friction  = round(1.0 - macro_sim, 4)

    if friction < 0.25:
        band, band_label = "low",    "Tight Consensus"
    elif friction < 0.55:
        band, band_label = "medium", "Moderate Divergence"
    else:
        band, band_label = "high",   "High Semantic Divergence"

    return {
        "friction_score": friction,
        "band":           band,
        "band_label":     band_label,
        "word_sets":      {k: sorted(word_sets.get(k, set())) for k in TRANSLATOR_KEYS},
        "pairs_log":      pairs_log,
    }
