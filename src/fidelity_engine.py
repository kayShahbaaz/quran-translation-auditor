# src/fidelity_engine.py
# ─────────────────────────────────────────────────────────────────────────────
# Root Semantic Fidelity Engine (Layer 2)
# + Gloss Fidelity Engine (Layer 1)
# ─────────────────────────────────────────────────────────────────────────────

import sys, os, string, unicodedata, re

sys.path.insert(0, os.path.dirname(__file__))
from root_lexicon import get_core_field, get_semantic_field, get_avoid_terms, ROOT_LEXICON

# ── Stopwords ──────────────────────────────────────────────────────────────────
# Deliberately minimal — Quranic gloss uses many "function" words that carry
# meaning (not, those, who, what, all). Only remove truly meaningless particles.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "is", "are", "was", "were",
    "be", "been", "being", "have", "has", "had", "do", "does", "did",
    "will", "would", "shall", "should", "may", "might", "must", "can",
    "could", "of", "in", "on", "at", "to", "for", "with", "by", "from",
    "into", "through", "during", "before", "after", "above", "below",
    "between", "it", "its", "he", "she", "they", "we", "you", "i",
    "him", "her", "them", "us", "his", "their", "our", "your", "my",
    "if", "as", "than", "too", "very", "just", "s", "t",
    # NOTE: "not", "no", "those", "who", "what", "all", "every", "each",
    # "that", "this", "there" are deliberately NOT stopwords — they carry
    # meaning in Quranic gloss comparisons.
}

# ── Unicode normalisation ──────────────────────────────────────────────────────
_UNICODE_MAP = str.maketrans({
    "ā": "a", "Ā": "A", "ī": "i", "Ī": "I", "ū": "u", "Ū": "U",
    "ṭ": "t", "Ṭ": "T", "ḥ": "h", "Ḥ": "H", "ḍ": "d", "Ḍ": "D",
    "ẓ": "z", "Ẓ": "Z", "ṣ": "s", "Ṣ": "S", "ʿ": "", "ʾ": "",
    "\u02be": "", "\u02bf": "",
})


def _normalise_unicode(text: str) -> str:
    text = text.translate(_UNICODE_MAP)
    return unicodedata.normalize("NFC", text)


# ── Stemmer — conservative, only clear suffixes ───────────────────────────────
# Deliberately conservative to prevent over-stemming.
# Does NOT strip: -ness, -ation, -ing from short words.
# Priority: don't mangle > don't match.

_STEM_RULES = [
    # Plurals & verb forms — safe to strip
    ("nesses", ""),
    ("ness",   ""),
    ("lessly", ""),
    ("less",   ""),
    ("ings",   ""),
    ("ing",    ""),   # running→run, but only if stem ≥ 4 chars
    ("ations", ""),
    ("ation",  ""),
    ("ators",  ""),
    ("ator",   ""),
    ("ities",  ""),
    ("ity",    ""),
    ("ments",  ""),
    ("ment",   ""),
    ("iers",   ""),
    ("ier",    ""),
    ("ied",    "y"),
    ("ies",    "y"),
    ("ers",    ""),
    ("ed",     ""),
    ("es",     ""),
    ("s",      ""),
    ("ly",     ""),
    ("ful",    ""),
]

_MIN_STEM = 4   # minimum stem length after stripping


def _stem(word: str) -> str:
    if len(word) <= _MIN_STEM:
        return word
    for suffix, replacement in _STEM_RULES:
        if word.endswith(suffix) and len(word) - len(suffix) >= _MIN_STEM:
            return word[: len(word) - len(suffix)] + replacement
    return word


# ── Synonym / equivalence groups ──────────────────────────────────────────────
# Format: (canonical, {all members including inflections})
# Canonical = most common plain English form.
# List inflected forms explicitly — don't rely on stemmer for these.
# Covers the most common Quranic translation vocabulary.

_SYNONYM_GROUPS: list[tuple[str, set]] = [

    # ── Divine names & attributes ──────────────────────────────────────────
    ("allah",        {"allah", "god", "lord god"}),
    ("lord",         {"lord", "lords", "master", "masters", "sovereign",
                      "owner", "owners", "king", "ruler", "rulers", "rabb",
                      "cherisher", "sustainer", "nurturer", "maintainer",
                      "guardian", "provider", "caretaker"}),
    ("merciful",     {"merciful", "mercy", "compassionate", "compassion",
                      "gracious", "grace", "beneficent", "clement",
                      "kind", "kindness", "tender", "tenderness",
                      "rahman", "raheem", "forgiving", "forgive",
                      "forgiveness", "forgave", "pardoning", "pardon"}),
    ("almighty",     {"almighty", "mighty", "powerful", "power", "strength",
                      "strong", "exalted", "majestic", "majesty",
                      "glorious", "glory", "supreme", "highest",
                      "lofty", "elevated", "grand", "great", "greatness"}),
    ("knowing",      {"knowing", "knower", "knowledge", "know", "knows",
                      "knew", "aware", "awareness", "acquainted",
                      "informed", "cognizant", "omniscient", "wise",
                      "wisdom", "wiser", "wisest", "all-knowing"}),
    ("eternal",      {"eternal", "eternity", "everlasting", "forever",
                      "ever-living", "everliving", "living", "alive",
                      "self-subsisting", "self-sufficient", "self-sustaining",
                      "selfsustaining", "sustain", "sustains", "sustained",
                      "sustainer", "independent", "absolute", "samad",
                      "qayyum"}),
    ("creator",      {"creator", "create", "creates", "created", "creating",
                      "creation", "creature", "creatures", "maker",
                      "originator", "fashioner", "former"}),

    # ── Cosmological ──────────────────────────────────────────────────────
    ("worlds",       {"world", "worlds", "universe", "universes", "realm",
                      "realms", "creation", "creatures", "beings", "being",
                      "existence", "alamin", "mankind", "all creatures"}),
    ("heaven",       {"heaven", "heavens", "sky", "skies", "firmament",
                      "celestial", "above", "paradise", "jannah",
                      "garden", "gardens"}),
    ("earth",        {"earth", "ground", "land", "world", "terrain",
                      "soil"}),

    # ── Book / Scripture ──────────────────────────────────────────────────
    ("book",         {"book", "books", "scripture", "scriptures",
                      "writing", "writings", "record", "records",
                      "text", "quran", "revelation", "revealed",
                      "kitab", "tablet", "tablets"}),

    # ── Guidance / Path ───────────────────────────────────────────────────
    ("guide",        {"guide", "guides", "guided", "guiding", "guidance",
                      "direct", "directs", "directed", "direction",
                      "lead", "leads", "led", "leading", "huda",
                      "hidaya", "show", "shown", "correct", "right path",
                      "straight path"}),
    ("path",         {"path", "paths", "way", "ways", "road", "roads",
                      "route", "routes", "course", "sirat", "method",
                      "manner", "track"}),
    ("straight",     {"straight", "upright", "right", "correct", "true",
                      "proper", "sound", "firm", "established"}),

    # ── Praise / Thanks ───────────────────────────────────────────────────
    ("praise",       {"praise", "praised", "praises", "praising",
                      "thanks", "thank", "thankful", "thanksgiving",
                      "gratitude", "grateful", "glory", "glorify",
                      "glorification", "glorifies", "glorified",
                      "laud", "laudation", "extol", "hamd",
                      "commend", "commendation"}),

    # ── Judgement / Recompense ────────────────────────────────────────────
    ("judgment",     {"judgment", "judgement", "recompense", "retribution",
                      "requital", "reckoning", "repayment", "reward",
                      "account", "accountability", "day of judgment",
                      "punishment", "punish", "punished", "punishing",
                      "penalty", "penalise", "torment", "torture",
                      "chastise", "chastisement", "din", "yawm"}),

    # ── Anger / Wrath ─────────────────────────────────────────────────────
    ("anger",        {"anger", "angry", "wrath", "wrathful", "furious",
                      "fury", "rage", "indignation", "displeasure",
                      "displeased", "earned", "incurred", "ghadab",
                      "angered"}),

    # ── Astray / Error ────────────────────────────────────────────────────
    ("astray",       {"astray", "stray", "strayed", "straying", "gone astray",
                      "lost", "erring", "erred", "error", "wrong",
                      "misguidance", "misguided", "deviate", "deviated",
                      "deviation", "dallin", "mislead", "misled"}),

    # ── Blessing / Favor ──────────────────────────────────────────────────
    ("blessing",     {"blessing", "bless", "blessed", "blesses", "blissful",
                      "favor", "favour", "favored", "favoured", "favoring",
                      "bounty", "grace", "bestow", "bestowed", "bestowing",
                      "nima", "nimat", "gift", "gifts", "grace",
                      "benefit", "benefits", "benefited", "good"}),

    # ── Faith / Belief ────────────────────────────────────────────────────
    ("faith",        {"faith", "faithful", "belief", "believe", "believes",
                      "believed", "believer", "believers", "iman",
                      "trust", "trusting", "conviction", "pious",
                      "piety", "devout", "devoted", "devotion",
                      "mindful", "mindfulness", "conscious", "consciousness",
                      "god-fearing", "godfearing", "godconscious",
                      "god-conscious", "taqwa", "righteous", "righteousness",
                      "upright", "uprightness", "good deeds"}),

    # ── Messenger / Prophet ───────────────────────────────────────────────
    ("messenger",    {"messenger", "messengers", "prophet", "prophets",
                      "apostle", "apostles", "rasul", "nabi",
                      "sent", "envoy", "emissary"}),

    # ── Worship / Servant ─────────────────────────────────────────────────
    ("worship",      {"worship", "worships", "worshipped", "worshipping",
                      "serve", "serving", "served", "adore", "venerate",
                      "ibadah", "servant", "servants", "slave", "slaves",
                      "abd", "devoted", "devotion", "obey", "obedience",
                      "subject", "subjects", "prostrate", "prostration",
                      "bow", "bowing"}),

    # ── Help / Aid ────────────────────────────────────────────────────────
    ("help",         {"help", "helps", "helped", "helping", "aid",
                      "aids", "aided", "assistance", "assist",
                      "succour", "support", "supports", "supported",
                      "seek help", "cooperation", "awn"}),

    # ── Compulsion / Coercion ─────────────────────────────────────────────
    ("compulsion",   {"compulsion", "compel", "compelled", "coercion",
                      "coerce", "force", "forced", "constraint",
                      "constrain", "ikrah", "obligation", "obliged"}),

    # ── Truth / Righteousness vs Error ────────────────────────────────────
    ("truth",        {"truth", "true", "righteousness", "righteous",
                      "uprightness", "rushd", "clear", "distinct",
                      "evident", "manifest", "right", "correct"}),
    ("falsehood",    {"falsehood", "false", "error", "wrong", "lie",
                      "lying", "fabricate", "fabrication", "ghayy",
                      "misguidance"}),

    # ── Soul / Self ───────────────────────────────────────────────────────
    ("soul",         {"soul", "souls", "self", "selves", "person",
                      "persons", "nafs", "spirit", "spirits",
                      "individual", "being", "heart", "hearts",
                      "mind", "minds", "inner", "conscience"}),

    # ── Death / Afterlife ─────────────────────────────────────────────────
    ("death",        {"death", "die", "dying", "dies", "dead",
                      "mawt", "perish", "perishes", "perished",
                      "deceased", "expire", "expired"}),
    ("hereafter",    {"hereafter", "afterlife", "next life", "akhirah",
                      "eternal life", "life to come", "beyond",
                      "resurrection", "raised", "raised up", "day",
                      "last day", "final day"}),

    # ── Negation / Exception ──────────────────────────────────────────────
    ("not",          {"not", "nor", "neither", "never", "no",
                      "without", "except", "other", "besides",
                      "ghayr", "none", "nothing", "nobody", "none"}),

    # ── Reference words ───────────────────────────────────────────────────
    ("those",        {"those", "who", "whom", "that", "which",
                      "people", "ones", "whoever", "whomever",
                      "anyone", "anyone"}),

    # ── Knowledge / Signs ─────────────────────────────────────────────────
    ("sign",         {"sign", "signs", "verse", "verses", "ayah", "ayat",
                      "miracle", "miracles", "proof", "proofs",
                      "evidence", "evidences", "portent", "portents",
                      "token", "tokens"}),
    ("decree",       {"decree", "decrees", "decreed", "command",
                      "commands", "commanded", "commandment", "order",
                      "ordained", "ordain", "destine", "destiny",
                      "fate", "qadar", "qadr", "will", "decision"}),

    # ── Sleep / Drowsiness (for Ayat al-Kursi) ───────────────────────────
    ("sleep",        {"sleep", "sleeping", "slept", "slumber", "slumbers",
                      "drowsiness", "drowsy", "siesta", "doze",
                      "rest", "overcome", "overtake", "overtakes",
                      "overtook", "seize", "seized"}),

    # ── Throne / Seat / Kursi ─────────────────────────────────────────────
    ("seat",         {"seat", "seats", "throne", "thrones", "kursi",
                      "footstool", "pedestal", "chair", "extend",
                      "extends", "extended", "encompass", "encompassing",
                      "encompasses", "encompassed", "span", "spans",
                      "spanning", "cover", "covers", "covered",
                      "encompas", "extend"}),

    # ── Behind / After / Before ───────────────────────────────────────────
    ("behind",       {"behind", "after", "before", "ahead", "front",
                      "future", "past", "present", "between",
                      "what lies", "what is", "in front"}),

    # ── Anything / Something / Nothing ───────────────────────────────────
    ("anything",     {"anything", "something", "nothing", "everything",
                      "thing", "things", "anyth", "someth", "noth",
                      "whatsoever", "whatever", "aught"}),

    # ── Preservation / Protection ─────────────────────────────────────────
    ("preserve",     {"preserve", "preserves", "preserved", "preserving",
                      "preservation", "protect", "protects", "protected",
                      "protecting", "protection", "guard", "guards",
                      "guarded", "guarding", "keep", "keeps", "kept",
                      "care", "cares", "tire", "tires", "tired",
                      "tiring", "burden", "burdens", "weary", "wearied",
                      "preserv", "tir"}),
]

# Build lookup dict
_SYNONYM_MAP: dict[str, str] = {}
for _canonical, _members in _SYNONYM_GROUPS:
    for _word in _members:
        _SYNONYM_MAP[_word] = _canonical


def _canonicalise(word: str) -> str:
    """
    Normalise word to canonical form.
    Order: synonym map first (catches known forms), then stem + re-check.
    """
    if word in _SYNONYM_MAP:
        return _SYNONYM_MAP[word]
    stemmed = _stem(word)
    return _SYNONYM_MAP.get(stemmed, stemmed)


def clean_text(text: str) -> set:
    """
    Clean text into a normalised content-word set.

    Pipeline:
      1. Unicode normalise (allāh → allah)
      2. Word-separator punctuation → space
      3. Remove parenthesised content: (be), (the), (of) etc.
      4. Strip punctuation
      5. Lowercase
      6. Remove stopwords and single-char tokens
      7. Remove stray trailing digits (lord1 → lord)
      8. Canonicalise (synonym map + stem)
    """
    if not text:
        return set()

    text = _normalise_unicode(text)

    # Remove parenthesised gloss qualifiers like (be), (the), (of Allah)
    text = re.sub(r'\([^)]*\)', ' ', text)

    # Word-separator chars → space
    separators = "\u2014\u2013\u2018\u2019\u201c\u201d\u060c\u061b\u061f\u02be\u02bf\u2026"
    for ch in separators:
        text = text.replace(ch, " ")

    translator = str.maketrans("", "", string.punctuation)
    text = text.translate(translator).lower()

    result = set()
    for w in text.split():
        # Remove stray trailing digits
        w = re.sub(r'([a-z]+)\d+$', r'\1', w)
        if not w or w in STOP_WORDS or len(w) < 2:
            continue
        result.add(_canonicalise(w))

    return result


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    return len(a & b) / len(union) if union else 0.0


# ── Layer 1: Gloss Fidelity ────────────────────────────────────────────────────

def gloss_fidelity_score(translation_text: str, gloss_words: list) -> dict:
    trans_words    = clean_text(translation_text)
    gloss_text     = " ".join(str(g) for g in gloss_words)
    gloss_word_set = clean_text(gloss_text)

    score   = jaccard(trans_words, gloss_word_set)
    matched = trans_words & gloss_word_set
    missing = gloss_word_set - trans_words
    extra   = trans_words - gloss_word_set

    return {
        "score":       round(score, 4),
        "trans_words": sorted(trans_words),
        "gloss_words": sorted(gloss_word_set),
        "matched":     sorted(matched),
        "missing":     sorted(missing),
        "extra":       sorted(extra),
    }


# ── Layer 2: Root Semantic Fidelity ───────────────────────────────────────────

def root_fidelity_score(translation_text: str, roots: dict) -> dict:
    trans_words = clean_text(translation_text)

    if not roots:
        return {"score": None, "root_breakdown": [],
                "roots_covered": 0, "roots_total": 0}

    distinct_roots = {}
    for arabic_word, root in roots.items():
        distinct_roots.setdefault(root, []).append(arabic_word)

    root_scores = []
    breakdown   = []
    covered     = 0

    for root, arabic_words in distinct_roots.items():
        entry = ROOT_LEXICON.get(root)
        if not entry:
            breakdown.append({
                "root": root, "arabic_words": arabic_words,
                "latin": "", "category": "Uncovered",
                "status": "not_in_lexicon", "matched_words": [],
                "per_root_score": None,
            })
            continue

        covered += 1
        core_field     = {_canonicalise(w) for w in entry["core"]}
        extended_field = {_canonicalise(w) for w in entry["extended"]}
        avoid_field    = {_canonicalise(w) for w in entry["avoid"]}

        core_matches     = trans_words & core_field
        extended_matches = trans_words & extended_field
        avoid_matches    = trans_words & avoid_field

        if core_matches:
            per_root_score = 1.0; status = "core_match"; matched = sorted(core_matches)
        elif extended_matches:
            per_root_score = 0.6; status = "extended_match"; matched = sorted(extended_matches)
        elif avoid_matches:
            per_root_score = -0.3; status = "avoid_match"; matched = sorted(avoid_matches)
        else:
            per_root_score = 0.0; status = "no_match"; matched = []

        root_scores.append(per_root_score)
        breakdown.append({
            "root": root, "arabic_words": arabic_words,
            "latin": entry["latin"], "category": entry["category"],
            "status": status, "matched_words": matched,
            "per_root_score": per_root_score,
        })

    if not root_scores:
        overall = None
    else:
        raw = sum(root_scores) / len(root_scores)
        overall = round(max(0.0, min(1.0, raw)), 4)

    return {
        "score": overall, "root_breakdown": breakdown,
        "roots_covered": covered, "roots_total": len(distinct_roots),
    }


# ── Combined scoring ────────────────────────────────────────────────────────────

TRANSLATOR_KEYS = ["sahih", "haleem", "khattab", "soliman", "kanzuliman"]
TRANSLATOR_LABELS = {
    "sahih":      "Sahih International",
    "haleem":     "Abdel Haleem",
    "khattab":    "Mustafa Khattab",
    "soliman":    "Fadel Soliman / Bridges",
    "kanzuliman": "Ala Hazrat / A.F. Qadri",
}
SCORE_LABELS = {
    "gloss": "Literal Accuracy",
    "root":  "Semantic Depth",
}


def score_all_translators(translations: dict, roots: dict, gloss_words: list) -> dict:
    results = {}
    for key in TRANSLATOR_KEYS:
        text = translations.get(key, "") or ""
        if not text.strip():
            results[key] = {"gloss": None, "root": None}
            continue
        results[key] = {
            "gloss": gloss_fidelity_score(text, gloss_words),
            "root":  root_fidelity_score(text, roots),
        }
    return results


if __name__ == "__main__":
    # Test the key problematic cases from diagnosis
    tests = [
        {
            "label": "1:1",
            "gloss": ["All praises and thanks", "(be) to Allah", "the Lord", "of the universe"],
            "sahih": "All praise is due to Allah, Lord of the worlds.",
            "haleem": "Praise belongs to Allah, Lord of the Worlds,",
        },
        {
            "label": "2:2",
            "gloss": ["That", "(is) the book", "no", "doubt", "in it", "guidance", "for those conscious of Allah"],
            "sahih": "This is the Book about which there is no doubt, a guidance for those conscious of Allah.",
            "haleem": "This is the Scripture in which there is no doubt, containing guidance for those who are mindful of God,",
        },
        {
            "label": "2:255 (Ayat al-Kursi)",
            "gloss": ["Allah", "no", "God", "except", "He", "the Ever-Living", "the Sustainer",
                      "not", "overtake", "Him", "drowsiness", "nor", "sleep",
                      "to Him", "belongs", "what", "in", "the heavens",
                      "and what", "in", "the earth", "who", "intercede",
                      "except", "by", "His permission", "He knows", "what",
                      "before them", "and what", "behind them",
                      "and not", "they encompass", "anything", "of His knowledge",
                      "except", "what", "He wills", "extends", "His seat",
                      "the heavens", "and the earth", "and not", "tires Him",
                      "their preservation", "and He", "the High", "the Great"],
            "sahih": "Allah — there is no deity except Him, the Ever-Living, the Sustainer of existence. Neither drowsiness overtakes Him nor sleep. To Him belongs whatever is in the heavens and whatever is on the earth. Who is it that can intercede with Him except by His permission? He knows what is before them and what will be after them, and they encompass not a thing of His knowledge except for what He wills. His Kursi extends over the heavens and the earth, and their preservation tires Him not. And He is the Most High, the Most Great.",
            "haleem": "God: there is no god but Him, the Ever Living, the Ever Watchful. Neither slumber nor sleep overtakes Him. All that is in the heavens and in the earth belongs to Him. Who is there that can intercede with Him except by His own permission? He knows what is before them and what is behind them, but they do not comprehend any of His knowledge except what He wills.",
        },
    ]

    for test in tests:
        gloss_words = clean_text(" ".join(test["gloss"]))
        sahih_words = clean_text(test["sahih"])
        haleem_words = clean_text(test["haleem"])
        sahih_score  = jaccard(sahih_words, gloss_words)
        haleem_score = jaccard(haleem_words, gloss_words)
        print(f"\n{test['label']}")
        print(f"  gloss words:  {sorted(gloss_words)}")
        print(f"  sahih score:  {sahih_score:.3f}")
        print(f"  haleem score: {haleem_score:.3f}")
        print(f"  sahih missing: {sorted(gloss_words - sahih_words)}")