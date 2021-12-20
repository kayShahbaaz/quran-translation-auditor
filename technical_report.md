# Technical Report: Quranic Cross-Lingual Translation Auditor

**Version:** 1.0.0
**Project:** A LearnQuran Academy Project
**Architecture:** Python 3 / Flask / SQLite / Vanilla JS
**Algorithm Class:** Lexical Fidelity Scoring via Set-Theoretic Overlap + Root Semantic Field Matching

---

## Abstract

This report documents the design, algorithmic architecture, and implementation rationale of the **Quranic Cross-Lingual Translation Auditor** — a web application that quantitatively scores how faithfully five major English translations of the Quran preserve the meaning of the original Arabic at both the lexical and root-semantic level.

The system operates across all 6,236 Ayat of the Quran, scoring five translations — Sahih International, Abdel Haleem, Mustafa Khattab, Fadel Soliman/Bridges, and Ala Hazrat/Kanzul Iman — on two independent dimensions: **Literal Accuracy** (word-level fidelity to the official Quranic Arabic Corpus gloss) and **Semantic Depth** (coverage of each Arabic root's Hans Wehr semantic field). Full Root Breakdown, Linguistic Reasoning, and Translation Analysis are provided for Surah Al-Fatiha, with the architecture designed for incremental extension to all 114 Surahs.

The system deliberately avoids transformer-based embeddings or neural NLP dependencies, preserving full interpretability, deployment simplicity, and academic reproducibility.

---

## 1. Problem Statement

### 1.1 The Translation Fidelity Challenge

The Quran presents a uniquely demanding case for cross-lingual semantic auditing. Each Ayah carries layered meaning across morphological, syntactic, rhetorical, and theological dimensions. Five translators with distinct methodological commitments produce substantially different English texts from the same Arabic source — and these differences are not errors. They are epistemically meaningful signals that reveal where the Arabic resists single-mapping into English.

Consider **الرَّحْمَٰنِ (Ar-Rahman)** from Al-Fatiha 1:2:

| Translator | Rendering | Philosophy |
|---|---|---|
| Sahih International | The Entirely Merciful | Morphological precision |
| Abdel Haleem | The Lord of Mercy | Relational, pragmatic |
| Mustafa Khattab | The Most Compassionate | Contemporary resonance |
| Fadel Soliman | The All-Merciful | Intensity suffix preserved |
| Ala Hazrat | The Most Gracious | Classical Barelvi tradition |

Each choice is coherent within its school. But measuring the divergence between them — and tracing it to specific root choices — is precisely what this system is built to do.

### 1.2 Gap This System Addresses

Existing Quranic translation tools are either static side-by-side displays with no quantitative analysis, or neural embedding systems requiring GPU infrastructure. This system fills the gap: a quantitative fidelity engine that is algorithmically rigorous, computationally minimal, and fully interpretable without machine learning expertise.

### 1.3 Scope

- **6,236 Ayat** — full Quranic coverage
- **5 translations** — representing literal, literary, contemporary, bridge, and classical Barelvi schools
- **2 scoring dimensions** — Literal Accuracy and Semantic Depth
- **Full analysis** for Al-Fatiha (1:1–1:7); Semantic Depth planned for all Surahs in future versions
- **Zero neural dependencies** — pure Python NLP pipeline

---

## 2. System Architecture

### 2.1 Data Layer

A single SQLite database (`auditor.db`, ~11MB) stores all data:

```
ayat table (6,236 rows)
├── id, ayah_key, surah_name
├── arabic              — Uthmani script (quran.com text_uthmani)
├── roots               — JSON: {arabic_word: trilateral_root}
├── gloss               — JSON: [word-by-word English gloss items]
├── trans_sahih         — Sahih International
├── trans_haleem        — Abdel Haleem
├── trans_khattab       — Mustafa Khattab
├── trans_soliman       — Fadel Soliman / Bridges
├── trans_kanzuliman    — Ala Hazrat / Kanzul Iman
├── reasoning           — Linguistic reasoning text (Al-Fatiha)
├── depth_commentary    — Translation analysis prose (Al-Fatiha)
└── surah_intro         — Surah introduction (Al-Fatiha)

surah_scores table (114 rows)
└── Pre-computed average Literal Accuracy per translator per Surah
```

### 2.2 Scoring Engine

`src/fidelity_engine.py` implements both scoring layers. Scores are computed at request time from the DB data, with no pre-stored per-Ayah scores — keeping the DB lean and allowing the scoring logic to be updated without DB migrations.

### 2.3 Flask Application

`run.py` serves two routes:
- `/` — Ayah dashboard with pagination and Surah filter
- `/surahs` — Surah summary table (reads from pre-computed `surah_scores`)

---

## 3. Data Pipeline

### 3.1 Sources

| Data | Source | Method |
|---|---|---|
| Arabic text + gloss | quran.com API | `scripts/fetch_gloss.py` |
| Translations (4) | quran.com API | `scripts/fetch_full_quran.py` |
| Kanzul Iman | barkati.net | `scripts/fetch_kanzuliman.py` (scraper) |
| Root morphology | mustafa0x/quran-morphology | `scripts/fetch_roots_all.py` |

### 3.2 Root Population

Root data was sourced from the **mustafa0x/quran-morphology** corpus — a 130,030-line tab-separated file of Quranic Arabic Corpus morphological annotations. Format:

```
surah:ayah:word:segment  arabic_text  POS  morph_tags
112:1:1:1  قُلْ  V  IMPV|VF:1|ROOT:قول|LEM:قالَ|2MS
```

The `ROOT:` field in column 4 gives the trilateral root directly. A custom parser extracts `{arabic_word: root}` for each Ayah, handling:
- Bismillah offset (surah 1 only — file's 1:1 = Bismillah, our 1:1 = Al-Hamd)
- Prefix stripping (morphology file stores stems; DB stores full prefixed words)
- Five-level fuzzy Arabic matching (diacritic normalisation → alef unification → prefix stripping → containment)

**Coverage:** 6,214 of 6,236 Ayat (99.6%). The 22 uncovered are muqatta'at letters (الم، يس، طه) which have no trilateral root by definition.

### 3.3 Data Cleaning

`scripts/fix_sahih_encoding.py` corrected encoding corruption across 4,309 rows:
- Unicode transliteration chars: `Allāh → Allah`, `Lām → Lam`
- Footnote superscripts: `Lord1 → Lord`, `signs1of → signs of`

---

## 4. Scoring Methodology

### 4.1 Layer 1 — Literal Accuracy

**What it measures:** How closely a translation's content words match the official word-by-word English gloss from the Quranic Arabic Corpus.

**Algorithm:**

```
score = |clean(translation) ∩ clean(gloss)| / |clean(translation) ∪ clean(gloss)|
```

This is Jaccard similarity between two content-word sets.

**The `clean_text()` pipeline:**

```
Input text
  → Unicode normalisation (allāh→allah, diacritics stripped)
  → Parenthetical removal: (be), (the), (of Allah) → ""
  → Word-separator punctuation → space
  → Lowercase + punctuation strip
  → Stopword removal (minimal list — preserves "not", "those", "who", "what")
  → Trailing digit removal (lord1 → lord)
  → Synonym canonicalisation + conservative stemming
  → Output: content word set
```

**Synonym normalisation** is the critical innovation. 30+ equivalence groups map legitimate translation variants to a canonical form before comparison, so Jaccard penalises genuine semantic divergence rather than surface vocabulary choice:

```python
("worlds", {"world", "worlds", "universe", "realm", "realms",
             "creation", "creatures", "beings", "existence"}),
("merciful", {"merciful", "mercy", "compassionate", "gracious",
              "beneficent", "forgiving", "pardoning"}),
("faith", {"faith", "belief", "believer", "pious", "devout",
           "mindful", "conscious", "righteous", "taqwa"}),
# ... 27 more groups
```

**Stemmer design:** Conservative suffix stripping (minimum 4-char stem) prevents over-stemming artifacts (`drowsiness→drowsi`, `anything→anyth`) that plagued earlier iterations. Known inflected forms are handled by the synonym map rather than the stemmer.

**Score range:** [0.0, 1.0]. Higher = closer to the official gloss vocabulary.

### 4.2 Layer 2 — Semantic Depth

**What it measures:** Whether a translation's vocabulary falls within the semantic field of each Arabic root in the Ayah — as defined by the Hans Wehr Arabic-English Dictionary.

**Algorithm:**

For each distinct root in the Ayah:

| Match type | Score |
|---|---|
| Translation word in root's **core** field | 1.0 |
| Translation word in root's **extended** field | 0.6 |
| Translation word is an **avoid** term | −0.3 |
| No match | 0.0 |

```
overall_score = mean(per_root_scores), clamped to [0.0, 1.0]
```

**Root lexicon:** `src/root_lexicon.py` contains 345 hand-curated entries covering the most frequent Quranic roots, verified against Lane's Lexicon and the Quranic Arabic Corpus. Example:

```python
"ح-م-د": {
    "latin": "h-m-d",
    "category": "Worship",
    "core": ["praise", "hamd", "commend", "laud", "extol",
             "thanksgiving", "gratitude", "glorify"],
    "extended": ["thank", "honor", "worship"],
    "avoid": ["glorify", "remember", "sanctify"]
},
```

**Current coverage:** Full Semantic Depth scoring for Al-Fatiha (1:1–1:7). The root data exists for 99.6% of the Quran; lexicon expansion for remaining Surahs is planned for v2.0.

---

## 5. Text Normalisation for Arabic

Matching morphology-file stem words against DB full-prefixed words required a five-level Arabic fuzzy matcher:

```python
def _match_root_to_db_word(morph_word, db_words):
    morph_norm  = _normalise_ar(morph_word)   # strip diacritics, unify alef variants
    morph_strip = _strip_ar_prefix(morph_norm) # remove ال، وال، فال، بال، كال

    for db_word in db_words:
        db_norm  = _normalise_ar(db_word)
        db_strip = _strip_ar_prefix(db_norm)

        if db_norm == morph_norm:        return db_word  # L1: exact normalised
        if db_strip == morph_strip:      return db_word  # L2: both prefix-stripped
        if db_strip == morph_norm:       return db_word  # L3: DB stem = morph word
        if db_norm == morph_strip:       return db_word  # L4: DB word = morph stem
        if morph_strip in db_norm:       return db_word  # L5: containment
    return None
```

Alef normalisation unifies `أ`, `إ`, `آ`, `ٱ` → `ا` before comparison, handling the common divergence between Uthmani script (`ٱلْحَمْدُ`) and standard Arabic (`الْحَمْدُ`).

---

## 6. Architectural Trade-offs

### 6.1 Why Not Transformer Embeddings?

| Concern | Detail |
|---|---|
| Interpretability | A cosine distance of 0.34 cannot be traced to specific words. A Jaccard score of 0.67 can be decomposed into exactly which words matched and which didn't — essential for a translation auditing tool |
| Deployment | Sentence-transformer models require 200MB–2GB downloads, optional GPU, 30–90s cold start |
| Reproducibility | Embedding models update silently; scores drift across versions |
| Scale appropriateness | Quranic translation strings are 5–30 words. Statistical NLP is appropriate at this scale |

### 6.2 Why SQLite?

Zero-config, single file, built into Python stdlib. Sufficient for 6,236 rows. `surah_scores` pre-computation table avoids rescoring all Ayat on every page load. PostgreSQL would add a running server process with no benefit at this scale.

### 6.3 Why Vanilla JS?

The collapsible panels, expand toggles, and translator tooltips are ~50 lines of vanilla JS. No build step, no npm, no bundler. Any Python developer can inspect, fork, and deploy without front-end toolchain knowledge.

---

## 7. Limitations

| Limitation | Detail |
|---|---|
| Semantic Depth coverage | Full scoring currently only for Al-Fatiha. Expanding requires hand-verifying ~1,400 additional lexicon entries |
| Gloss quality | quran.com gloss varies in verbosity — some Ayat have truncated gloss data affecting Literal Accuracy scores |
| Phrase-level units | Jaccard operates on unigrams. "Ever-Living" vs "Ever Living" may tokenise differently |
| Auto-generated lexicon | The 1,369 auto-generated root entries (from gloss co-occurrence) have lower semantic precision than the 345 hand-curated entries |
| No Arabic morphological analysis | Root assignment uses pre-computed corpus data rather than live Arabic NLP |

---

## 8. Future Work

| Feature | Approach |
|---|---|
| Full Semantic Depth coverage | Extend hand-curated lexicon to all ~1,700 Quranic roots |
| Linguistic Reasoning for all Surahs | Incremental batch workflow, surah by surah |
| CSV/JSON export | Flask `/export/<surah>` route |
| Ayah search | Client-side filter or SQLite FTS5 |
| Arabic NLP integration | CAMeL Tools for live morphological analysis |
| Tanzil alignment verification | Cross-check root assignments against Tanzil v1.1 |

---

## 9. Conclusion

The Quranic Cross-Lingual Translation Auditor demonstrates that meaningful, quantitative semantic fidelity analysis across five translations of the Quran does not require deep learning infrastructure. By grounding the engine in Jaccard set theory and Hans Wehr semantic field matching — both mathematically transparent, fully interpretable methods — the system produces scores directly traceable to specific vocabulary choices.

A researcher reading that Sahih International scores 0.83 Literal Accuracy on 1:1 can immediately see that "due" was the one extra word beyond the gloss — and understand exactly why. A researcher reading that Abdel Haleem scores 0.67 can see that "belongs" was the extra word, and that "God" was not penalised because it canonicalises to the same token as "Allah" via the synonym map.

This interpretability is not a compromise relative to neural approaches. For theologically dense texts like Quranic Ayat, where every word choice carries scholarly weight, being able to trace every score to specific words is a deliberate methodological advantage.

---

## Contact

📧 [Email](mailto:learnquran.iqra@gmail.com) ▶️ [YouTube](https://www.youtube.com/@LearnQuran_iqra)

---

*جزاك الله خيراً — May Allah reward you with good.*

---

**kayShahbaaz خ شهباز**