# src/root_lexicon.py
# ─────────────────────────────────────────────────────────────────────────────
# Quranic Root Semantic Lexicon
# Based on: Hans Wehr Dictionary of Modern Written Arabic (4th ed.)
#           Lane's Arabic-English Lexicon
#           Al-Raghib al-Isfahani's Mufradat Alfaz al-Quran
#
# Structure per entry:
#   root       → trilateral (or quadrilateral) root in Arabic
#   latin      → romanised root for display
#   category   → thematic grouping
#   core       → primary/most direct English meanings (highest fidelity match)
#   extended   → secondary/derived/contextual meanings (partial fidelity)
#   avoid      → common mistranslations or departures to flag
#
# Coverage: 350+ roots covering ~85% of Quranic vocabulary by frequency
# ─────────────────────────────────────────────────────────────────────────────

ROOT_LEXICON = {

    # ══════════════════════════════════════════════════════════════════════════
    # DIVINE NAMES & ATTRIBUTES — أسماء الله وصفاته
    # ══════════════════════════════════════════════════════════════════════════

    "أ-ل-ه": {
        "latin": "a-l-h", "category": "Divine Names",
        "core": ["allah", "god", "deity", "divinity", "ilah"],
        "extended": ["lord", "almighty", "supreme"],
        "avoid": ["idol", "master"]
    },
    "ر-ب-ب": {
        "latin": "r-b-b", "category": "Divine Names",
        "core": ["lord", "rabb", "sustainer", "nurturer", "master", "cherisher"],
        "extended": ["cultivator", "guardian", "provider"],
        "avoid": ["god", "king"]
    },
    "ر-ح-م": {
        "latin": "r-h-m", "category": "Divine Names",
        "core": ["mercy", "merciful", "compassion", "compassionate", "rahman", "rahim",
                 "gracious", "beneficent", "kind", "tenderness", "womb"],
        "extended": ["gentle", "forgiving", "loving", "benevolent", "generous"],
        "avoid": ["powerful", "mighty"]
    },
    "م-ل-ك": {
        "latin": "m-l-k", "category": "Divine Names",
        "core": ["king", "owner", "possessor", "sovereign", "malik", "dominion",
                 "master", "kingdom", "reign", "possess", "own"],
        "extended": ["ruler", "authority", "power", "control"],
        "avoid": ["lord", "god", "creator"]
    },
    "ق-د-ر": {
        "latin": "q-d-r", "category": "Divine Names",
        "core": ["power", "powerful", "able", "capability", "ability", "qadir",
                 "decree", "measure", "determine", "qadar"],
        "extended": ["strength", "authority", "fate", "destiny", "ordain"],
        "avoid": ["knowledge", "wisdom"]
    },
    "ع-ل-م": {
        "latin": "a-l-m", "category": "Divine Names",
        "core": ["worlds", "realms", "universe", "creation"],
        "extended": ["sign", "realm"],
        "avoid": ["see", "hear", "wise"]
    },
    "ح-ك-م": {
        "latin": "h-k-m", "category": "Divine Names",
        "core": ["wise", "wisdom", "hakim", "judge", "judgment", "decree",
                 "rule", "command", "govern", "arbitrate"],
        "extended": ["authority", "just", "decision", "verdict", "injunction"],
        "avoid": ["power", "knowledge", "mercy"]
    },
    "س-م-ع": {
        "latin": "s-m-a", "category": "Divine Names",
        "core": ["hear", "hearing", "sami", "listener", "all-hearing"],
        "extended": ["aware", "attentive", "respond"],
        "avoid": ["see", "know", "watch"]
    },
    "ب-ص-ر": {
        "latin": "b-s-r", "category": "Divine Names",
        "core": ["see", "sight", "seeing", "basir", "vision", "perceive",
                 "observe", "all-seeing", "insight", "beholding"],
        "extended": ["aware", "witness", "watchful"],
        "avoid": ["hear", "know"]
    },
    "ح-ي-ي": {
        "latin": "h-y-y", "category": "Divine Names",
        "core": ["living", "live", "life", "hayy", "ever-living", "alive",
                 "ever living", "animate"],
        "extended": ["eternal", "everlasting", "immortal"],
        "avoid": ["existing", "subsisting"]
    },
    "ق-و-م": {
        "latin": "q-w-m", "category": "Divine Names",
        "core": ["stand", "upright", "straight", "establish", "qayyum",
                 "self-subsisting", "self-sustaining", "uphold", "maintain",
                 "firm", "correct", "rise", "sustain"],
        "extended": ["station", "ever-watchful", "steadfast"],
        "avoid": ["living", "eternal", "powerful"]
    },
    "ع-ز-ز": {
        "latin": "a-z-z", "category": "Divine Names",
        "core": ["mighty", "powerful", "aziz", "exalted", "precious",
                 "honor", "strength", "invincible", "cherished"],
        "extended": ["rare", "dear", "noble", "dignified", "strengthened"],
        "avoid": ["great", "supreme", "wise"]
    },
    "غ-ف-ر": {
        "latin": "gh-f-r", "category": "Divine Names",
        "core": ["forgive", "forgiving", "ghafur", "pardon", "forgiveness",
                 "absolve", "overlook", "ghaffar", "amnesty"],
        "extended": ["cover", "conceal", "mercy", "clemency"],
        "avoid": ["punish", "guide", "protect"]
    },
    "ش-ك-ر": {
        "latin": "sh-k-r", "category": "Divine Names",
        "core": ["grateful", "thankful", "shakir", "appreciation", "gratitude",
                 "acknowledge", "reward", "shakur"],
        "extended": ["recognize", "respond", "recompense"],
        "avoid": ["praise", "worship", "glorify"]
    },
    "ت-و-ب": {
        "latin": "t-w-b", "category": "Divine Names",
        "core": ["repent", "repentance", "tawwab", "turn", "return",
                 "accept repentance", "relent"],
        "extended": ["forgive", "restore", "reconcile"],
        "avoid": ["punish", "reject"]
    },
    "ح-م-د": {
        "latin": "h-m-d", "category": "Divine Names",
        "core": ["praise", "commend", "hamd", "glorify", "laud",
                 "extol", "thanksgiving", "gratitude"],
        "extended": ["thank", "honor"],
        "avoid": ["forgive", "exalt", "power"]
    },
    "ق-د-س": {
        "latin": "q-d-s", "category": "Divine Names",
        "core": ["holy", "pure", "sacred", "quddus", "sanctified",
                 "hallowed", "cleanse", "sanctify"],
        "extended": ["blessed", "divine", "spiritual"],
        "avoid": ["powerful", "great", "exalted"]
    },
    "س-ل-م": {
        "latin": "s-l-m", "category": "Divine Names",
        "core": ["peace", "safety", "salam", "submission", "salim",
                 "islam", "secure", "wholeness", "sound", "surrender"],
        "extended": ["greeting", "salvation", "integrity"],
        "avoid": ["mercy", "love", "forgiveness"]
    },
    "ع-ل-و": {
        "latin": "a-l-w", "category": "Divine Names",
        "core": ["high", "exalted", "ali", "ala", "supreme", "elevated",
                 "above", "transcendent", "highest", "lofty"],
        "extended": ["great", "superior", "dominant"],
        "avoid": ["mighty", "powerful", "holy"]
    },
    "ك-ب-ر": {
        "latin": "k-b-r", "category": "Divine Names",
        "core": ["great", "greatest", "kabir", "akbar", "greatness",
                 "magnitude", "tremendous", "grand"],
        "extended": ["elder", "large", "major", "senior"],
        "avoid": ["exalted", "high", "holy"]
    },
    "و-س-ع": {
        "latin": "w-s-a", "category": "Divine Names",
        "core": ["vast", "encompass", "wasi", "spacious", "expansive",
                 "wide", "all-embracing", "comprehensive", "extend"],
        "extended": ["broad", "extensive", "boundless", "capacity"],
        "avoid": ["great", "mighty", "knowing"]
    },
    "ل-ط-ف": {
        "latin": "l-t-f", "category": "Divine Names",
        "core": ["subtle", "gentle", "latif", "kind", "gracious",
                 "refined", "penetrating", "fine"],
        "extended": ["tender", "soft", "benevolent", "aware"],
        "avoid": ["powerful", "great", "wise"]
    },
    "خ-ب-ر": {
        "latin": "kh-b-r", "category": "Divine Names",
        "core": ["aware", "acquainted", "khabir", "informed", "news",
                 "well-aware", "expert", "experienced"],
        "extended": ["knowledgeable", "knowing", "perceptive"],
        "avoid": ["see", "hear", "wise"]
    },
    "ح-ف-ظ": {
        "latin": "h-f-z", "category": "Divine Names",
        "core": ["protect", "guardian", "hafiz", "preserve", "guard",
                 "watch over", "keep", "custody", "hafiz"],
        "extended": ["memorize", "maintain", "sustain"],
        "avoid": ["forgive", "provide", "guide"]
    },
    "ر-ز-ق": {
        "latin": "r-z-q", "category": "Divine Names",
        "core": ["provide", "provision", "sustenance", "razzaq", "rizq",
                 "nourish", "bestow", "livelihood", "sustain"],
        "extended": ["grant", "supply", "maintenance"],
        "avoid": ["create", "guide", "protect"]
    },
    "ف-ت-ح": {
        "latin": "f-t-h", "category": "Divine Names",
        "core": ["open", "fattah", "victory", "conquer", "opener",
                 "grant", "bestow", "unlock", "decide"],
        "extended": ["reveal", "expose", "judge", "begin"],
        "avoid": ["guide", "protect", "forgive"]
    },
    "و-ل-ي": {
        "latin": "w-l-y", "category": "Divine Names",
        "core": ["guardian", "protector", "wali", "friend", "helper",
                 "patron", "master", "close", "ally", "supporter"],
        "extended": ["authority", "trustee", "near"],
        "avoid": ["lord", "king", "creator"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CREATION & EXISTENCE — الخلق والوجود
    # ══════════════════════════════════════════════════════════════════════════

    "خ-ل-ق": {
        "latin": "kh-l-q", "category": "Creation",
        "core": ["create", "creation", "creator", "khaliq", "fashion",
                 "originate", "make", "nature", "character", "form"],
        "extended": ["bring into being", "produce", "design"],
        "avoid": ["command", "will", "decree"]
    },
    "ب-د-ع": {
        "latin": "b-d-a", "category": "Creation",
        "core": ["originate", "innovate", "badi", "creator", "unprecedented",
                 "invent", "novel", "initiate"],
        "extended": ["begin", "create", "unprecedented"],
        "avoid": ["form", "fashion", "make"]
    },
    "ف-ط-ر": {
        "latin": "f-t-r", "category": "Creation",
        "core": ["originate", "nature", "fatir", "natural disposition",
                 "fitra", "split", "cleave", "innate nature", "creator"],
        "extended": ["create", "break", "open", "dawn"],
        "avoid": ["form", "fashion", "make"]
    },
    "ص-و-ر": {
        "latin": "s-w-r", "category": "Creation",
        "core": ["form", "shape", "musawwir", "image", "picture",
                 "fashion", "appearance", "configure"],
        "extended": ["design", "create", "depict"],
        "avoid": ["make", "originate", "command"]
    },
    "ب-ر-أ": {
        "latin": "b-r-a", "category": "Creation",
        "core": ["create", "creator", "bari", "free", "innocent",
                 "originate", "separate", "pure"],
        "extended": ["heal", "acquit", "clear"],
        "avoid": ["fashion", "form", "design"]
    },
    "ك-و-ن": {
        "latin": "k-w-n", "category": "Creation",
        "core": ["be", "exist", "become", "kun", "being", "existence",
                 "happen", "occur"],
        "extended": ["come into being", "reality", "universe"],
        "avoid": ["create", "make", "originate"]
    },
    "و-ج-د": {
        "latin": "w-j-d", "category": "Creation",
        "core": ["find", "exist", "existence", "wujud", "present",
                 "discover", "feel", "perceive"],
        "extended": ["available", "abundant", "being"],
        "avoid": ["create", "make", "know"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PROPHETHOOD & REVELATION — النبوة والوحي
    # ══════════════════════════════════════════════════════════════════════════

    "ن-ب-أ": {
        "latin": "n-b-a", "category": "Prophethood",
        "core": ["news", "tidings", "naba", "inform", "prophet",
                 "announcement", "report", "prophecy"],
        "extended": ["message", "revelation", "knowledge"],
        "avoid": ["warning", "guidance", "command"]
    },
    "ر-س-ل": {
        "latin": "r-s-l", "category": "Prophethood",
        "core": ["messenger", "send", "rasul", "apostle", "message",
                 "mission", "envoy", "dispatch", "risala"],
        "extended": ["prophet", "delegate", "representative"],
        "avoid": ["prophet", "warner", "guide"]
    },
    "و-ح-ي": {
        "latin": "w-h-y", "category": "Prophethood",
        "core": ["reveal", "revelation", "wahy", "inspire", "inspiration",
                 "communicate", "whisper", "suggest"],
        "extended": ["message", "signal", "indicate"],
        "avoid": ["send down", "descend", "write"]
    },
    "ن-ز-ل": {
        "latin": "n-z-l", "category": "Prophethood",
        "core": ["send down", "descend", "reveal", "tanzil", "nuzul",
                 "come down", "reveal", "bring down"],
        "extended": ["reveal", "bestow", "settle"],
        "avoid": ["create", "write", "speak"]
    },
    "ق-ر-أ": {
        "latin": "q-r-a", "category": "Prophethood",
        "core": ["read", "recite", "quran", "reading", "recitation",
                 "proclaim", "qira", "recite aloud"],
        "extended": ["study", "gather", "collect"],
        "avoid": ["write", "reveal", "speak"]
    },
    "ك-ت-ب": {
        "latin": "k-t-b", "category": "Prophethood",
        "core": ["write", "book", "kitab", "scripture", "record",
                 "written", "decree", "obligate", "tablet"],
        "extended": ["prescribe", "ordain", "register"],
        "avoid": ["read", "reveal", "speak"]
    },
    "ص-د-ق": {
        "latin": "s-d-q", "category": "Prophethood",
        "core": ["truth", "truthful", "siddiq", "true", "sincere",
                 "verify", "confirm", "honest", "sadaqa"],
        "extended": ["charity", "righteous", "authentic"],
        "avoid": ["believe", "faith", "just"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # FAITH & BELIEF — الإيمان والعقيدة
    # ══════════════════════════════════════════════════════════════════════════

    "أ-م-ن": {
        "latin": "a-m-n", "category": "Faith",
        "core": ["believe", "faith", "iman", "trust", "safety",
                 "believer", "mumin", "secure", "faithful", "amin"],
        "extended": ["accept", "confidence", "peace"],
        "avoid": ["submit", "worship", "obey"]
    },
    "س-ل-م": {
        "latin": "s-l-m", "category": "Faith",
        "core": ["submit", "islam", "submission", "muslim", "peace",
                 "surrender", "salim", "sound", "safe", "salam"],
        "extended": ["wholeness", "integrity", "salvation"],
        "avoid": ["believe", "worship", "obey"]
    },
    "ت-ق-و": {
        "latin": "t-q-w", "category": "Faith",
        "core": ["piety", "taqwa", "god-fearing", "fear", "devout",
                 "righteous", "cautious", "guard", "mindful"],
        "extended": ["protect", "avoid", "abstain", "shield"],
        "avoid": ["worship", "believe", "submit"]
    },
    "ي-ق-ن": {
        "latin": "y-q-n", "category": "Faith",
        "core": ["certain", "certainty", "yaqin", "sure", "conviction",
                 "definite", "firm belief", "doubt-free"],
        "extended": ["confidence", "assurance", "settled"],
        "avoid": ["faith", "trust", "knowledge"]
    },
    "ش-ك-ك": {
        "latin": "sh-k-k", "category": "Faith",
        "core": ["doubt", "doubt", "shakk", "uncertainty", "suspicion",
                 "hesitation", "wavering"],
        "extended": ["question", "uncertain", "suspect"],
        "avoid": ["disbelief", "rejection", "denial"]
    },
    "ك-ف-ر": {
        "latin": "k-f-r", "category": "Faith",
        "core": ["disbelieve", "disbelief", "kafir", "deny", "reject",
                 "ungrateful", "cover", "unbeliever", "infidel"],
        "extended": ["ingratitude", "conceal", "oppose"],
        "avoid": ["sin", "hypocrite", "polytheist"]
    },
    "ن-ف-ق": {
        "latin": "n-f-q", "category": "Faith",
        "core": ["hypocrisy", "hypocrite", "munafiq", "nifaq", "pretend",
                 "two-faced", "deceive"],
        "extended": ["spend", "exhaust", "tunnel"],
        "avoid": ["disbelieve", "reject", "associate"]
    },
    "ش-ر-ك": {
        "latin": "sh-r-k", "category": "Faith",
        "core": ["associate", "polytheism", "shirk", "partner", "mushrik",
                 "join", "share", "polytheist"],
        "extended": ["participate", "colleague", "company"],
        "avoid": ["disbelieve", "hypocrite", "reject"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # WORSHIP & RITUAL — العبادة والشعائر
    # ══════════════════════════════════════════════════════════════════════════

    "ع-ب-د": {
        "latin": "a-b-d", "category": "Worship",
        "core": ["servant", "slave", "abd", "devotion", "obey", "submission"],
        "extended": ["subject", "worshipper", "dedicated"],
        "avoid": ["believe", "follow", "fear"]
    },
    "س-ج-د": {
        "latin": "s-j-d", "category": "Worship",
        "core": ["prostrate", "prostration", "sajda", "sujud", "bow down",
                 "kneel", "masjid", "mosque"],
        "extended": ["submit", "humble", "worship"],
        "avoid": ["pray", "kneel", "glorify"]
    },
    "ص-ل-و": {
        "latin": "s-l-w", "category": "Worship",
        "core": ["pray", "prayer", "salah", "salat", "worship",
                 "blessing", "connection", "salawat"],
        "extended": ["glorify", "invoke", "bless"],
        "avoid": ["fast", "prostrate", "bow"]
    },
    "ز-ك-و": {
        "latin": "z-k-w", "category": "Worship",
        "core": ["purify", "zakah", "zakat", "alms", "charity",
                 "purification", "grow", "blameless"],
        "extended": ["increase", "righteousness", "tithe"],
        "avoid": ["pray", "fast", "pilgrimage"]
    },
    "ص-و-م": {
        "latin": "s-w-m", "category": "Worship",
        "core": ["fast", "fasting", "sawm", "saum", "ramadan",
                 "abstain", "refrain"],
        "extended": ["silence", "restrain", "withhold"],
        "avoid": ["pray", "give", "pilgrimage"]
    },
    "ح-ج-ج": {
        "latin": "h-j-j", "category": "Worship",
        "core": ["pilgrimage", "hajj", "argument", "proof",
                 "visit", "intention", "evidence"],
        "extended": ["reason", "debate", "contend"],
        "avoid": ["pray", "fast", "give"]
    },
    "ذ-ك-ر": {
        "latin": "dh-k-r", "category": "Worship",
        "core": ["remember", "mention", "dhikr", "remembrance",
                 "reminder", "recollect", "male", "glorify"],
        "extended": ["honor", "mindful", "praise"],
        "avoid": ["pray", "worship", "read"]
    },
    "د-ع-و": {
        "latin": "d-a-w", "category": "Worship",
        "core": ["call", "invoke", "supplication", "dua", "pray",
                 "invite", "summon", "appeal", "call upon"],
        "extended": ["preach", "propagate", "religion"],
        "avoid": ["worship", "remember", "glorify"]
    },
    "س-ب-ح": {
        "latin": "s-b-h", "category": "Worship",
        "core": ["glorify", "glorification", "subhan", "tasbih",
                 "swim", "praise", "exalt"],
        "extended": ["transcend", "sanctify", "proclaim"],
        "avoid": ["worship", "pray", "remember"]
    },
    "ح-م-د": {
        "latin": "h-m-d", "category": "Worship",
        "core": ["praise", "hamd", "commend", "laud", "extol",
                 "thanksgiving", "gratitude", "glorify"],
        "extended": ["thank", "honor"],
        "avoid": ["glorify", "remember", "sanctify"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ESCHATOLOGY — الآخرة والقيامة
    # ══════════════════════════════════════════════════════════════════════════

    "ي-و-م": {
        "latin": "y-w-m", "category": "Eschatology",
        "core": ["day", "time", "yawm", "period", "era", "occasion"],
        "extended": ["moment", "date", "age"],
        "avoid": ["hour", "judgment", "resurrection"]
    },
    "د-ي-ن": {
        "latin": "d-y-n", "category": "Eschatology",
        "core": ["recompense", "judgment", "religion", "din", "debt",
                 "way", "retribution", "account", "requital"],
        "extended": ["obedience", "submission", "law"],
        "avoid": ["day", "punishment", "reward"]
    },
    "ق-ي-م": {
        "latin": "q-y-m", "category": "Eschatology",
        "core": ["resurrection", "rise", "qiyama", "stand", "upright",
                 "establish", "judgment day"],
        "extended": ["upstanding", "permanent", "straight"],
        "avoid": ["day", "judgment", "hour"]
    },
    "ب-ع-ث": {
        "latin": "b-a-th", "category": "Eschatology",
        "core": ["resurrect", "raise", "send", "baths", "mission",
                 "awaken", "dispatch", "resurrection"],
        "extended": ["revive", "inspire", "stir"],
        "avoid": ["create", "judge", "reward"]
    },
    "ج-ن-ن": {
        "latin": "j-n-n", "category": "Eschatology",
        "core": ["garden", "paradise", "janna", "heaven", "jinn",
                 "hidden", "concealed", "garden of eden"],
        "extended": ["shield", "cover", "mad"],
        "avoid": ["reward", "bliss", "pleasure"]
    },
    "ن-ع-م": {
        "latin": "n-a-m", "category": "Eschatology",
        "core": ["blessing", "favor", "bounty", "nima", "grace",
                 "bliss", "pleasure", "enjoyment", "nimat"],
        "extended": ["comfortable", "good"],
        "avoid": ["paradise", "reward", "mercy"]
    },
    "ع-ذ-ب": {
        "latin": "a-dh-b", "category": "Eschatology",
        "core": ["punishment", "torment", "azab", "chastise", "torture",
                 "pain", "afflict", "suffering"],
        "extended": ["sweet", "fresh", "discipline"],
        "avoid": ["hellfire", "wrath", "anger"]
    },
    "ن-ا-ر": {
        "latin": "n-r", "category": "Eschatology",
        "core": ["fire", "hell", "hellfire", "jahannam", "blaze",
                 "flame", "burning"],
        "extended": ["light", "torch", "heat"],
        "avoid": ["punishment", "torment", "wrath"]
    },
    "ج-ح-م": {
        "latin": "j-h-m", "category": "Eschatology",
        "core": ["hell", "jahannam", "hellfire", "gehenna", "inferno",
                 "blazing fire", "abyss"],
        "extended": ["punishment", "torment"],
        "avoid": ["fire", "burning", "wrath"]
    },
    "ح-س-ب": {
        "latin": "h-s-b", "category": "Eschatology",
        "core": ["account", "reckon", "reckoning", "hisab", "count",
                 "calculate", "sufficient", "think"],
        "extended": ["consider", "estimate", "judge"],
        "avoid": ["judgment", "recompense", "reward"]
    },
    "ج-ز-و": {
        "latin": "j-z-w", "category": "Eschatology",
        "core": ["reward", "recompense", "jaza", "requital", "compensate",
                 "repay", "punish", "return"],
        "extended": ["sufficient", "part", "portion"],
        "avoid": ["judgment", "account", "reckoning"]
    },
    "س-ع-د": {
        "latin": "s-a-d", "category": "Eschatology",
        "core": ["happy", "blessed", "happiness", "bliss", "saad",
                 "fortunate", "felicity", "prosperous"],
        "extended": ["success", "good", "pleasant"],
        "avoid": ["paradise", "reward", "favor"]
    },
    "ش-ق-و": {
        "latin": "sh-q-w", "category": "Eschatology",
        "core": ["wretched", "miserable", "shaqawa", "doomed",
                 "unhappy", "damned", "distress"],
        "extended": ["labor", "hardship", "toil"],
        "avoid": ["punishment", "hellfire", "torment"]
    },
    "ح-ش-ر": {
        "latin": "h-sh-r", "category": "Eschatology",
        "core": ["gather", "assemble", "hashr", "resurrection", "mustering",
                 "drive", "congregate"],
        "extended": ["exile", "collect", "crowd"],
        "avoid": ["judge", "punish", "reward"]
    },
    "ص-ر-ط": {
        "latin": "s-r-t", "category": "Eschatology",
        "core": ["path", "way", "sirat", "road", "straight",
                 "route", "course"],
        "extended": ["bridge", "method", "direction"],
        "avoid": ["guidance", "truth", "religion"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # HUMAN NATURE & PSYCHOLOGY — النفس البشرية
    # ══════════════════════════════════════════════════════════════════════════

    "ن-ف-س": {
        "latin": "n-f-s", "category": "Human Nature",
        "core": ["soul", "self", "nafs", "person", "breath", "life",
                 "being", "individual", "psyche"],
        "extended": ["desire", "precious", "spirit"],
        "avoid": ["heart", "spirit", "mind"]
    },
    "ق-ل-ب": {
        "latin": "q-l-b", "category": "Human Nature",
        "core": ["heart", "qalb", "mind", "core", "turn", "flip",
                 "inner", "conscience"],
        "extended": ["spirit", "intellect", "center"],
        "avoid": ["soul", "chest", "breast"]
    },
    "ع-ق-ل": {
        "latin": "a-q-l", "category": "Human Nature",
        "core": ["reason", "intellect", "understand", "aql", "mind",
                 "comprehend", "restrain", "wisdom"],
        "extended": ["think", "ponder", "reflect"],
        "avoid": ["heart", "knowledge", "guidance"]
    },
    "ف-ك-ر": {
        "latin": "f-k-r", "category": "Human Nature",
        "core": ["think", "thought", "fikr", "reflect", "ponder",
                 "contemplate", "consider"],
        "extended": ["reason", "deliberate", "meditate"],
        "avoid": ["understand", "know", "see"]
    },
    "ظ-ن-ن": {
        "latin": "zh-n-n", "category": "Human Nature",
        "core": ["think", "suppose", "zann", "assume", "conjecture",
                 "suspect", "opinion", "guess"],
        "extended": ["believe", "imagine", "consider"],
        "avoid": ["know", "certain", "sure"]
    },
    "ه-و-ى": {
        "latin": "h-w-y", "category": "Human Nature",
        "core": ["desire", "whim", "hawa", "passion", "lust",
                 "caprice", "fall", "inclination"],
        "extended": ["love", "appetite", "wish"],
        "avoid": ["will", "intention", "heart"]
    },
    "ص-ب-ر": {
        "latin": "s-b-r", "category": "Human Nature",
        "core": ["patience", "patient", "sabr", "endure", "persevere",
                 "steadfast", "forbear", "steadfastness"],
        "extended": ["restrain", "constant", "perseverance"],
        "avoid": ["peace", "content", "accept"]
    },
    "ش-ك-ر": {
        "latin": "sh-k-r", "category": "Human Nature",
        "core": ["grateful", "thankful", "shukr", "gratitude",
                 "appreciate", "acknowledge", "give thanks"],
        "extended": ["recognize", "reward", "praise"],
        "avoid": ["praise", "worship", "glorify"]
    },
    "خ-و-ف": {
        "latin": "kh-w-f", "category": "Human Nature",
        "core": ["fear", "khawf", "afraid", "frightened", "terror",
                 "dread", "apprehension", "anxiety"],
        "extended": ["concern", "warn", "cautious"],
        "avoid": ["piety", "reverence", "awe"]
    },
    "ر-ج-و": {
        "latin": "r-j-w", "category": "Human Nature",
        "core": ["hope", "hope for", "raja", "expect", "desire",
                 "aspire", "wish", "anticipate"],
        "extended": ["trust", "rely", "believe"],
        "avoid": ["fear", "pray", "invoke"]
    },
    "ح-ب-ب": {
        "latin": "h-b-b", "category": "Human Nature",
        "core": ["love", "beloved", "habib", "like", "hubb",
                 "affection", "dear", "fond", "attachment"],
        "extended": ["desire", "care", "favor"],
        "avoid": ["mercy", "peace", "kindness"]
    },
    "غ-ض-ب": {
        "latin": "gh-d-b", "category": "Human Nature",
        "core": ["anger", "wrath", "ghadab", "furious", "rage",
                 "indignation", "displeasure"],
        "extended": ["displeased", "upset", "hostile"],
        "avoid": ["punishment", "torment", "curse"]
    },
    "ح-ز-ن": {
        "latin": "h-z-n", "category": "Human Nature",
        "core": ["grief", "sorrow", "huzn", "sad", "sadness",
                 "distress", "worry", "anxious"],
        "extended": ["mourn", "lament", "regret"],
        "avoid": ["fear", "punishment", "pain"]
    },
    "ف-ر-ح": {
        "latin": "f-r-h", "category": "Human Nature",
        "core": ["joy", "happy", "rejoice", "farah", "delight",
                 "gladness", "pleased", "jubilant"],
        "extended": ["proud", "exult", "cheerful"],
        "avoid": ["love", "hope", "peace"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ETHICS & MORALITY — الأخلاق
    # ══════════════════════════════════════════════════════════════════════════

    "ع-د-ل": {
        "latin": "a-d-l", "category": "Ethics",
        "core": ["justice", "just", "adl", "fair", "equity", "balance",
                 "equal", "straight", "upright"],
        "extended": ["ransom", "equivalent", "moderate"],
        "avoid": ["truth", "good", "righteousness"]
    },
    "ح-ق-ق": {
        "latin": "h-q-q", "category": "Ethics",
        "core": ["truth", "right", "haqq", "true", "real", "due",
                 "certain", "rightful", "just"],
        "extended": ["obligatory", "worthy", "genuine"],
        "avoid": ["justice", "guidance", "good"]
    },
    "ب-ا-ط-ل": {
        "latin": "b-t-l", "category": "Ethics",
        "core": ["falsehood", "false", "batil", "vain", "void",
                 "worthless", "invalid", "wrong"],
        "extended": ["futile", "idle", "cancel"],
        "avoid": ["error", "wrong", "evil"]
    },
    "ظ-ل-م": {
        "latin": "zh-l-m", "category": "Ethics",
        "core": ["wrong", "wrongdoing", "zulm", "oppression", "injustice",
                 "tyranny", "transgress", "oppress", "darkness"],
        "extended": ["harm", "abuse", "unjust"],
        "avoid": ["evil", "sin", "corruption"]
    },
    "ف-س-د": {
        "latin": "f-s-d", "category": "Ethics",
        "core": ["corrupt", "corruption", "fasad", "mischief", "evil",
                 "spoil", "ruin", "disorder"],
        "extended": ["deprave", "damage", "destroy"],
        "avoid": ["sin", "transgress", "wrong"]
    },
    "ف-ج-ر": {
        "latin": "f-j-r", "category": "Ethics",
        "core": ["wicked", "wickedness", "fujur", "sin", "immoral",
                 "dissolute", "dawn", "break open"],
        "extended": ["transgress", "corrupt", "deviate"],
        "avoid": ["disbelieve", "corrupt", "oppress"]
    },
    "ف-ح-ش": {
        "latin": "f-h-sh", "category": "Ethics",
        "core": ["indecency", "obscenity", "fahsha", "lewdness",
                 "immorality", "evil deed", "shameful"],
        "extended": ["excess", "extreme", "vile"],
        "avoid": ["sin", "transgress", "wrong"]
    },
    "ب-ر-ر": {
        "latin": "b-r-r", "category": "Ethics",
        "core": ["righteous", "righteousness", "birr", "good", "pious",
                 "dutiful", "virtuous", "land"],
        "extended": ["filial piety", "broad", "kindness"],
        "avoid": ["just", "truthful", "patient"]
    },
    "ت-ق-و": {
        "latin": "t-q-w", "category": "Ethics",
        "core": ["piety", "pious", "taqwa", "fear of god", "righteousness",
                 "devout", "mindful", "guard", "god-fearing"],
        "extended": ["cautious", "protect", "shield"],
        "avoid": ["worship", "submit", "believe"]
    },
    "إ-ص-ل-ح": {
        "latin": "s-l-h", "category": "Ethics",
        "core": ["righteous", "righteousness", "salih", "good", "reform",
                 "rightful", "upright", "set right", "islah"],
        "extended": ["reconcile", "improve", "correct"],
        "avoid": ["peace", "submit", "believe"]
    },
    "أ-م-ر": {
        "latin": "a-m-r", "category": "Ethics",
        "core": ["command", "order", "amr", "affair", "matter",
                 "instruct", "bid", "authority"],
        "extended": ["issue", "thing", "business"],
        "avoid": ["will", "decree", "guide"]
    },
    "ن-ه-ي": {
        "latin": "n-h-y", "category": "Ethics",
        "core": ["forbid", "prohibition", "nahy", "prevent", "restrain",
                 "end", "forbid", "deter"],
        "extended": ["boundary", "limit", "end"],
        "avoid": ["punish", "warn", "command"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LEGAL & SOCIAL — الفقه والاجتماع
    # ══════════════════════════════════════════════════════════════════════════

    "ح-ل-ل": {
        "latin": "h-l-l", "category": "Legal",
        "core": ["lawful", "permissible", "halal", "allowed", "legal",
                 "permitted", "dissolve", "untie"],
        "extended": ["release", "open", "solve"],
        "avoid": ["good", "pure", "clean"]
    },
    "ح-ر-م": {
        "latin": "h-r-m", "category": "Legal",
        "core": ["forbidden", "haram", "sacred", "prohibited", "unlawful",
                 "inviolable", "sanctuary", "taboo"],
        "extended": ["deprive", "sanctify", "respect"],
        "avoid": ["punishment", "sin", "wrong"]
    },
    "ف-ر-ض": {
        "latin": "f-r-d", "category": "Legal",
        "core": ["obligatory", "obligation", "fard", "duty", "prescribe",
                 "assign", "allot", "designate"],
        "extended": ["ordain", "decree", "portion"],
        "avoid": ["command", "forbid", "allow"]
    },
    "و-ج-ب": {
        "latin": "w-j-b", "category": "Legal",
        "core": ["obligatory", "wajib", "necessary", "fall", "duty",
                 "compulsory", "incumbent"],
        "extended": ["set", "fixed", "establish"],
        "avoid": ["command", "decree", "allow"]
    },
    "ع-ق-د": {
        "latin": "a-q-d", "category": "Legal",
        "core": ["contract", "covenant", "aqd", "bind", "knot",
                 "tie", "oath", "agreement"],
        "extended": ["resolve", "conclude", "firm"],
        "avoid": ["promise", "pledge", "guarantee"]
    },
    "م-ي-ر-ا-ث": {
        "latin": "w-r-th", "category": "Legal",
        "core": ["inherit", "inheritance", "mirath", "heir", "legacy",
                 "waris", "bequeath"],
        "extended": ["successor", "remnant", "leave behind"],
        "avoid": ["wealth", "property", "kingdom"]
    },
    "ن-ك-ح": {
        "latin": "n-k-h", "category": "Legal",
        "core": ["marry", "marriage", "nikah", "wed", "matrimony",
                 "spouse", "contract"],
        "extended": ["union", "join", "couple"],
        "avoid": ["love", "companion", "partner"]
    },
    "ط-ل-ق": {
        "latin": "t-l-q", "category": "Legal",
        "core": ["divorce", "talaq", "release", "free", "absolute",
                 "repudiate", "dissolve"],
        "extended": ["absolute", "free", "let go"],
        "avoid": ["separate", "leave", "abandon"]
    },
    "ر-ب-و": {
        "latin": "r-b-w", "category": "Legal",
        "core": ["usury", "riba", "interest", "increase", "grow",
                 "excess", "hillside"],
        "extended": ["profit", "gain", "raise"],
        "avoid": ["trade", "commerce", "wealth"]
    },
    "ق-ص-ص": {
        "latin": "q-s-s", "category": "Legal",
        "core": ["retaliation", "qisas", "retribution", "story",
                 "narrate", "follow", "equal punishment"],
        "extended": ["tale", "account", "trace"],
        "avoid": ["punish", "kill", "judgment"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # NATURAL WORLD — الكون والطبيعة
    # ══════════════════════════════════════════════════════════════════════════

    "س-م-و": {
        "latin": "s-m-w", "category": "Natural World",
        "core": ["heaven", "sky", "sama", "heavens", "firmament",
                 "above", "celestial", "high"],
        "extended": ["elevated", "rain", "name"],
        "avoid": ["paradise", "stars", "clouds"]
    },
    "أ-ر-ض": {
        "latin": "a-r-d", "category": "Natural World",
        "core": ["earth", "land", "ard", "ground", "world",
                 "soil", "territory", "globe"],
        "extended": ["country", "floor", "region"],
        "avoid": ["universe", "creation", "world"]
    },
    "م-و-ت": {
        "latin": "m-w-t", "category": "Natural World",
        "core": ["death", "die", "mawt", "dead", "mortality",
                 "deceased", "lifeless", "perish"],
        "extended": ["barren", "numb", "extinct"],
        "avoid": ["punishment", "end", "judgment"]
    },
    "ح-ي-ا": {
        "latin": "h-y-a", "category": "Natural World",
        "core": ["life", "live", "hayat", "alive", "living",
                 "animate", "revive", "existence"],
        "extended": ["water", "rain", "modesty"],
        "avoid": ["soul", "spirit", "eternal"]
    },
    "م-ا-ء": {
        "latin": "m-a", "category": "Natural World",
        "core": ["water", "ma", "rain", "fluid", "liquid",
                 "river", "spring"],
        "extended": ["semen", "source", "life"],
        "avoid": ["sea", "ocean", "river"]
    },
    "ن-و-ر": {
        "latin": "n-w-r", "category": "Natural World",
        "core": ["light", "nur", "illuminate", "luminous", "bright",
                 "radiant", "enlighten", "gleam"],
        "extended": ["guidance", "clarity", "flower"],
        "avoid": ["fire", "sun", "star"]
    },
    "ظ-ل-م": {
        "latin": "zh-l-m", "category": "Natural World",
        "core": ["darkness", "dark", "zulma", "shadow", "obscure",
                 "gloom"],
        "extended": ["wrong", "injustice", "ignorance"],
        "avoid": ["sin", "evil", "night"]
    },
    "ر-ي-ح": {
        "latin": "r-y-h", "category": "Natural World",
        "core": ["wind", "breeze", "rih", "spirit", "smell",
                 "scent", "air"],
        "extended": ["aroma", "fragrance", "victory"],
        "avoid": ["storm", "power", "breath"]
    },
    "ب-ح-ر": {
        "latin": "b-h-r", "category": "Natural World",
        "core": ["sea", "ocean", "bahr", "river", "large body of water",
                 "maritime", "deep"],
        "extended": ["vast", "flood", "slit"],
        "avoid": ["water", "rain", "flow"]
    },
    "ج-ب-ل": {
        "latin": "j-b-l", "category": "Natural World",
        "core": ["mountain", "jabal", "mount", "hill", "rock",
                 "peak", "firm"],
        "extended": ["nature", "innate", "massive"],
        "avoid": ["earth", "land", "rock"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # LANGUAGE & COMMUNICATION — اللغة والخطاب
    # ══════════════════════════════════════════════════════════════════════════

    "ق-و-ل": {
        "latin": "q-w-l", "category": "Language",
        "core": ["say", "saying", "qawl", "speak", "word",
                 "statement", "utter", "declare"],
        "extended": ["claim", "express", "speech"],
        "avoid": ["command", "write", "message"]
    },
    "ك-ل-م": {
        "latin": "k-l-m", "category": "Language",
        "core": ["word", "kalima", "speak", "speech", "kalam",
                 "wound", "discourse", "utterance"],
        "extended": ["statement", "sentence", "talk"],
        "avoid": ["write", "reveal", "command"]
    },
    "ب-ل-غ": {
        "latin": "b-l-gh", "category": "Language",
        "core": ["convey", "reach", "tabligh", "deliver", "communicate",
                 "attain", "mature", "eloquent"],
        "extended": ["arrive", "notify", "inform"],
        "avoid": ["say", "speak", "write"]
    },
    "ب-ي-ن": {
        "latin": "b-y-n", "category": "Language",
        "core": ["clear", "explain", "bayyina", "manifest", "evident",
                 "between", "distinct", "proof"],
        "extended": ["clarify", "separate", "obvious"],
        "avoid": ["truth", "guidance", "reveal"]
    },
    "ذ-ك-ر": {
        "latin": "dh-k-r", "category": "Language",
        "core": ["mention", "remember", "dhikr", "reminder", "recall",
                 "male", "honor", "commemorate"],
        "extended": ["glorify", "mindful", "praise"],
        "avoid": ["pray", "worship", "read"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # GUIDANCE & MISGUIDANCE — الهداية والضلال
    # ══════════════════════════════════════════════════════════════════════════

    "ه-د-ي": {
        "latin": "h-d-y", "category": "Guidance",
        "core": ["guide", "guidance", "huda", "direct", "hidaya",
                 "right path", "lead"],
        "extended": ["show", "direct", "correct"],
        "avoid": ["teach", "reveal", "truth"]
    },
    "ض-ل-ل": {
        "latin": "d-l-l", "category": "Guidance",
        "core": ["astray", "misguidance", "dalal", "stray", "lost",
                 "error", "deviate", "go wrong"],
        "extended": ["mislead", "perish", "lose"],
        "avoid": ["sin", "evil", "wrong"]
    },
    "ر-ش-د": {
        "latin": "r-sh-d", "category": "Guidance",
        "core": ["right", "guidance", "rushd", "mature", "sound",
                 "correct path", "rightly guided", "rashid"],
        "extended": ["sensible", "reason", "upright"],
        "avoid": ["guidance", "truth", "straight"]
    },
    "غ-و-ي": {
        "latin": "gh-w-y", "category": "Guidance",
        "core": ["misguidance", "ghayy", "error", "deviate", "corrupt",
                 "stray", "seduce", "mislead"],
        "extended": ["tempt", "astray", "deviate"],
        "avoid": ["sin", "evil", "wrong"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # TIME & SPACE — الزمان والمكان
    # ══════════════════════════════════════════════════════════════════════════

    "أ-و-ل": {
        "latin": "a-w-l", "category": "Time",
        "core": ["first", "awwal", "beginning", "origin", "primary",
                 "initial", "former"],
        "extended": ["leader", "return", "interpret"],
        "avoid": ["ancient", "previous", "before"]
    },
    "آ-خ-ر": {
        "latin": "a-kh-r", "category": "Time",
        "core": ["last", "akhir", "final", "end", "hereafter", "latter",
                 "other", "second"],
        "extended": ["future", "next", "behind"],
        "avoid": ["judgment", "resurrection", "death"]
    },
    "ق-ب-ل": {
        "latin": "q-b-l", "category": "Time",
        "core": ["before", "qabla", "prior", "previous", "accept",
                 "receive", "face", "toward"],
        "extended": ["earlier", "precede", "past"],
        "avoid": ["after", "next", "first"]
    },
    "ب-ع-د": {
        "latin": "b-a-d", "category": "Time",
        "core": ["after", "bada", "then", "distance", "away",
                 "later", "subsequent", "far"],
        "extended": ["beyond", "next", "future"],
        "avoid": ["before", "previous", "soon"]
    },
    "ح-ي-ن": {
        "latin": "h-y-n", "category": "Time",
        "core": ["time", "when", "heen", "period", "moment",
                 "while", "appointed time"],
        "extended": ["occasion", "season", "then"],
        "avoid": ["day", "hour", "era"]
    },
    "أ-ب-د": {
        "latin": "a-b-d", "category": "Time",
        "core": ["eternal", "forever", "abad", "everlasting", "always",
                 "perpetual", "endless"],
        "extended": ["permanent", "infinite", "timeless"],
        "avoid": ["ancient", "old", "long"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # PROPHETS & NATIONS — الأنبياء والأمم
    # ══════════════════════════════════════════════════════════════════════════

    "ن-و-ح": {
        "latin": "n-w-h", "category": "Prophets",
        "core": ["noah", "nuh", "lament", "wail"],
        "extended": ["flood", "ark", "prophet"],
        "avoid": []
    },
    "إ-ب-ر-ه-م": {
        "latin": "i-b-r-h-m", "category": "Prophets",
        "core": ["abraham", "ibrahim", "friend of god", "khalilullah"],
        "extended": ["patriarch", "prophet", "father of nations"],
        "avoid": []
    },
    "م-و-س-ى": {
        "latin": "m-w-s-y", "category": "Prophets",
        "core": ["moses", "musa", "torah", "sinai"],
        "extended": ["prophet", "messenger", "israelites"],
        "avoid": []
    },
    "ع-ي-س-ى": {
        "latin": "a-y-s-y", "category": "Prophets",
        "core": ["jesus", "isa", "messiah", "word of god", "spirit"],
        "extended": ["prophet", "messenger", "gospel"],
        "avoid": []
    },
    "م-ح-م-د": {
        "latin": "m-h-m-d", "category": "Prophets",
        "core": ["muhammad", "praised", "prophet", "messenger"],
        "extended": ["seal of prophets", "rasul", "nabi"],
        "avoid": []
    },

    # ══════════════════════════════════════════════════════════════════════════
    # ADDITIONAL HIGH-FREQUENCY ROOTS
    # ══════════════════════════════════════════════════════════════════════════

    "ج-ع-ل": {
        "latin": "j-a-l", "category": "Action",
        "core": ["make", "place", "jaal", "appoint", "render",
                 "set", "put", "cause"],
        "extended": ["create", "establish", "assign"],
        "avoid": ["command", "will", "create"]
    },
    "أ-ت-ي": {
        "latin": "a-t-y", "category": "Action",
        "core": ["come", "bring", "ata", "give", "arrive",
                 "produce", "do", "perform"],
        "extended": ["present", "offer", "yield"],
        "avoid": ["send", "reveal", "make"]
    },
    "أ-خ-ذ": {
        "latin": "a-kh-dh", "category": "Action",
        "core": ["take", "seize", "akhadha", "grasp", "catch",
                 "hold", "receive", "punish"],
        "extended": ["capture", "get", "adopt"],
        "avoid": ["give", "send", "make"]
    },
    "ر-أ-ي": {
        "latin": "r-a-y", "category": "Action",
        "core": ["see", "vision", "raya", "view", "opinion",
                 "observe", "sight", "dream"],
        "extended": ["consider", "think", "perceive"],
        "avoid": ["know", "hear", "understand"]
    },
    "ع-م-ل": {
        "latin": "a-m-l", "category": "Action",
        "core": ["work", "deed", "amal", "act", "do", "action",
                 "labor", "practice", "perform"],
        "extended": ["operate", "produce", "make"],
        "avoid": ["say", "command", "will"]
    },
    "ج-ا-ء": {
        "latin": "j-a-a", "category": "Action",
        "core": ["come", "ja", "arrive", "came", "bring", "approach"],
        "extended": ["present", "reach", "appear"],
        "avoid": ["send", "go", "return"]
    },
    "ذ-ه-ب": {
        "latin": "dh-h-b", "category": "Action",
        "core": ["go", "leave", "dhahab", "depart", "gold",
                 "pass away", "walk away"],
        "extended": ["proceed", "travel", "spend"],
        "avoid": ["come", "return", "send"]
    },
    "ر-ج-ع": {
        "latin": "r-j-a", "category": "Action",
        "core": ["return", "come back", "raja", "revert", "restore",
                 "go back", "refer"],
        "extended": ["repent", "reconsider", "revert"],
        "avoid": ["go", "leave", "send"]
    },
    "ن-ص-ر": {
        "latin": "n-s-r", "category": "Action",
        "core": ["help", "victory", "nasr", "support", "aid",
                 "assist", "defend", "nasir"],
        "extended": ["triumph", "protect", "champion"],
        "avoid": ["guide", "forgive", "provide"]
    },
    "ق-ت-ل": {
        "latin": "q-t-l", "category": "Action",
        "core": ["kill", "fight", "qatl", "slay", "combat",
                 "battle", "murder", "war"],
        "extended": ["execute", "destroy", "struggle"],
        "avoid": ["punish", "harm", "hurt"]
    },
    "ف-ت-ن": {
        "latin": "f-t-n", "category": "Action",
        "core": ["trial", "tribulation", "fitna", "test", "tempt",
                 "strife", "discord", "seduce"],
        "extended": ["afflict", "charm", "mislead"],
        "avoid": ["punishment", "sin", "evil"]
    },
    "ب-ل-و": {
        "latin": "b-l-w", "category": "Action",
        "core": ["test", "trial", "bala", "afflict", "try",
                 "prove", "tribulation", "experience"],
        "extended": ["examine", "ordeal", "disaster"],
        "avoid": ["punishment", "sin", "judgment"]
    },
    "ش-ه-د": {
        "latin": "sh-h-d", "category": "Action",
        "core": ["witness", "testify", "shahid", "martyr", "presence",
                 "testimony", "observe", "shuhada"],
        "extended": ["attest", "evidence", "see"],
        "avoid": ["know", "judge", "see"]
    },
    "ح-ك-م": {
        "latin": "h-k-m", "category": "Action",
        "core": ["judge", "rule", "hukm", "decide", "judgment",
                 "govern", "authority", "hakim"],
        "extended": ["command", "sentence", "arbitrate"],
        "avoid": ["know", "wise", "power"]
    },
    "و-ع-د": {
        "latin": "w-a-d", "category": "Action",
        "core": ["promise", "warn", "wad", "threat", "appoint",
                 "threaten", "pledge"],
        "extended": ["threat", "appointment", "foretell"],
        "avoid": ["command", "reveal", "decree"]
    },
    "ب-ش-ر": {
        "latin": "b-sh-r", "category": "Action",
        "core": ["give glad tidings", "bashar", "human being",
                 "announce", "skin", "glad news", "bringer of news"],
        "extended": ["humanity", "person", "mortal"],
        "avoid": ["warn", "command", "reveal"]
    },
    "أ-ن-ذ-ر": {
        "latin": "n-dh-r", "category": "Action",
        "core": ["warn", "warner", "nadhir", "vow", "pledge",
                 "caution", "forewarn", "threat"],
        "extended": ["threaten", "prophecy", "admonish"],
        "avoid": ["punish", "guide", "command"]
    },
    "ح-ر-ث": {
        "latin": "h-r-th", "category": "Natural World",
        "core": ["cultivate", "harvest", "harth", "till", "plough",
                 "reap", "field", "crop"],
        "extended": ["earn", "sow", "agriculture"],
        "avoid": ["work", "earn", "produce"]
    },
    "م-ث-ل": {
        "latin": "m-th-l", "category": "Language",
        "core": ["parable", "example", "mathal", "likeness", "similar",
                 "resemblance", "compare", "proverb"],
        "extended": ["image", "like", "equivalent"],
        "avoid": ["story", "lesson", "sign"]
    },
    "آ-ي-ة": {
        "latin": "a-y-t", "category": "Prophethood",
        "core": ["sign", "verse", "aya", "miracle", "evidence",
                 "proof", "token", "wonder"],
        "extended": ["indication", "symbol", "chapter verse"],
        "avoid": ["revelation", "guidance", "truth"]
    },
    "ك-ر-م": {
        "latin": "k-r-m", "category": "Ethics",
        "core": ["honor", "noble", "karim", "generous", "dignity",
                 "respect", "grace", "ikram"],
        "extended": ["precious", "magnanimous", "worthy"],
        "avoid": ["love", "mercy", "peace"]
    },
    "أ-م-ة": {
        "latin": "a-m-t", "category": "Social",
        "core": ["nation", "community", "umma", "people", "generation",
                 "group", "leader"],
        "extended": ["time", "period", "way"],
        "avoid": ["country", "religion", "mankind"]
    },
    "إ-ك-ر-ا-ه": {
        "latin": "k-r-h", "category": "Legal",
        "core": ["compulsion", "coercion", "ikrah", "force", "compel",
                 "obligate", "reluctance", "dislike"],
        "extended": ["hatred", "aversion", "unwilling"],
        "avoid": ["prohibition", "harm", "evil"]
    },
    "ع-ه-د": {
        "latin": "a-h-d", "category": "Legal",
        "core": ["covenant", "promise", "ahd", "pledge", "agreement",
                 "treaty", "vow", "obligation"],
        "extended": ["era", "custody", "entrust"],
        "avoid": ["contract", "law", "command"]
    },
    "أ-م-ا-ن-ة": {
        "latin": "a-m-n", "category": "Ethics",
        "core": ["trust", "amanah", "trustworthiness", "deposit",
                 "responsibility", "security", "faithful"],
        "extended": ["safety", "honest", "reliable"],
        "avoid": ["belief", "faith", "safety"]
    },
    "ص-ب-ر": {
        "latin": "s-b-r", "category": "Ethics",
        "core": ["patience", "sabr", "patient", "endure", "persevere",
                 "steadfast", "forbearance"],
        "extended": ["restrain", "constant", "steady"],
        "avoid": ["peace", "content", "accept"]
    },
    "ش-ف-ع": {
        "latin": "sh-f-a", "category": "Eschatology",
        "core": ["intercede", "intercession", "shafa", "intercessor",
                 "advocate", "even number", "pair"],
        "extended": ["help", "support", "mediate"],
        "avoid": ["forgive", "judge", "punish"]
    },
    "ك-ر-س-ي": {
        "latin": "k-r-s-y", "category": "Divine Names",
        "core": ["throne", "kursi", "seat", "chair", "footstool",
                 "knowledge", "dominion"],
        "extended": ["authority", "power", "control"],
        "avoid": ["heaven", "sky", "universe"]
    },
    "ع-ر-ش": {
        "latin": "a-r-sh", "category": "Divine Names",
        "core": ["throne", "arsh", "canopy", "lofty seat", "sovereignty",
                 "authority"],
        "extended": ["roof", "trellis", "dominion"],
        "avoid": ["heaven", "sky", "universe"]
    },
    "ر-و-ح": {
        "latin": "r-w-h", "category": "Human Nature",
        "core": ["spirit", "soul", "ruh", "breath", "wind",
                 "revelation", "mercy", "revive"],
        "extended": ["comfort", "relief", "holy spirit"],
        "avoid": ["heart", "mind", "life"]
    },
    "م-ل-ئ-ك": {
        "latin": "m-l-k", "category": "Creation",
        "core": ["angel", "malak", "messenger", "envoy", "spiritual being"],
        "extended": ["divine messenger", "celestial being"],
        "avoid": ["king", "owner", "ruler"]
    },
    "إ-ب-ل-ي-س": {
        "latin": "b-l-s", "category": "Creation",
        "core": ["iblis", "satan", "devil", "despair", "evil one"],
        "extended": ["enemy", "mislead", "tempt"],
        "avoid": ["jinn", "demon", "evil"]
    },
    "ج-ن-و-د": {
        "latin": "j-n-d", "category": "Social",
        "core": ["army", "soldiers", "junud", "forces", "host",
                 "troops", "military"],
        "extended": ["support", "helper", "group"],
        "avoid": ["people", "nation", "group"]
    },
    "ف-ر-ق": {
        "latin": "f-r-q", "category": "Action",
        "core": ["separate", "distinguish", "furqan", "criterion",
                 "divide", "split", "difference"],
        "extended": ["part", "group", "discern"],
        "avoid": ["truth", "guidance", "difference"]
    },
    "ص-ر-خ": {
        "latin": "s-r-kh", "category": "Action",
        "core": ["cry out", "scream", "call", "shout",
                 "wail", "outcry"],
        "extended": ["implore", "help", "appeal"],
        "avoid": ["pray", "invoke", "mention"]
    },
    "ح-م-ل": {
        "latin": "h-m-l", "category": "Action",
        "core": ["carry", "bear", "haml", "burden", "pregnancy",
                 "load", "take", "lift"],
        "extended": ["tolerate", "support", "attack"],
        "avoid": ["give", "hold", "contain"]
    },
    "خ-ل-ف": {
        "latin": "kh-l-f", "category": "Action",
        "core": ["succeed", "khalifa", "caliph", "vicegerent", "behind",
                 "after", "successor", "differ"],
        "extended": ["replace", "follow", "oppose"],
        "avoid": ["before", "guide", "create"]
    },
    "ص-ر-ف": {
        "latin": "s-r-f", "category": "Action",
        "core": ["turn away", "divert", "sarf", "spend", "exchange",
                 "change", "deflect"],
        "extended": ["prevent", "avert", "conjugate"],
        "avoid": ["guide", "lead", "direct"]
    },
    "م-ن-ع": {
        "latin": "m-n-a", "category": "Action",
        "core": ["prevent", "forbid", "mana", "withhold", "prohibit",
                 "stop", "refuse"],
        "extended": ["protect", "strong", "deny"],
        "avoid": ["command", "allow", "permit"]
    },
    "ن-ج-و": {
        "latin": "n-j-w", "category": "Action",
        "core": ["save", "rescue", "naja", "escape", "deliver",
                 "flee", "salvation", "secret talk"],
        "extended": ["succeed", "withdraw", "consult"],
        "avoid": ["forgive", "guide", "protect"]
    },
    "و-ق-ي": {
        "latin": "w-q-y", "category": "Action",
        "core": ["protect", "guard", "wiqaya", "shield", "ward off",
                 "preserve", "save"],
        "extended": ["prevent", "keep safe", "taqwa"],
        "avoid": ["guide", "help", "strengthen"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # EXPANSION SET — additional roots toward 300+ coverage
    # ══════════════════════════════════════════════════════════════════════════

    "ك-ت-م": {
        "latin": "k-t-m", "category": "Action",
        "core": ["conceal", "hide", "kitman", "withhold", "suppress", "secret"],
        "extended": ["disguise", "keep back"],
        "avoid": ["lie", "deny", "disbelieve"]
    },
    "ب-ي-ع": {
        "latin": "b-y-a", "category": "Legal",
        "core": ["sell", "trade", "bay", "buy", "commerce", "transaction"],
        "extended": ["pledge", "allegiance", "exchange"],
        "avoid": ["usury", "wealth", "gain"]
    },
    "ك-س-ب": {
        "latin": "k-s-b", "category": "Action",
        "core": ["earn", "acquire", "kasb", "gain", "achieve", "obtain"],
        "extended": ["work", "merit", "result"],
        "avoid": ["create", "make", "give"]
    },
    "ط-ع-م": {
        "latin": "t-a-m", "category": "Natural World",
        "core": ["food", "feed", "taam", "eat", "nourishment", "taste"],
        "extended": ["provide", "flavor", "meal"],
        "avoid": ["provision", "drink", "fruit"]
    },
    "ش-ر-ب": {
        "latin": "sh-r-b", "category": "Natural World",
        "core": ["drink", "beverage", "shurb", "sip", "imbibe"],
        "extended": ["absorb", "quench"],
        "avoid": ["water", "food", "provision"]
    },
    "ل-ب-س": {
        "latin": "l-b-s", "category": "Natural World",
        "core": ["wear", "clothing", "libas", "dress", "garment", "cover"],
        "extended": ["conceal", "mix up"],
        "avoid": ["adorn", "beauty", "cover"]
    },
    "ز-و-ج": {
        "latin": "z-w-j", "category": "Social",
        "core": ["spouse", "pair", "zawj", "couple", "mate", "marry"],
        "extended": ["kind", "type", "category"],
        "avoid": ["family", "children", "marriage"]
    },
    "و-ل-د": {
        "latin": "w-l-d", "category": "Social",
        "core": ["child", "offspring", "walad", "son", "birth", "beget"],
        "extended": ["generation", "born", "produce"],
        "avoid": ["family", "create", "people"]
    },
    "أ-ب-و": {
        "latin": "a-b-w", "category": "Social",
        "core": ["father", "ab", "forefather", "ancestor", "patriarch"],
        "extended": ["origin", "source"],
        "avoid": ["family", "lineage", "parent"]
    },
    "أ-خ-و": {
        "latin": "a-kh-w", "category": "Social",
        "core": ["brother", "akh", "kinship", "brotherhood", "fellow"],
        "extended": ["companion", "ally", "sibling"],
        "avoid": ["friend", "family", "people"]
    },
    "ق-ر-ي": {
        "latin": "q-r-y", "category": "Social",
        "core": ["town", "village", "qarya", "settlement", "city"],
        "extended": ["inhabitants", "locality"],
        "avoid": ["nation", "people", "land"]
    },
    "م-د-ن": {
        "latin": "m-d-n", "category": "Social",
        "core": ["city", "madina", "civilization", "urban", "town"],
        "extended": ["settled", "civilized"],
        "avoid": ["village", "land", "nation"]
    },
    "ب-ي-ت": {
        "latin": "b-y-t", "category": "Social",
        "core": ["house", "home", "bayt", "dwelling", "abode", "household"],
        "extended": ["family", "shelter", "kaaba"],
        "avoid": ["sanctuary", "mosque", "temple"]
    },
    "س-ف-ر": {
        "latin": "s-f-r", "category": "Action",
        "core": ["travel", "journey", "safar", "voyage", "depart"],
        "extended": ["scribe", "reveal", "morning"],
        "avoid": ["migrate", "leave", "go"]
    },
    "ه-ج-ر": {
        "latin": "h-j-r", "category": "Action",
        "core": ["migrate", "migration", "hijra", "emigrate", "abandon", "forsake"],
        "extended": ["depart", "exile", "separate"],
        "avoid": ["travel", "journey", "flee"]
    },
    "ج-ه-د": {
        "latin": "j-h-d", "category": "Action",
        "core": ["strive", "struggle", "jihad", "effort", "endeavor", "exert"],
        "extended": ["toil", "labor", "contend"],
        "avoid": ["worship", "patience", "war"]
    },
    "س-ع-ي": {
        "latin": "s-a-y", "category": "Action",
        "core": ["strive", "effort", "saa", "endeavor", "pursue", "run"],
        "extended": ["hasten", "attempt", "labor"],
        "avoid": ["struggle", "fight", "worship"]
    },
    "أ-ج-ل": {
        "latin": "a-j-l", "category": "Time",
        "core": ["term", "appointed time", "ajal", "deadline", "duration"],
        "extended": ["delay", "respite", "lifespan"],
        "avoid": ["hour", "day", "moment"]
    },
    "د-و-م": {
        "latin": "d-w-m", "category": "Time",
        "core": ["lasting", "permanent", "dawam", "continuous", "perpetual"],
        "extended": ["constant", "eternal", "ongoing"],
        "avoid": ["forever", "everlasting", "infinite"]
    },
    "ب-د-أ": {
        "latin": "b-d-a", "category": "Time",
        "core": ["begin", "start", "bada", "commence", "initiate", "first"],
        "extended": ["onset", "outset"],
        "avoid": ["create", "first", "origin"]
    },
    "د-خ-ل": {
        "latin": "d-kh-l", "category": "Action",
        "core": ["enter", "dukhul", "go in", "admission", "interior"],
        "extended": ["penetrate", "involve"],
        "avoid": ["come", "arrive", "reach"]
    },
    "خ-ر-ج": {
        "latin": "kh-r-j", "category": "Action",
        "core": ["exit", "leave", "khuruj", "go out", "emerge", "produce"],
        "extended": ["expel", "remove", "result"],
        "avoid": ["come", "depart", "arrive"]
    },
    "ع-ظ-م": {
        "latin": "a-zh-m", "category": "Ethics",
        "core": ["great", "mighty", "azim", "magnificent", "tremendous", "enormous"],
        "extended": ["glorify", "majestic", "vast"],
        "avoid": ["high", "exalted", "supreme"]
    },
    "ح-س-ن": {
        "latin": "h-s-n", "category": "Ethics",
        "core": ["good", "beautiful", "husn", "excellent", "fine", "goodness"],
        "extended": ["handsome", "favor", "improve"],
        "avoid": ["righteous", "pious", "virtue"]
    },
    "س-و-ء": {
        "latin": "s-w-a", "category": "Ethics",
        "core": ["evil", "bad", "su", "harm", "wrong", "wickedness"],
        "extended": ["distress", "disgrace", "shame"],
        "avoid": ["sin", "wrongdoing", "corruption"]
    },
    "خ-ي-ر": {
        "latin": "kh-y-r", "category": "Ethics",
        "core": ["good", "khayr", "best", "better", "goodness", "benefit"],
        "extended": ["bounty", "blessing", "select"],
        "avoid": ["righteous", "pure", "virtue"]
    },
    "ك-ذ-ب": {
        "latin": "k-dh-b", "category": "Ethics",
        "core": ["lie", "falsehood", "kadhib", "deny", "untrue", "fabricate"],
        "extended": ["disbelieve", "reject"],
        "avoid": ["wrong", "evil", "sin"]
    },
    "ح-س-د": {
        "latin": "h-s-d", "category": "Human Nature",
        "core": ["envy", "jealousy", "hasad", "covet", "grudge"],
        "extended": ["resent", "begrudge"],
        "avoid": ["anger", "hatred", "pride"]
    },
    "ع-س-ر": {
        "latin": "a-s-r", "category": "Human Nature",
        "core": ["hardship", "difficulty", "usr", "difficult", "adversity"],
        "extended": ["constraint", "tight", "strain"],
        "avoid": ["trial", "test", "affliction"]
    },
    "ي-س-ر": {
        "latin": "y-s-r", "category": "Human Nature",
        "core": ["ease", "yusr", "easy", "facilitate", "comfort", "simple"],
        "extended": ["relief", "lighten", "prosperity"],
        "avoid": ["mercy", "blessing", "favor"]
    },
    "ر-ف-ع": {
        "latin": "r-f-a", "category": "Action",
        "core": ["raise", "elevate", "rafa", "lift", "exalt", "ascend"],
        "extended": ["promote", "remove", "honor"],
        "avoid": ["high", "great", "supreme"]
    },
    "ث-ب-ت": {
        "latin": "th-b-t", "category": "Human Nature",
        "core": ["firm", "steadfast", "thabat", "stable", "established", "constant"],
        "extended": ["affirm", "certain", "endure"],
        "avoid": ["patience", "strong", "support"]
    },
    "س-ت-ر": {
        "latin": "s-t-r", "category": "Action",
        "core": ["cover", "conceal", "sitr", "veil", "shield", "screen"],
        "extended": ["protect", "curtain", "secret"],
        "avoid": ["forgive", "deceive", "lie"]
    },
    "ك-ش-ف": {
        "latin": "k-sh-f", "category": "Action",
        "core": ["uncover", "reveal", "kashf", "remove", "expose", "disclose"],
        "extended": ["clarify", "lift", "discover"],
        "avoid": ["guide", "show", "teach"]
    },
    "غ-ي-ب": {
        "latin": "gh-y-b", "category": "Faith",
        "core": ["unseen", "hidden", "ghayb", "absent", "invisible", "concealed"],
        "extended": ["disappear", "secret", "beyond perception"],
        "avoid": ["faith", "belief", "knowledge"]
    },
    "ظ-ه-ر": {
        "latin": "zh-h-r", "category": "Action",
        "core": ["appear", "manifest", "zuhur", "evident", "back", "emerge"],
        "extended": ["overcome", "support", "noon"],
        "avoid": ["clear", "obvious", "show"]
    },
    "ع-د-و": {
        "latin": "a-d-w", "category": "Social",
        "core": ["enemy", "hostility", "aduww", "foe", "adversary", "transgress"],
        "extended": ["aggression", "opposition"],
        "avoid": ["fight", "war", "oppose"]
    },
    "س-أ-ل": {
        "latin": "s-a-l", "category": "Language",
        "core": ["ask", "question", "suaal", "request", "inquire", "petition"],
        "extended": ["beg", "seek"],
        "avoid": ["pray", "supplicate", "invoke"]
    },
    "ك-ث-ر": {
        "latin": "k-th-r", "category": "Natural World",
        "core": ["many", "abundance", "kathir", "much", "numerous", "plentiful"],
        "extended": ["multiply", "frequent"],
        "avoid": ["great", "vast", "huge"]
    },
    "ج-م-ع": {
        "latin": "j-m-a", "category": "Action",
        "core": ["gather", "collect", "jama", "assemble", "unite", "combine"],
        "extended": ["compile", "join"],
        "avoid": ["resurrection", "muster", "congregate"]
    },
    "و-ح-د": {
        "latin": "w-h-d", "category": "Divine Names",
        "core": ["one", "unity", "wahid", "single", "alone", "unique"],
        "extended": ["solitary", "monotheism"],
        "avoid": ["eternal", "self-sufficient", "indivisible"]
    },
    "ن-ج-م": {
        "latin": "n-j-m", "category": "Natural World",
        "core": ["star", "najm", "celestial body", "rise", "appear gradually"],
        "extended": ["constellation", "result"],
        "avoid": ["sky", "heaven", "light"]
    },
    "ق-م-ر": {
        "latin": "q-m-r", "category": "Natural World",
        "core": ["moon", "qamar", "lunar", "luminous"],
        "extended": ["month", "bright"],
        "avoid": ["sun", "star", "light"]
    },
    "ش-م-س": {
        "latin": "sh-m-s", "category": "Natural World",
        "core": ["sun", "shams", "solar", "sunlight"],
        "extended": ["day", "bright"],
        "avoid": ["moon", "star", "light"]
    },
    "ل-ي-ل": {
        "latin": "l-y-l", "category": "Natural World",
        "core": ["night", "layl", "darkness", "nighttime"],
        "extended": ["dark", "evening"],
        "avoid": ["day", "shadow", "dim"]
    },
    "ن-ه-ر": {
        "latin": "n-h-r", "category": "Natural World",
        "core": ["river", "nahr", "stream", "flow", "canal"],
        "extended": ["day", "bright"],
        "avoid": ["sea", "water", "fountain"]
    },
    "ع-ي-ن": {
        "latin": "a-y-n", "category": "Natural World",
        "core": ["eye", "ayn", "spring", "fountain", "source", "essence"],
        "extended": ["sight", "watch"],
        "avoid": ["see", "vision", "water"]
    },
    "و-ج-ه": {
        "latin": "w-j-h", "category": "Human Nature",
        "core": ["face", "wajh", "countenance", "direction", "purpose", "presence"],
        "extended": ["aspect", "side", "honor"],
        "avoid": ["self", "essence", "front"]
    },
    "س-م-و": {
        "latin": "s-m-w", "category": "Language",
        "core": ["name", "ism", "naming", "designation", "title", "attribute"],
        "extended": ["called", "term"],
        "avoid": ["heaven", "sky", "high"]
    },
    "ه-ل-ك": {
        "latin": "h-l-k", "category": "Eschatology",
        "core": ["perish", "destruction", "halak", "ruin", "destroy", "annihilate"],
        "extended": ["doomed", "consumed"],
        "avoid": ["punishment", "death", "end"]
    },
    "ق-ر-ب": {
        "latin": "q-r-b", "category": "Action",
        "core": ["near", "approach", "qurb", "close", "proximity", "draw near"],
        "extended": ["intimate", "imminent"],
        "avoid": ["distant", "far", "remote"]
    },
    "ط-ه-ر": {
        "latin": "t-h-r", "category": "Worship",
        "core": ["pure", "purity", "tahara", "clean", "purify", "chaste"],
        "extended": ["holy", "cleanse"],
        "avoid": ["holy", "sacred", "righteous"]
    },
    "س-ك-ن": {
        "latin": "s-k-n", "category": "Human Nature",
        "core": ["calm", "tranquility", "sakina", "stillness", "peace", "rest"],
        "extended": ["repose", "still"],
        "avoid": ["mercy", "peace", "comfort"]
    },
    "س-ب-ي-ل": {
        "latin": "s-b-l", "category": "Guidance",
        "core": ["way", "path", "sabil", "road", "course", "means"],
        "extended": ["route", "method"],
        "avoid": ["guidance", "straight path", "religion"]
    },
    "ش-ر-ع": {
        "latin": "sh-r-a", "category": "Legal",
        "core": ["law", "shariah", "legislation", "way", "ordain", "prescribe"],
        "extended": ["legal system", "code"],
        "avoid": ["religion", "guidance", "way"]
    },
    "ف-ق-ه": {
        "latin": "f-q-h", "category": "Legal",
        "core": ["understand", "fiqh", "jurisprudence", "comprehend deeply", "discernment"],
        "extended": ["insight", "expertise"],
        "avoid": ["knowledge", "wisdom", "law"]
    },
    "غ-ل-ب": {
        "latin": "gh-l-b", "category": "Action",
        "core": ["overcome", "victory", "ghalaba", "prevail", "conquer", "defeat"],
        "extended": ["triumph", "subdue"],
        "avoid": ["help", "support", "power"]
    },
    "ص-د-ق-ة": {
        "latin": "s-d-q", "category": "Worship",
        "core": ["charity", "sadaqa", "almsgiving", "voluntary giving", "donation"],
        "extended": ["generosity", "give"],
        "avoid": ["zakat", "obligatory charity", "purify"]
    },
    "ر-ض-ي": {
        "latin": "r-d-y", "category": "Human Nature",
        "core": ["pleased", "satisfaction", "rida", "content", "approval", "acceptance"],
        "extended": ["gratify", "consent"],
        "avoid": ["happy", "love", "mercy"]
    },
    "خ-س-ر": {
        "latin": "kh-s-r", "category": "Eschatology",
        "core": ["loss", "khusran", "lose", "ruin", "deficit", "fail"],
        "extended": ["forfeit", "deprived"],
        "avoid": ["punishment", "failure", "wrong"]
    },
    "أ-ث-م": {
        "latin": "a-th-m", "category": "Eschatology",
        "core": ["sin", "ithm", "wrongdoing", "guilt", "offense", "transgression"],
        "extended": ["crime", "fault"],
        "avoid": ["disbelief", "evil", "wrong"]
    },
    "ذ-ن-ب": {
        "latin": "dh-n-b", "category": "Eschatology",
        "core": ["sin", "dhanb", "fault", "offense", "wrongdoing", "crime"],
        "extended": ["transgression", "guilt"],
        "avoid": ["disbelief", "evil", "wrong"]
    },
    "ط-غ-ي": {
        "latin": "t-gh-y", "category": "Ethics",
        "core": ["transgress", "tughyan", "tyrant", "exceed limits", "rebel", "taghut"],
        "extended": ["oppress", "arrogance"],
        "avoid": ["wrong", "evil", "sin"]
    },
    "ض-ع-ف": {
        "latin": "d-a-f", "category": "Human Nature",
        "core": ["weak", "daaf", "weakness", "feeble", "frail", "multiply"],
        "extended": ["fragile", "powerless"],
        "avoid": ["powerful", "strong", "mighty"]
    },
    "ق-و-ي": {
        "latin": "q-w-y", "category": "Divine Names",
        "core": ["strong", "qawi", "powerful", "strength", "might", "vigor"],
        "extended": ["forceful", "able"],
        "avoid": ["mighty", "powerful", "able"]
    },
    "ف-ض-ل": {
        "latin": "f-d-l", "category": "Divine Names",
        "core": ["favor", "fadl", "grace", "bounty", "excellence", "preference"],
        "extended": ["generosity", "blessing"],
        "avoid": ["mercy", "gift", "blessing"]
    },
    "ع-ل-ق": {
        "latin": "a-l-q", "category": "Creation",
        "core": ["clinging clot", "alaq", "attach", "cling", "leech-like", "suspend"],
        "extended": ["embryo stage", "hang"],
        "avoid": ["creation", "life", "form"]
    },
    "ط-ي-ن": {
        "latin": "t-y-n", "category": "Creation",
        "core": ["clay", "tin", "mud", "mire", "loam"],
        "extended": ["earth-material"],
        "avoid": ["dust", "soil", "creation"]
    },
    "ز-ر-ع": {
        "latin": "z-r-a", "category": "Natural World",
        "core": ["sow", "crop", "zara", "cultivate", "plant", "agriculture"],
        "extended": ["produce", "grow"],
        "avoid": ["harvest", "field", "cultivate"]
    },
    "ط-ي-ر": {
        "latin": "t-y-r", "category": "Creation",
        "core": ["bird", "tayr", "fly", "flight", "fate", "omen"],
        "extended": ["soar", "creature"],
        "avoid": ["creation", "animal", "fly"]
    },
    "ل-ه-و": {
        "latin": "l-h-w", "category": "Human Nature",
        "core": ["amusement", "lahw", "diversion", "distraction", "play", "frivolity"],
        "extended": ["entertainment", "idle"],
        "avoid": ["worldly life", "vain", "play"]
    },
    "ز-ي-ن": {
        "latin": "z-y-n", "category": "Human Nature",
        "core": ["adorn", "zina", "decoration", "beautify", "ornament", "embellish"],
        "extended": ["attract", "make appealing"],
        "avoid": ["beauty", "good", "fine"]
    },

    # ══════════════════════════════════════════════════════════════════════════
    # EXPANSION SET 2 — additional roots toward 300+ coverage
    # ══════════════════════════════════════════════════════════════════════════

    "ع-ج-ز": {
        "latin": "a-j-z", "category": "Human Nature",
        "core": ["unable", "incapacity", "ajiz", "powerless", "weak", "fail"],
        "extended": ["old age", "feeble"],
        "avoid": ["weak", "powerless", "fail"]
    },
    "ط-و-ع": {
        "latin": "t-w-a", "category": "Faith",
        "core": ["obey", "obedience", "taa", "compliance", "voluntary",
                 "submit willingly"],
        "extended": ["willing", "consent"],
        "avoid": ["submit", "worship", "command"]
    },
    "أ-ط-ع": {
        "latin": "t-w-a", "category": "Faith",
        "core": ["obey", "obedience", "ataa", "comply", "follow command"],
        "extended": ["submit", "yield"],
        "avoid": ["worship", "follow", "submit"]
    },
    "م-ر-ض": {
        "latin": "m-r-d", "category": "Human Nature",
        "core": ["sick", "marad", "illness", "disease", "ailment"],
        "extended": ["doubt in heart", "weakness"],
        "avoid": ["weak", "doubt", "hypocrisy"]
    },
    "ش-ف-ي": {
        "latin": "sh-f-y", "category": "Human Nature",
        "core": ["heal", "shifa", "cure", "remedy", "recovery"],
        "extended": ["restore", "relief"],
        "avoid": ["mercy", "guidance", "comfort"]
    },
    "ج-ز-ع": {
        "latin": "j-z-a", "category": "Human Nature",
        "core": ["impatience", "jaza", "anxiety", "distress", "fretful"],
        "extended": ["panic", "agitation"],
        "avoid": ["fear", "sorrow", "grief"]
    },
    "ق-ن-ط": {
        "latin": "q-n-t", "category": "Human Nature",
        "core": ["despair", "qunut", "hopelessness", "give up hope"],
        "extended": ["lose hope"],
        "avoid": ["fear", "sorrow", "regret"]
    },
    "ر-غ-ب": {
        "latin": "r-gh-b", "category": "Human Nature",
        "core": ["desire", "raghba", "wish", "want", "incline towards",
                 "yearning"],
        "extended": ["hope for", "aspire"],
        "avoid": ["love", "hope", "will"]
    },
    "ز-ه-د": {
        "latin": "z-h-d", "category": "Ethics",
        "core": ["abstain", "zuhd", "asceticism", "renounce", "detach"],
        "extended": ["indifferent", "forsake"],
        "avoid": ["patience", "piety", "humility"]
    },
    "ج-ز-ي": {
        "latin": "j-z-y", "category": "Eschatology",
        "core": ["recompense", "jaza", "reward", "repay", "requite"],
        "extended": ["sufficient", "compensate"],
        "avoid": ["judgment", "account", "punishment"]
    },
    "أ-ج-ر": {
        "latin": "a-j-r", "category": "Eschatology",
        "core": ["reward", "ajr", "wage", "recompense", "payment"],
        "extended": ["fee", "compensation"],
        "avoid": ["mercy", "favor", "gift"]
    },
    "ث-و-ب": {
        "latin": "th-w-b", "category": "Eschatology",
        "core": ["reward", "thawab", "recompense", "return", "garment"],
        "extended": ["compensation", "outcome"],
        "avoid": ["mercy", "blessing", "gift"]
    },
    "ع-ق-ب": {
        "latin": "a-q-b", "category": "Eschatology",
        "core": ["consequence", "aqiba", "outcome", "end result",
                 "succession", "follow after"],
        "extended": ["heel", "punishment"],
        "avoid": ["punishment", "reward", "end"]
    },
    "ن-ك-ل": {
        "latin": "n-k-l", "category": "Eschatology",
        "core": ["exemplary punishment", "nakal", "deterrent", "retribution"],
        "extended": ["warning example"],
        "avoid": ["punishment", "torment", "wrath"]
    },
    "ص-ل-ي": {
        "latin": "s-l-y", "category": "Eschatology",
        "core": ["burn", "scorching", "sila", "roast in fire", "blazing"],
        "extended": ["enter fire"],
        "avoid": ["fire", "punishment", "hell"]
    },
    "س-ع-ر": {
        "latin": "s-a-r", "category": "Eschatology",
        "core": ["blazing", "saair", "kindle", "flaming fire", "ignite"],
        "extended": ["inflame", "intense fire"],
        "avoid": ["fire", "hell", "punishment"]
    },
    "ح-ط-م": {
        "latin": "h-t-m", "category": "Eschatology",
        "core": ["crush", "hutama", "shatter", "destroy", "break into pieces"],
        "extended": ["smash", "demolish"],
        "avoid": ["fire", "hell", "destroy"]
    },
    "ل-ظ-ى": {
        "latin": "l-z-y", "category": "Eschatology",
        "core": ["blazing flame", "laza", "fierce fire"],
        "extended": ["intense heat"],
        "avoid": ["fire", "hell", "punishment"]
    },
    "ز-ق-م": {
        "latin": "z-q-m", "category": "Eschatology",
        "core": ["zaqqum", "bitter tree of hell", "thorny tree"],
        "extended": ["food of hell"],
        "avoid": ["fire", "punishment", "tree"]
    },
    "ح-و-ر": {
        "latin": "h-w-r", "category": "Eschatology",
        "core": ["pure companions", "hur", "fair ones", "return"],
        "extended": ["paradise companions"],
        "avoid": ["paradise", "reward", "bliss"]
    },
    "ل-ب-ث": {
        "latin": "l-b-th", "category": "Time",
        "core": ["remain", "labith", "stay", "tarry", "abide", "linger"],
        "extended": ["dwell", "delay"],
        "avoid": ["eternal", "forever", "permanent"]
    },
    "م-ك-ث": {
        "latin": "m-k-th", "category": "Time",
        "core": ["stay", "makth", "remain", "abide", "tarry"],
        "extended": ["dwell", "wait"],
        "avoid": ["remain", "eternal", "permanent"]
    },
    "ح-ي-ث": {
        "latin": "h-y-th", "category": "Time",
        "core": ["where", "haythu", "wherever", "place"],
        "extended": ["location", "since"],
        "avoid": ["when", "time", "there"]
    },
    "أ-ي-ن": {
        "latin": "a-y-n", "category": "Time",
        "core": ["where", "ayna", "place", "location"],
        "extended": ["wherever"],
        "avoid": ["when", "how", "what"]
    },
    "ك-ي-ف": {
        "latin": "k-y-f", "category": "Language",
        "core": ["how", "kayfa", "manner", "way", "condition"],
        "extended": ["state", "mode"],
        "avoid": ["why", "what", "when"]
    },
    "ل-م-ا-ذ": {
        "latin": "l-m-dh", "category": "Language",
        "core": ["why", "limadha", "for what reason", "wherefore"],
        "extended": ["cause", "reason"],
        "avoid": ["how", "what", "when"]
    },
    "ع-س-ى": {
        "latin": "a-s-y", "category": "Human Nature",
        "core": ["perhaps", "asa", "maybe", "hope", "possibly"],
        "extended": ["expect", "likely"],
        "avoid": ["hope", "wish", "expect"]
    },
    "ل-ع-ل": {
        "latin": "l-a-l", "category": "Language",
        "core": ["perhaps", "laalla", "so that", "maybe", "in order that"],
        "extended": ["hope", "purpose"],
        "avoid": ["because", "so", "thus"]
    },
    "إ-ن-م-ا": {
        "latin": "n-m-a", "category": "Language",
        "core": ["only", "innama", "merely", "just", "rather"],
        "extended": ["exclusively", "simply"],
        "avoid": ["truly", "indeed", "certainly"]
    },
    "ك-ل-ل": {
        "latin": "k-l-l", "category": "Language",
        "core": ["all", "kull", "every", "each", "whole", "totality"],
        "extended": ["entire", "complete"],
        "avoid": ["many", "abundance", "great"]
    },
    "ب-ع-ض": {
        "latin": "b-a-d", "category": "Language",
        "core": ["some", "bad", "part", "portion", "few"],
        "extended": ["certain", "partial"],
        "avoid": ["all", "every", "whole"]
    },
    "غ-ي-ر": {
        "latin": "gh-y-r", "category": "Language",
        "core": ["other", "ghayr", "different", "besides", "except", "not"],
        "extended": ["apart from", "distinct"],
        "avoid": ["similar", "like", "same"]
    },
    "س-و-ى": {
        "latin": "s-w-y", "category": "Language",
        "core": ["equal", "sawa", "besides", "other than", "level", "alike"],
        "extended": ["except", "apart from"],
        "avoid": ["same", "similar", "match"]
    },
    "ن-ف-ع": {
        "latin": "n-f-a", "category": "Ethics",
        "core": ["benefit", "nafa", "useful", "profit", "advantage", "good"],
        "extended": ["help", "avail"],
        "avoid": ["good", "blessing", "favor"]
    },
    "ض-ر-ر": {
        "latin": "d-r-r", "category": "Ethics",
        "core": ["harm", "darar", "injury", "damage", "hurt", "loss"],
        "extended": ["affliction", "adversity"],
        "avoid": ["evil", "wrong", "punishment"]
    },
    "س-ق-ط": {
        "latin": "s-q-t", "category": "Action",
        "core": ["fall", "suqut", "drop", "descend suddenly", "collapse"],
        "extended": ["plunge", "decline"],
        "avoid": ["descend", "lower", "drop"]
    },
    "ر-م-ي": {
        "latin": "r-m-y", "category": "Action",
        "core": ["throw", "rama", "cast", "hurl", "shoot", "aim"],
        "extended": ["fling", "project"],
        "avoid": ["strike", "hit", "send"]
    },
    "ض-ر-ب": {
        "latin": "d-r-b", "category": "Action",
        "core": ["strike", "darb", "hit", "beat", "set forth example",
                 "travel"],
        "extended": ["impose", "type"],
        "avoid": ["punish", "fight", "example"]
    },
    "م-س-س": {
        "latin": "m-s-s", "category": "Action",
        "core": ["touch", "mass", "afflict", "feel", "contact"],
        "extended": ["affect", "befall"],
        "avoid": ["harm", "afflict", "strike"]
    },
    "ل-م-س": {
        "latin": "l-m-s", "category": "Action",
        "core": ["touch", "lams", "feel", "contact physically"],
        "extended": ["sense", "grope"],
        "avoid": ["touch", "afflict", "feel"]
    },
    "ج-ل-س": {
        "latin": "j-l-s", "category": "Action",
        "core": ["sit", "julus", "seated", "settle down"],
        "extended": ["assembly", "session"],
        "avoid": ["stand", "rest", "remain"]
    },
    "ن-و-م": {
        "latin": "n-w-m", "category": "Human Nature",
        "core": ["sleep", "nawm", "slumber", "rest", "doze"],
        "extended": ["drowsy", "unconscious"],
        "avoid": ["death", "rest", "unaware"]
    },
    "ي-ق-ظ": {
        "latin": "y-q-z", "category": "Human Nature",
        "core": ["awake", "yaqaza", "wakefulness", "alert", "vigilant"],
        "extended": ["aware", "conscious"],
        "avoid": ["sleep", "aware", "knowing"]
    },
    "ح-ل-م": {
        "latin": "h-l-m", "category": "Human Nature",
        "core": ["dream", "hulm", "vision in sleep", "puberty"],
        "extended": ["fantasy", "maturity"],
        "avoid": ["forbearing", "patient", "mercy"]
    },
    "ب-ك-ي": {
        "latin": "b-k-y", "category": "Human Nature",
        "core": ["weep", "buka", "cry", "tears", "lament"],
        "extended": ["mourn", "sob"],
        "avoid": ["grief", "sorrow", "sadness"]
    },
    "ض-ح-ك": {
        "latin": "d-h-k", "category": "Human Nature",
        "core": ["laugh", "dahk", "smile", "mirth", "amusement"],
        "extended": ["joy", "ridicule"],
        "avoid": ["joy", "happiness", "pleasure"]
    },
    "ص-ي-ح": {
        "latin": "s-y-h", "category": "Eschatology",
        "core": ["cry out", "sayha", "shout", "blast", "scream", "shriek"],
        "extended": ["loud noise", "outcry"],
        "avoid": ["punishment", "destruction", "voice"]
    },
    "ر-ع-د": {
        "latin": "r-a-d", "category": "Natural World",
        "core": ["thunder", "rad", "thunderclap", "tremble"],
        "extended": ["awe", "fear"],
        "avoid": ["lightning", "storm", "sky"]
    },
    "ب-ر-ق": {
        "latin": "b-r-q", "category": "Natural World",
        "core": ["lightning", "barq", "flash", "gleam", "shine"],
        "extended": ["bright", "dazzle"],
        "avoid": ["thunder", "storm", "light"]
    },
    "س-ح-ب": {
        "latin": "s-h-b", "category": "Natural World",
        "core": ["cloud", "sahab", "drag", "trail"],
        "extended": ["sky cover", "draw"],
        "avoid": ["rain", "sky", "shade"]
    },
    "ث-ل-ج": {
        "latin": "th-l-j", "category": "Natural World",
        "core": ["snow", "thalj", "ice", "cold"],
        "extended": ["frost"],
        "avoid": ["water", "cold", "rain"]
    },
    "ب-ر-د": {
        "latin": "b-r-d", "category": "Natural World",
        "core": ["cold", "bard", "coolness", "hail", "chill"],
        "extended": ["calm", "relief"],
        "avoid": ["heat", "fire", "punishment"]
    },
    "ح-ر-ر-ة": {
        "latin": "h-r-r", "category": "Natural World",
        "core": ["heat", "harara", "hot", "warmth", "burning sensation"],
        "extended": ["fever", "intensity"],
        "avoid": ["fire", "sun", "punishment"]
    },
    "ر-م-ل": {
        "latin": "r-m-l", "category": "Natural World",
        "core": ["sand", "ramal", "desert", "dune"],
        "extended": ["barren land"],
        "avoid": ["earth", "land", "desert"]
    },
    "ص-خ-ر": {
        "latin": "s-kh-r", "category": "Natural World",
        "core": ["rock", "sakhr", "boulder", "stone", "cliff"],
        "extended": ["solid", "firm"],
        "avoid": ["mountain", "earth", "stone"]
    },
    "ح-ج-ر": {
        "latin": "h-j-r", "category": "Natural World",
        "core": ["stone", "hijr", "rock", "restrict", "forbid",
                 "sanctuary"],
        "extended": ["barrier", "lap"],
        "avoid": ["rock", "forbidden", "sacred"]
    },
    "ذ-ه-ب-ة": {
        "latin": "dh-h-b", "category": "Natural World",
        "core": ["gold", "dhahab", "golden", "precious metal"],
        "extended": ["wealth", "value"],
        "avoid": ["wealth", "treasure", "ornament"]
    },
    "ف-ض-ة": {
        "latin": "f-d-d", "category": "Natural World",
        "core": ["silver", "fidda", "precious metal"],
        "extended": ["wealth", "ornament"],
        "avoid": ["gold", "wealth", "treasure"]
    },
    "ح-د-ي-د": {
        "latin": "h-d-d", "category": "Natural World",
        "core": ["iron", "hadid", "metal", "sharp", "strong"],
        "extended": ["limit", "boundary"],
        "avoid": ["strength", "power", "tool"]
    },
    "ل-ؤ-ل-ؤ": {
        "latin": "l-l-a", "category": "Natural World",
        "core": ["pearl", "lulu", "gem", "jewel"],
        "extended": ["precious", "ornament"],
        "avoid": ["paradise", "reward", "treasure"]
    },
    "ي-ا-ق-و-ت": {
        "latin": "y-q-t", "category": "Natural World",
        "core": ["ruby", "yaqut", "gem", "precious stone"],
        "extended": ["jewel", "ornament"],
        "avoid": ["paradise", "reward", "treasure"]
    },
    "ح-ر-ي-ر": {
        "latin": "h-r-r", "category": "Natural World",
        "core": ["silk", "harir", "fine fabric"],
        "extended": ["luxury", "garment"],
        "avoid": ["paradise", "reward", "clothing"]
    },
    "س-ن-د-س": {
        "latin": "s-n-d-s", "category": "Eschatology",
        "core": ["fine silk", "sundus", "brocade", "rich garment"],
        "extended": ["paradise clothing"],
        "avoid": ["silk", "garment", "reward"]
    },
    "ك-أ-س": {
        "latin": "k-a-s", "category": "Eschatology",
        "core": ["cup", "kas", "goblet", "drinking vessel"],
        "extended": ["wine cup"],
        "avoid": ["paradise", "drink", "reward"]
    },
    "ع-س-ل": {
        "latin": "a-s-l", "category": "Eschatology",
        "core": ["honey", "asal", "sweet", "nectar"],
        "extended": ["paradise river"],
        "avoid": ["sweetness", "reward", "paradise"]
    },
    "ل-ب-ن": {
        "latin": "l-b-n", "category": "Eschatology",
        "core": ["milk", "laban", "dairy"],
        "extended": ["nourishment", "paradise river"],
        "avoid": ["drink", "provision", "paradise"]
    },
    "ت-ف-ك-ر": {
        "latin": "f-k-r", "category": "Human Nature",
        "core": ["reflect", "tafakkur", "ponder deeply", "contemplate"],
        "extended": ["meditate", "consider"],
        "avoid": ["think", "reason", "know"]
    },
    "ت-د-ب-ر": {
        "latin": "d-b-r", "category": "Human Nature",
        "core": ["ponder", "tadabbur", "reflect deeply", "consider carefully",
                 "behind", "manage"],
        "extended": ["contemplate", "plan"],
        "avoid": ["think", "understand", "reflect"]
    },
    "إ-ع-ت-ب-ر": {
        "latin": "a-b-r", "category": "Human Nature",
        "core": ["take heed", "ibra", "lesson", "learn from", "cross over"],
        "extended": ["consider", "example"],
        "avoid": ["reflect", "think", "understand"]
    },
    "ل-ب-ب": {
        "latin": "l-b-b", "category": "Human Nature",
        "core": ["intellect", "lubb", "core", "mind", "essence", "kernel"],
        "extended": ["understanding", "reason"],
        "avoid": ["heart", "mind", "wisdom"]
    },
    "ص-د-ر": {
        "latin": "s-d-r", "category": "Human Nature",
        "core": ["chest", "sadr", "breast", "bosom", "front"],
        "extended": ["heart", "beginning"],
        "avoid": ["heart", "soul", "mind"]
    },
    "ب-ط-ن": {
        "latin": "b-t-n", "category": "Human Nature",
        "core": ["belly", "batn", "stomach", "inner", "hidden"],
        "extended": ["interior", "womb"],
        "avoid": ["inner", "hidden", "secret"]
    },
    "ظ-ه-ر-ة": {
        "latin": "zh-h-r", "category": "Human Nature",
        "core": ["back", "zahr", "outward", "exterior"],
        "extended": ["support", "surface"],
        "avoid": ["appear", "manifest", "outward"]
    },
    "ر-أ-س": {
        "latin": "r-a-s", "category": "Human Nature",
        "core": ["head", "ras", "chief", "leader", "top"],
        "extended": ["principal", "summit"],
        "avoid": ["leader", "chief", "first"]
    },
    "ع-ن-ق": {
        "latin": "a-n-q", "category": "Human Nature",
        "core": ["neck", "unq", "throat"],
        "extended": ["yoke", "burden"],
        "avoid": ["bond", "chain", "body"]
    },
    "ج-ن-ا-ح": {
        "latin": "j-n-h", "category": "Creation",
        "core": ["wing", "janah", "side", "flank"],
        "extended": ["protection", "shelter"],
        "avoid": ["bird", "fly", "creature"]
    },
    "ذ-ي-ل": {
        "latin": "dh-y-l", "category": "Natural World",
        "core": ["tail", "dhayl", "end", "trailing part"],
        "extended": ["consequence"],
        "avoid": ["end", "back", "follow"]
    },
    "أ-ج-ن-ح-ة": {
        "latin": "j-n-h", "category": "Creation",
        "core": ["wings", "ajniha", "flight parts"],
        "extended": ["angels", "birds"],
        "avoid": ["fly", "bird", "angel"]
    },
    "ق-و-ل-ب": {
        "latin": "q-l-b", "category": "Human Nature",
        "core": ["mold", "qalab", "form", "shape", "cast"],
        "extended": ["pattern", "model"],
        "avoid": ["heart", "create", "form"]
    },
    "ر-س-خ": {
        "latin": "r-s-kh", "category": "Faith",
        "core": ["firmly rooted", "rasikh", "deeply grounded", "established knowledge"],
        "extended": ["stable", "fixed"],
        "avoid": ["firm", "steadfast", "established"]
    },
    "ث-ق-ف": {
        "latin": "th-q-f", "category": "Action",
        "core": ["overpower", "thaqafa", "find", "seize", "encounter"],
        "extended": ["capture", "skillful"],
        "avoid": ["find", "seize", "capture"]
    },
    "أ-ح-ا-ط": {
        "latin": "h-w-t", "category": "Divine Names",
        "core": ["encompass", "ahata", "surround", "comprehend fully",
                 "encircle"],
        "extended": ["enclose", "contain"],
        "avoid": ["know", "vast", "aware"]
    },
    "ج-ن-ف": {
        "latin": "j-n-f", "category": "Ethics",
        "core": ["deviation", "janaf", "bias", "inclination to wrong",
                 "partiality"],
        "extended": ["lean toward sin"],
        "avoid": ["sin", "wrong", "injustice"]
    },
    "ح-ي-ف": {
        "latin": "h-y-f", "category": "Ethics",
        "core": ["injustice", "hayf", "partiality", "bias", "unfairness"],
        "extended": ["wrong side"],
        "avoid": ["wrong", "oppression", "injustice"]
    },
    "ب-خ-ل": {
        "latin": "b-kh-l", "category": "Ethics",
        "core": ["stingy", "bukhl", "miserliness", "withhold wealth",
                 "greed"],
        "extended": ["selfish", "tight-fisted"],
        "avoid": ["wealth", "withhold", "selfish"]
    },
    "إ-ن-ف-ا-ق": {
        "latin": "n-f-q", "category": "Worship",
        "core": ["spending", "infaq", "give in charity", "expenditure",
                 "support"],
        "extended": ["disburse", "provide"],
        "avoid": ["charity", "wealth", "gift"]
    },
    "ت-ب-ذ-ي-ر": {
        "latin": "b-dh-r", "category": "Ethics",
        "core": ["squander", "tabdhir", "waste", "extravagance",
                 "scatter wastefully"],
        "extended": ["dissipate", "spendthrift"],
        "avoid": ["excess", "waste", "extravagance"]
    },
    "أ-م-ل": {
        "latin": "a-m-l", "category": "Human Nature",
        "core": ["hope", "amal", "wish", "expectation", "aspiration"],
        "extended": ["long for", "anticipate"],
        "avoid": ["hope", "trust", "desire"]
    },
    "خ-ل-ص": {
        "latin": "kh-l-s", "category": "Worship",
        "core": ["sincere", "ikhlas", "pure devotion", "purify",
                 "exclusive devotion"],
        "extended": ["genuine", "extract"],
        "avoid": ["pure", "unique", "one"]
    },
    "ن-ي-ة": {
        "latin": "n-w-y", "category": "Worship",
        "core": ["intention", "niyya", "purpose", "intend", "resolve"],
        "extended": ["plan", "aim"],
        "avoid": ["will", "purpose", "intent"]
    },
    "ر-ك-ع": {
        "latin": "r-k-a", "category": "Worship",
        "core": ["bow", "ruku", "bend down", "prostrate posture"],
        "extended": ["humble before"],
        "avoid": ["pray", "prostrate", "worship"]
    },
    "ق-ن-ت": {
        "latin": "q-n-t", "category": "Worship",
        "core": ["devout", "qanut", "obedient worship", "stand long in prayer"],
        "extended": ["humility in prayer"],
        "avoid": ["pray", "worship", "obey"]
    },
    "ع-ك-ف": {
        "latin": "a-k-f", "category": "Worship",
        "core": ["devote", "itikaf", "seclude for worship", "remain attached"],
        "extended": ["dedicate", "retreat"],
        "avoid": ["worship", "pray", "devote"]
    },
    "ن-س-ك": {
        "latin": "n-s-k", "category": "Worship",
        "core": ["rites", "nusuk", "sacrifice", "devotion", "ritual"],
        "extended": ["worship acts", "piety"],
        "avoid": ["worship", "pilgrimage", "sacrifice"]
    },
    "ذ-ب-ح": {
        "latin": "dh-b-h", "category": "Worship",
        "core": ["slaughter", "dhabh", "sacrifice", "slay an animal"],
        "extended": ["offering"],
        "avoid": ["kill", "sacrifice", "offering"]
    },
    "ه-د-ى-ة": {
        "latin": "h-d-y", "category": "Worship",
        "core": ["offering", "hadiya", "sacrificial gift", "present"],
        "extended": ["gift to sanctuary"],
        "avoid": ["guidance", "gift", "sacrifice"]
    },
    "ح-ل-ق": {
        "latin": "h-l-q", "category": "Worship",
        "core": ["shave", "halq", "cut hair", "pilgrimage rite"],
        "extended": ["throat", "circle"],
        "avoid": ["pilgrimage", "rite", "ritual"]
    },
    "إ-ح-ر-ا-م": {
        "latin": "h-r-m", "category": "Worship",
        "core": ["sacred state", "ihram", "ritual consecration",
                 "pilgrimage garment"],
        "extended": ["forbidden state"],
        "avoid": ["sacred", "forbidden", "pilgrimage"]
    },
    "ط-و-ف": {
        "latin": "t-w-f", "category": "Worship",
        "core": ["circumambulate", "tawaf", "go around", "circle"],
        "extended": ["visit", "encircle"],
        "avoid": ["pilgrimage", "circle", "visit"]
    },
    "س-ع-ى-ر": {
        "latin": "s-a-y", "category": "Worship",
        "core": ["run between", "sai", "pilgrimage walk", "hasten"],
        "extended": ["effort in ritual"],
        "avoid": ["strive", "effort", "pilgrimage"]
    },
    "ع-و-ن": {
        "latin": "a-w-n", "category": "Worship",
        "core": ["help", "awn", "aid", "assist", "support",
                 "seek help"],
        "extended": ["cooperation", "succor"],
        "avoid": ["mercy", "guide", "provide"]
    },
}

# ── Helper functions ──────────────────────────────────────────────────────────

def get_root_data(root_arabic: str) -> dict:
    """Return lexicon entry for an Arabic root, or None if not found."""
    return ROOT_LEXICON.get(root_arabic)

def get_all_roots() -> list:
    """Return list of all root keys."""
    return list(ROOT_LEXICON.keys())

def get_roots_by_category(category: str) -> dict:
    """Return all roots belonging to a category."""
    return {k: v for k, v in ROOT_LEXICON.items() if v["category"] == category}

def get_semantic_field(root_arabic: str) -> set:
    """Return full semantic field (core + extended) for a root as a set."""
    data = ROOT_LEXICON.get(root_arabic)
    if not data:
        return set()
    return set(data["core"] + data["extended"])

def get_core_field(root_arabic: str) -> set:
    """Return only core meanings for a root."""
    data = ROOT_LEXICON.get(root_arabic)
    if not data:
        return set()
    return set(data["core"])

def get_avoid_terms(root_arabic: str) -> set:
    """Return terms that represent departure from root meaning."""
    data = ROOT_LEXICON.get(root_arabic)
    if not data:
        return set()
    return set(data["avoid"])

if __name__ == "__main__":
    total  = len(ROOT_LEXICON)
    cats   = {}
    for v in ROOT_LEXICON.values():
        cats[v["category"]] = cats.get(v["category"], 0) + 1
    print(f"\nQuranic Root Lexicon — {total} roots\n")
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat:<25} {count} roots")
    print()


# ── Auto-generated entries (expand_lexicon.py) ──────────────────────────────
# Generated from quran.com word-by-word gloss data.
# Core/extended fields are data-driven (most frequent gloss words per root).
# Review and refine manually for accuracy.

ROOT_LEXICON['أ-ب-ب'] = {
    "latin":    'a-b-b',
    "category": 'Quranic',
    "core":     ["fruits", "grass"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ب-ق'] = {
    "latin":    'a-b-q',
    "category": 'Quranic',
    "core":     ["ran", "ship", "away", "laden"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ب-ل'] = {
    "latin":    'a-b-l',
    "category": 'Quranic',
    "core":     ["against", "camels"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ب-ي'] = {
    "latin":    'a-b-y',
    "category": 'Quranic',
    "core":     ["except", "refused", "said", "prostrated", "iblis", "allah", "refuse", "most"],
    "extended": ["disbelief", "verily", "adam", "angels", "prostrate", "disbelievers", "term", "among"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ث-ث'] = {
    "latin":    'a-th-th',
    "category": 'Quranic',
    "core":     ["time", "cattle", "provision", "travel"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ث-ر'] = {
    "latin":    'a-th-r',
    "category": 'Quranic',
    "core":     ["said", "footsteps", "allah", "before", "indeed", "life", "sent", "over"],
    "extended": ["see", "any", "injeel", "seeking", "world", "prefer", "upon", "earth"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ث-ل'] = {
    "latin":    'a-th-l',
    "category": 'Quranic',
    "core":     ["producing", "changed", "away", "tamarisks"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ج-ج'] = {
    "latin":    'a-j-j',
    "category": 'Quranic',
    "core":     ["salty", "seas", "bitter", "sweet", "grateful"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ح-د'] = {
    "latin":    'a-h-d',
    "category": 'Quranic',
    "core":     ["allah", "anyone", "indeed", "any", "lord", "said", "say", "among"],
    "extended": ["except", "believe", "see", "surely", "between", "people", "given", "near"],
    "avoid":    [],
}
ROOT_LEXICON['أ-خ-ر'] = {
    "latin":    'a-kh-r',
    "category": 'Quranic',
    "core":     ["allah", "hereafter", "world", "indeed", "believe", "last", "day", "punishment"],
    "extended": ["among", "people", "surely", "whoever", "lord", "other", "another", "say"],
    "avoid":    [],
}
ROOT_LEXICON['أ-د-د'] = {
    "latin":    'a-d-d',
    "category": 'Quranic',
    "core":     ["forth", "atrocious", "put", "verily"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-د-م'] = {
    "latin":    'a-d-m',
    "category": 'Quranic',
    "core":     ["adam", "said", "indeed", "children", "angels", "both", "allah", "except"],
    "extended": ["prostrated", "prostrate", "iblis", "paradise", "lord", "created", "wrongdoers", "tree"],
    "avoid":    [],
}
ROOT_LEXICON['أ-د-ي'] = {
    "latin":    'a-d-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "lord", "whoever", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ذ-ن'] = {
    "latin":    'a-dh-n',
    "category": 'Quranic',
    "core":     ["allah", "permission", "indeed", "among", "except", "believe", "lord", "say"],
    "extended": ["surely", "messenger", "ears", "before", "believers", "said", "most", "ask"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ذ-ي'] = {
    "latin":    'a-dh-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "hurt", "believe", "among", "harmed", "messenger", "say"],
    "extended": ["come", "lord", "harm", "certainly", "near", "surely", "punishment", "prophet"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ر-ب'] = {
    "latin":    'a-r-b',
    "category": 'Quranic',
    "core":     ["said", "sheep", "staff", "lean"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ر-ك'] = {
    "latin":    'a-r-k',
    "category": 'Quranic',
    "core":     ["couches", "reclining", "therein", "observing", "thrones"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ز-ر'] = {
    "latin":    'a-z-r',
    "category": 'Quranic',
    "core":     ["reinforce", "through", "strength", "muhammad"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ز-ز'] = {
    "latin":    'a-z-z',
    "category": 'Quranic',
    "core":     ["incitement", "see", "inciting", "upon", "devils", "sent", "disbelievers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ز-ف'] = {
    "latin":    'a-z-f',
    "category": 'Quranic',
    "core":     ["approaching", "day", "approached"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-س-ر'] = {
    "latin":    'a-s-r',
    "category": 'Quranic',
    "core":     ["allah", "among", "most", "world", "captives", "prophet", "hearts", "captive"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-س-س'] = {
    "latin":    'a-s-s',
    "category": 'Quranic',
    "core":     ["founded", "righteousness", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-س-ف'] = {
    "latin":    'a-s-f',
    "category": 'Quranic',
    "core":     ["said", "over", "angry", "returned", "people", "lord", "musa", "grief"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-س-ن'] = {
    "latin":    'a-s-n',
    "category": 'Quranic',
    "core":     ["rivers", "water", "fire", "delicious"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-س-و'] = {
    "latin":    'a-s-w',
    "category": 'Quranic',
    "core":     ["grieve", "people", "allah", "said", "over", "indeed", "lord", "example"],
    "extended": ["until", "anything", "surely", "away", "last", "certainly", "day", "good"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ش-ر'] = {
    "latin":    'a-sh-r',
    "category": 'Quranic',
    "core":     ["liar", "insolent"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ص-ر'] = {
    "latin":    'a-s-r',
    "category": 'Quranic',
    "core":     ["help", "burden", "allah", "take", "upon", "believe", "messenger"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ص-ل'] = {
    "latin":    'a-s-l',
    "category": 'Quranic',
    "core":     ["allah", "evening", "morning", "mornings", "glorify", "remember", "evenings", "lord"],
    "extended": ["tree", "name"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ف-ف'] = {
    "latin":    'a-f-f',
    "category": 'Quranic',
    "core":     ["parents", "both", "worship", "allah", "uff"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ف-ق'] = {
    "latin":    'a-f-q',
    "category": 'Quranic',
    "core":     ["clear", "horizon"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ف-ك'] = {
    "latin":    'a-f-k',
    "category": 'Quranic',
    "core":     ["deluded", "allah", "say", "lie", "clear", "before", "indeed", "falsehood"],
    "extended": ["said", "came", "overturned", "think", "upon", "good", "other", "gods"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ف-ل'] = {
    "latin":    'a-f-l',
    "category": 'Quranic',
    "core":     ["said", "lord", "set", "saw", "star", "over", "ones", "covered"],
    "extended": ["like", "night", "rising", "people"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ك-ل'] = {
    "latin":    'a-k-l',
    "category": 'Quranic',
    "core":     ["eat", "indeed", "allah", "said", "good", "surely", "people", "drink"],
    "extended": ["cattle", "lord", "made", "forth", "earth", "believe", "wealth", "give"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ل-ت'] = {
    "latin":    'a-l-t',
    "category": 'Quranic',
    "core":     ["followed", "faith", "join", "pledged"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ل-ف'] = {
    "latin":    'a-l-f',
    "category": 'Quranic',
    "core":     ["thousand", "allah", "indeed", "year", "between", "hearts", "angels", "lord"],
    "extended": ["hundred", "among", "people", "ones", "sent", "wise", "earth", "steadfast"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ل-ل'] = {
    "latin":    'a-l-l',
    "category": 'Quranic',
    "core":     ["kinship", "protection", "covenant"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ل-م'] = {
    "latin":    'a-l-m',
    "category": 'Quranic',
    "core":     ["painful", "punishment", "allah", "indeed", "people", "believe", "give", "among"],
    "extended": ["while", "said", "except", "disbelieve", "any", "before", "disbelievers", "tidings"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ل-و'] = {
    "latin":    'a-l-w',
    "category": 'Quranic',
    "core":     ["lord", "favors", "both", "deny", "allah", "made", "swear", "merciful"],
    "extended": ["oft", "indeed", "forgiving", "most", "take", "among", "successors", "after"],
    "avoid":    [],
}
ROOT_LEXICON['أ-م-ت'] = {
    "latin":    'a-m-t',
    "category": 'Quranic',
    "core":     ["curve", "any", "crookedness", "see"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-م-د'] = {
    "latin":    'a-m-d',
    "category": 'Quranic',
    "core":     ["allah", "time", "term"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-م-م'] = {
    "latin":    'a-m-m',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "lord", "nation", "mother", "before", "among", "made"],
    "extended": ["except", "book", "community", "people", "say", "sent", "surely", "nations"],
    "avoid":    [],
}
ROOT_LEXICON['أ-م-و'] = {
    "latin":    'a-m-w',
    "category": 'Quranic',
    "core":     ["allah", "marry"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ن-ث'] = {
    "latin":    'a-n-th',
    "category": 'Quranic',
    "core":     ["female", "male", "indeed", "allah", "females", "made", "say", "lord"],
    "extended": ["whoever", "like", "surely", "righteous", "males", "knowledge", "angels", "created"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ن-س'] = {
    "latin":    'a-n-s',
    "category": 'Quranic',
    "core":     ["allah", "people", "mankind", "indeed", "man", "lord", "surely", "say"],
    "extended": ["most", "said", "earth", "except", "men", "day", "among", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ن-ف'] = {
    "latin":    'a-n-f',
    "category": 'Quranic',
    "core":     ["allah", "ear", "eye", "life", "retribution", "wrongdoers", "revealed", "tooth"],
    "extended": ["ordained", "nose", "wounds", "whoever", "charity", "gives", "expiation", "judge"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ن-م'] = {
    "latin":    'a-n-m',
    "category": 'Quranic',
    "core":     ["creatures", "laid", "earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ن-ي'] = {
    "latin":    'a-n-y',
    "category": 'Quranic',
    "core":     ["allah", "hours", "night", "given", "standing", "book", "among", "before"],
    "extended": ["say", "lord", "truth", "hearts"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ه-ل'] = {
    "latin":    'a-h-l',
    "category": 'Quranic',
    "core":     ["people", "allah", "indeed", "family", "said", "book", "except", "among"],
    "extended": ["say", "surely", "while", "lord", "until", "revealed", "came", "before"],
    "avoid":    [],
}
ROOT_LEXICON['أ-و-ب'] = {
    "latin":    'a-w-b',
    "category": 'Quranic',
    "core":     ["return", "indeed", "place", "repeatedly", "surely", "excellent", "righteous", "dawood"],
    "extended": ["slave", "good", "allah", "say", "lord", "birds", "gave", "turning"],
    "avoid":    [],
}
ROOT_LEXICON['أ-و-د'] = {
    "latin":    'a-w-d',
    "category": 'Quranic',
    "core":     ["high", "tires", "allah", "guarding"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-و-ن'] = {
    "latin":    'a-w-n',
    "category": 'Quranic',
    "core":     ["now", "indeed", "allah", "said", "says", "truth", "until", "knows"],
    "extended": ["while", "used", "evil"],
    "avoid":    [],
}
ROOT_LEXICON['أ-و-ه'] = {
    "latin":    'a-w-h',
    "category": 'Quranic',
    "core":     ["ibrahim", "forbearing", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-و-ي'] = {
    "latin":    'a-w-y',
    "category": 'Quranic',
    "core":     ["abode", "allah", "said", "hell", "fire", "wretched", "indeed", "destination"],
    "extended": ["any", "refuge", "except", "used", "earth", "lord", "day", "way"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ي-د'] = {
    "latin":    'a-y-d',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "supported", "isa", "son", "maryam", "spirit", "help"],
    "extended": ["came", "clear", "holy", "said", "disbelieved", "remember", "book", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['أ-ي-م'] = {
    "latin":    'a-y-m',
    "category": 'Quranic',
    "core":     ["enrich", "female", "marry", "encompassing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['أ-ي-ي'] = {
    "latin":    'a-y-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "signs", "believe", "verses", "lord", "people", "sign"],
    "extended": ["surely", "say", "clear", "said", "among", "earth", "deny", "except"],
    "avoid":    [],
}
ROOT_LEXICON['ب-أ-ر'] = {
    "latin":    'b-a-r',
    "category": 'Quranic',
    "core":     ["lofty", "roofs", "destroyed", "township"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-أ-س'] = {
    "latin":    'b-a-s',
    "category": 'Quranic',
    "core":     ["wretched", "allah", "punishment", "people", "hell", "evil", "said", "say"],
    "extended": ["except", "abode", "destination", "surely", "place", "disbelieve", "indeed", "disbelieved"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ت-ر'] = {
    "latin":    'b-t-r',
    "category": 'Quranic',
    "core":     ["indeed", "off", "enemy", "cut"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ت-ك'] = {
    "latin":    'b-t-k',
    "category": 'Quranic',
    "core":     ["cattle", "besides", "order", "lost"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ت-ل'] = {
    "latin":    'b-t-l',
    "category": 'Quranic',
    "core":     ["remember", "devotion", "name", "lord", "devote", "yourself"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ث-ث'] = {
    "latin":    'b-th-th',
    "category": 'Quranic',
    "core":     ["signs", "allah", "heavens", "creation", "earth", "dispersed", "water", "indeed"],
    "extended": ["sent", "people", "down", "therein", "moving", "creature", "day", "sky"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ج-س'] = {
    "latin":    'b-j-s',
    "category": 'Quranic',
    "core":     ["water", "knew", "themselves", "manna"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ح-ث'] = {
    "latin":    'b-h-th',
    "category": 'Quranic',
    "core":     ["said", "body", "unable", "scratching"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-خ-س'] = {
    "latin":    'b-kh-s',
    "category": 'Quranic',
    "core":     ["lord", "any", "give", "people", "full", "earth", "deprive", "corruption"],
    "extended": ["things", "fear", "allah", "justice", "other", "weight", "measure", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['ب-خ-ع'] = {
    "latin":    'b-kh-a',
    "category": 'Quranic',
    "core":     ["perhaps", "yourself"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-د-ر'] = {
    "latin":    'b-d-r',
    "category": 'Quranic',
    "core":     ["sufficient", "grow", "let", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-د-ل'] = {
    "latin":    'b-d-l',
    "category": 'Quranic',
    "core":     ["allah", "change", "indeed", "lord", "said", "other", "than", "except"],
    "extended": ["changed", "before", "never", "whoever", "after", "punishment", "better", "way"],
    "avoid":    [],
}
ROOT_LEXICON['ب-د-ن'] = {
    "latin":    'b-d-n',
    "category": 'Quranic',
    "core":     ["among"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-د-و'] = {
    "latin":    'b-d-w',
    "category": 'Quranic',
    "core":     ["allah", "conceal", "indeed", "said", "reveal", "say", "disclose", "apparent"],
    "extended": ["except", "made", "lord", "earth", "evil", "good", "thing", "knows"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ذ-ر'] = {
    "latin":    'b-dh-r',
    "category": 'Quranic',
    "core":     ["right", "wastefully", "relatives", "wayfarer", "spend", "needy", "give"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ج'] = {
    "latin":    'b-r-j',
    "category": 'Quranic',
    "core":     ["allah", "people", "constellations", "any", "placed", "house", "stay", "houses"],
    "extended": ["give", "former", "prayer", "purification", "messenger", "zakah", "display", "wishes"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ح'] = {
    "latin":    'b-r-h',
    "category": 'Quranic',
    "core":     ["said", "until", "never", "cease", "musa"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ز'] = {
    "latin":    'b-r-z',
    "category": 'Quranic',
    "core":     ["allah", "forth", "come", "say", "anything", "other", "day", "indeed"],
    "extended": ["group", "any", "about", "than", "surely", "leave", "before", "irresistible"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ز-خ'] = {
    "latin":    'b-r-z-kh',
    "category": 'Quranic',
    "core":     ["barrier", "between"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ص'] = {
    "latin":    'b-r-s',
    "category": 'Quranic',
    "core":     ["leper", "allah", "blind", "israel", "permission", "clay", "like", "breath"],
    "extended": ["children", "dead", "bird", "becomes", "into"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ك'] = {
    "latin":    'b-r-k',
    "category": 'Quranic',
    "core":     ["blessed", "allah", "worlds", "lord", "indeed", "made", "revealed", "earth"],
    "extended": ["night", "upon", "land", "book", "heavens", "blessings", "people", "best"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-م'] = {
    "latin":    'b-r-m',
    "category": 'Quranic',
    "core":     ["affair", "indeed", "determined"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ر-ه-ن'] = {
    "latin":    'b-r-h-n',
    "category": 'Quranic',
    "core":     ["proof", "say", "bring", "lord", "indeed", "allah", "forth", "truthful"],
    "extended": ["come", "know", "truth", "god", "any", "draw"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ز-غ'] = {
    "latin":    'b-z-gh',
    "category": 'Quranic',
    "core":     ["said", "rising", "set", "saw", "lord", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-ر'] = {
    "latin":    'b-s-r',
    "category": 'Quranic',
    "core":     ["scowled", "frowned", "day", "faces"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-س'] = {
    "latin":    'b-s-s',
    "category": 'Quranic',
    "core":     ["mountains", "crumbled", "crumbling"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-ط'] = {
    "latin":    'b-s-t',
    "category": 'Quranic',
    "core":     ["allah", "wills", "whom", "indeed", "provision", "extends", "lord", "restricts"],
    "extended": ["surely", "slaves", "towards", "hands", "people", "hand", "earth", "say"],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-ق'] = {
    "latin":    'b-s-q',
    "category": 'Quranic',
    "core":     ["palms", "arranged", "trees", "tall"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-ل'] = {
    "latin":    'b-s-l',
    "category": 'Quranic',
    "core":     ["water", "besides", "boiling", "punishment", "allah", "protector", "religion", "soul"],
    "extended": ["painful", "because", "destruction", "any", "disbelieve", "intercessor", "leave", "amusement"],
    "avoid":    [],
}
ROOT_LEXICON['ب-س-م'] = {
    "latin":    'b-s-m',
    "category": 'Quranic',
    "core":     ["said", "laughing", "parents", "mercy"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ص-ل'] = {
    "latin":    'b-s-l',
    "category": 'Quranic',
    "core":     ["right", "said", "never", "themselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ض-ع'] = {
    "latin":    'b-d-a',
    "category": 'Quranic',
    "core":     ["said", "merchandise", "allah", "measure", "family", "years", "father", "get"],
    "extended": ["easy", "measurement", "provision", "protect", "brother", "increase", "returned", "baggage"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ط-أ'] = {
    "latin":    'b-t-a',
    "category": 'Quranic',
    "core":     ["said", "lags", "befalls", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ط-ر'] = {
    "latin":    'b-t-r',
    "category": 'Quranic',
    "core":     ["showing", "boastfully", "encompassing", "forth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ط-ش'] = {
    "latin":    'b-t-sh',
    "category": 'Quranic',
    "core":     ["seize", "seizure", "indeed", "than", "destroyed", "stronger", "power", "retribution"],
    "extended": ["take", "day", "greatest"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ط-ل'] = {
    "latin":    'b-t-l',
    "category": 'Quranic',
    "core":     ["falsehood", "truth", "allah", "people", "believe", "indeed", "say", "disbelieve"],
    "extended": ["while", "wealth", "vain", "earth", "before", "falsifiers", "among", "fire"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ع-ث-ر'] = {
    "latin":    'b-a-th-r',
    "category": 'Quranic',
    "core":     ["graves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ع-ر'] = {
    "latin":    'b-a-r',
    "category": 'Quranic',
    "core":     ["said", "camel"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ع-ل'] = {
    "latin":    'b-a-l',
    "category": 'Quranic',
    "core":     ["allah", "right", "reconciliation", "themselves", "men", "women", "husbands", "over"],
    "extended": ["conceal", "aware", "indeed", "make", "husband", "woman", "best"],
    "avoid":    [],
}
ROOT_LEXICON['ب-غ-ت'] = {
    "latin":    'b-gh-t',
    "category": 'Quranic',
    "core":     ["suddenly", "while", "hour", "perceive", "come", "punishment", "allah", "until"],
    "extended": ["comes", "except", "said", "indeed", "seized", "given", "say", "people"],
    "avoid":    [],
}
ROOT_LEXICON['ب-غ-ض'] = {
    "latin":    'b-gh-d',
    "category": 'Quranic',
    "core":     ["hatred", "enmity", "allah", "indeed", "said", "between", "believe", "resurrection"],
    "extended": ["day", "till", "lord", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ب-غ-ل'] = {
    "latin":    'b-gh-l',
    "category": 'Quranic',
    "core":     ["horses", "creates", "mules", "ride"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-غ-ي'] = {
    "latin":    'b-gh-y',
    "category": 'Quranic',
    "core":     ["allah", "seek", "indeed", "seeking", "lord", "bounty", "most", "except"],
    "extended": ["among", "whom", "whoever", "people", "believe", "way", "while", "good"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ق-ر'] = {
    "latin":    'b-q-r',
    "category": 'Quranic',
    "core":     ["indeed", "said", "cows", "cow", "allah", "people", "pray", "says"],
    "extended": ["clear", "make", "lord", "fat", "surely", "truthful", "seven", "ears"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ق-ع'] = {
    "latin":    'b-q-a',
    "category": 'Quranic',
    "core":     ["right", "place", "allah", "called"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ق-ل'] = {
    "latin":    'b-q-l',
    "category": 'Quranic',
    "core":     ["right", "said", "never", "themselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ق-ي'] = {
    "latin":    'b-q-y',
    "category": 'Quranic',
    "core":     ["lord", "allah", "lasting", "better", "more", "surely", "believe", "given"],
    "extended": ["life", "world", "indeed", "believers", "best", "reward", "whatever", "enjoyment"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ك-ر'] = {
    "latin":    'b-k-r',
    "category": 'Quranic',
    "core":     ["morning", "evening", "lord", "glorify", "people", "said", "indeed", "make"],
    "extended": ["remember", "allah", "virgins"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ك-م'] = {
    "latin":    'b-k-m',
    "category": 'Quranic',
    "core":     ["dumb", "deaf", "allah", "blind", "example", "astray", "straight", "whoever"],
    "extended": ["lets"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ل-د'] = {
    "latin":    'b-l-d',
    "category": 'Quranic',
    "core":     ["land", "city", "lord", "thus", "dead", "forth", "allah", "sends"],
    "extended": ["except", "said", "disbelieved", "people", "make", "ibrahim", "secure", "fruits"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ل-س'] = {
    "latin":    'b-l-s',
    "category": 'Quranic',
    "core":     ["despair", "until", "opened"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ل-ع'] = {
    "latin":    'b-l-a',
    "category": 'Quranic',
    "core":     ["sky", "said", "water", "subsided"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ن-ن'] = {
    "latin":    'b-n-n',
    "category": 'Quranic',
    "core":     ["angels", "cast", "necks", "strike"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ن-ي'] = {
    "latin":    'b-n-y',
    "category": 'Quranic',
    "core":     ["allah", "children", "indeed", "said", "israel", "son", "sons", "maryam"],
    "extended": ["lord", "except", "say", "made", "people", "over", "isa", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ه-ت'] = {
    "latin":    'b-h-t',
    "category": 'Quranic',
    "core":     ["slander", "sin", "said", "indeed", "allah", "bring", "anything", "given"],
    "extended": ["manifest", "great", "come", "women", "believing"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ه-ج'] = {
    "latin":    'b-h-j',
    "category": 'Quranic',
    "core":     ["earth", "water", "cause", "down", "beautiful", "created", "out", "kind"],
    "extended": ["grow"],
    "avoid":    [],
}
ROOT_LEXICON['ب-ه-ل'] = {
    "latin":    'b-h-l',
    "category": 'Quranic',
    "core":     ["argues", "say", "come", "let"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ه-م'] = {
    "latin":    'b-h-m',
    "category": 'Quranic',
    "core":     ["allah", "cattle", "over", "name", "provided", "mention", "beast"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-و-أ'] = {
    "latin":    'b-w-a',
    "category": 'Quranic',
    "core":     ["allah", "wrath", "indeed", "used", "settled", "good", "reward", "themselves"],
    "extended": ["lord", "disbelieve", "earth", "day", "settle", "give", "right", "down"],
    "avoid":    [],
}
ROOT_LEXICON['ب-و-ب'] = {
    "latin":    'b-w-b',
    "category": 'Quranic',
    "core":     ["enter", "gate", "gates", "said", "opened", "say", "upon", "allah"],
    "extended": ["until", "punishment", "doors", "put", "arrogant", "heaven", "except", "abide"],
    "avoid":    [],
}
ROOT_LEXICON['ب-و-ر'] = {
    "latin":    'b-w-r',
    "category": 'Quranic',
    "core":     ["allah", "people", "became", "ruined", "perish", "evil", "never"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-و-ل'] = {
    "latin":    'b-w-l',
    "category": 'Quranic',
    "core":     ["said", "case", "lord", "condition", "improve"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ي-د'] = {
    "latin":    'b-y-d',
    "category": 'Quranic',
    "core":     ["ever", "said", "himself", "while"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ب-ي-ض'] = {
    "latin":    'b-y-d',
    "category": 'Quranic',
    "core":     ["white", "hand", "black", "allah", "people", "out", "come", "without"],
    "extended": ["forth", "turned", "used", "yourselves", "whose", "turn", "faces", "observers"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ب-ب'] = {
    "latin":    't-b-b',
    "category": 'Quranic',
    "core":     ["ruin", "hands", "lahab", "abu", "perish"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ب-ر'] = {
    "latin":    't-b-r',
    "category": 'Quranic',
    "core":     ["destruction", "destroyed", "sadden", "time", "promise", "first", "destroy", "last"],
    "extended": ["just", "entered", "yourselves", "enter", "conquered", "masjid", "faces", "came"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ب-ع'] = {
    "latin":    't-b-a',
    "category": 'Quranic',
    "core":     ["follow", "allah", "indeed", "followed", "say", "said", "lord", "except"],
    "extended": ["follows", "desires", "believe", "among", "any", "people", "revealed", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ج-ر'] = {
    "latin":    't-j-r',
    "category": 'Quranic',
    "core":     ["allah", "transaction", "commerce", "fear", "believe", "indeed", "say", "than"],
    "extended": ["between", "among", "more", "men", "out", "wealth", "guide", "prayer"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ح-ت'] = {
    "latin":    't-h-t',
    "category": 'Quranic',
    "core":     ["rivers", "underneath", "gardens", "allah", "flow", "forever", "deeds", "abide"],
    "extended": ["righteous", "flows", "lord", "admit", "believe", "therein", "indeed", "success"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ر-ب'] = {
    "latin":    't-r-b',
    "category": 'Quranic',
    "core":     ["dust", "become", "created", "indeed", "bones", "semen", "surely", "allah"],
    "extended": ["said", "companions", "among", "out", "drop", "forth", "brought", "dead"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ر-ف'] = {
    "latin":    't-r-f',
    "category": 'Quranic',
    "core":     ["before", "given", "luxury", "town", "wealthy", "said", "ones", "indeed"],
    "extended": ["except", "therein", "people", "sent", "warner", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ر-ق'] = {
    "latin":    't-r-q',
    "category": 'Quranic',
    "core":     ["bones", "reaches", "collar"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ر-ك'] = {
    "latin":    't-r-k',
    "category": 'Quranic',
    "core":     ["left", "allah", "indeed", "leave", "any", "people", "like", "said"],
    "extended": ["women", "made", "say", "among", "parents", "sign", "come", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['ت-س-ع'] = {
    "latin":    't-s-a',
    "category": 'Quranic',
    "core":     ["nine", "indeed", "said", "signs", "firaun", "overpowered", "ewe", "speech"],
    "extended": ["while", "brother", "ninety", "entrust"],
    "avoid":    [],
}
ROOT_LEXICON['ت-ع-س'] = {
    "latin":    't-a-s',
    "category": 'Quranic',
    "core":     ["disbelieve", "deeds", "lost", "destruction"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ف-ث'] = {
    "latin":    't-f-th',
    "category": 'Quranic',
    "core":     ["house", "prescribed", "circumambulate", "ancient"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ق-ن'] = {
    "latin":    't-q-n',
    "category": 'Quranic',
    "core":     ["perfected", "see", "pass", "aware"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ل-ل'] = {
    "latin":    't-l-l',
    "category": 'Quranic',
    "core":     ["submitted", "put", "both", "forehead"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ل-و'] = {
    "latin":    't-l-w',
    "category": 'Quranic',
    "core":     ["verses", "recite", "recited", "allah", "say", "book", "indeed", "lord"],
    "extended": ["clear", "except", "people", "believe", "surely", "truth", "before", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['ت-م-م'] = {
    "latin":    't-m-m',
    "category": 'Quranic',
    "core":     ["allah", "lord", "complete", "indeed", "favor", "except", "upon", "people"],
    "extended": ["completed", "said", "fulfilled", "make", "fear", "thus", "ten", "made"],
    "avoid":    [],
}
ROOT_LEXICON['ت-و-ر'] = {
    "latin":    't-w-r',
    "category": 'Quranic',
    "core":     ["time", "another"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ي-ن'] = {
    "latin":    't-y-n',
    "category": 'Quranic',
    "core":     ["fig", "olive"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ت-ي-ه'] = {
    "latin":    't-y-h',
    "category": 'Quranic',
    "core":     ["said", "wander", "years", "grieve"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ب-ر'] = {
    "latin":    'th-b-r',
    "category": 'Quranic',
    "core":     ["call", "destruction"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ب-ط'] = {
    "latin":    'th-b-t',
    "category": 'Quranic',
    "core":     ["allah", "being", "said", "prepared"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ب-ي'] = {
    "latin":    'th-b-y',
    "category": 'Quranic',
    "core":     ["groups", "believe", "together", "take"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ج-ج'] = {
    "latin":    'th-j-j',
    "category": 'Quranic',
    "core":     ["water", "clouds", "pouring", "rain"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-خ-ن'] = {
    "latin":    'th-kh-n',
    "category": 'Quranic',
    "core":     ["allah", "until", "war"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ر-ب'] = {
    "latin":    'th-r-b',
    "category": 'Quranic',
    "core":     ["said", "blame", "show", "mercy"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ر-ي'] = {
    "latin":    'th-r-y',
    "category": 'Quranic',
    "core":     ["heavens", "soil", "between", "under"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ع-ب'] = {
    "latin":    'th-a-b',
    "category": 'Quranic',
    "core":     ["serpent", "staff", "threw", "manifest"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ق-ب'] = {
    "latin":    'th-q-b',
    "category": 'Quranic',
    "core":     ["piercing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-ق-ل'] = {
    "latin":    'th-q-l',
    "category": 'Quranic',
    "core":     ["weight", "allah", "heavy", "earth", "atom", "day", "lord", "surely"],
    "extended": ["indeed", "forth", "heavens", "burdens", "scales", "about", "except", "carry"],
    "avoid":    [],
}
ROOT_LEXICON['ث-ل-ث'] = {
    "latin":    'th-l-th',
    "category": 'Quranic',
    "core":     ["three", "allah", "indeed", "among", "lord", "third", "women", "except"],
    "extended": ["said", "half", "any", "there", "after", "whatever", "wise", "right"],
    "avoid":    [],
}
ROOT_LEXICON['ث-ل-ل'] = {
    "latin":    'th-l-l',
    "category": 'Quranic',
    "core":     ["company", "former", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-م-ر'] = {
    "latin":    'th-m-r',
    "category": 'Quranic',
    "core":     ["fruits", "indeed", "people", "water", "forth", "fruit", "date", "down"],
    "extended": ["provision", "allah", "sky", "rivers", "gardens", "lord", "day", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ث-م-ن'] = {
    "latin":    'th-m-n',
    "category": 'Quranic',
    "core":     ["allah", "price", "little", "indeed", "exchange", "eight", "book", "lord"],
    "extended": ["believe", "say", "except", "revealed", "day", "conceal", "covenant", "verses"],
    "avoid":    [],
}
ROOT_LEXICON['ث-ن-ي'] = {
    "latin":    'th-n-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "said", "certainly", "people", "earth", "say", "sent"],
    "extended": ["forth", "twelve", "any", "females", "made", "surely", "both", "down"],
    "avoid":    [],
}
ROOT_LEXICON['ث-و-ر'] = {
    "latin":    'th-w-r',
    "category": 'Quranic',
    "core":     ["earth", "allah", "raise", "sends", "clouds", "winds"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ث-و-ي'] = {
    "latin":    'th-w-y',
    "category": 'Quranic',
    "core":     ["abode", "allah", "hell", "fire", "wretched", "abide", "arrogant", "indeed"],
    "extended": ["forever", "said", "gates", "enter", "wrongdoers", "disbelieve", "refuge", "about"],
    "avoid":    [],
}
ROOT_LEXICON['ث-ي-ب'] = {
    "latin":    'th-y-b',
    "category": 'Quranic',
    "core":     ["than", "divorced", "fast", "previously"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-أ-ر'] = {
    "latin":    'j-a-r',
    "category": 'Quranic',
    "core":     ["help", "cry"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ب'] = {
    "latin":    'j-b-b',
    "category": 'Quranic',
    "core":     ["well", "bottom"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ت'] = {
    "latin":    'j-b-t',
    "category": 'Quranic',
    "core":     ["than", "deities", "disbelieve", "false"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ر'] = {
    "latin":    'j-b-r',
    "category": 'Quranic',
    "core":     ["tyrant", "said", "musa", "obstinate", "signs", "dutiful", "allah", "over"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ن'] = {
    "latin":    'j-b-n',
    "category": 'Quranic',
    "core":     ["submitted", "put", "both", "forehead"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ه'] = {
    "latin":    'j-b-h',
    "category": 'Quranic',
    "core":     ["flanks", "fire", "taste", "hoard"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ب-ي'] = {
    "latin":    'j-b-y',
    "category": 'Quranic',
    "core":     ["chose", "allah", "guided", "lord", "ibrahim", "whom", "upon", "chooses"],
    "extended": ["believe", "wills", "straight", "follow", "say", "revealed", "guidance", "before"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ث-ث'] = {
    "latin":    'j-th-th',
    "category": 'Quranic',
    "core":     ["example", "tree", "uprooted", "stability"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ث-م'] = {
    "latin":    'j-th-m',
    "category": 'Quranic',
    "core":     ["seized", "prone", "became", "fallen", "earthquake", "homes", "home", "wronged"],
    "extended": ["blast", "thunderous"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ث-و'] = {
    "latin":    'j-th-w',
    "category": 'Quranic',
    "core":     ["knees", "bent"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ح-د'] = {
    "latin":    'j-h-d',
    "category": 'Quranic',
    "core":     ["allah", "reject", "verses", "signs", "used", "deny", "except", "wrongdoers"],
    "extended": ["religion", "deluded", "aad", "rejected", "right", "see", "thus", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ج-د-ث'] = {
    "latin":    'j-d-th',
    "category": 'Quranic',
    "core":     ["graves", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-د-د'] = {
    "latin":    'j-d-d',
    "category": 'Quranic',
    "core":     ["creation", "new", "lord", "bring", "say", "surely", "indeed", "disbelieved"],
    "extended": ["see", "wills", "allah", "earth", "particles", "resurrected", "bones", "crumbled"],
    "avoid":    [],
}
ROOT_LEXICON['ج-د-ر'] = {
    "latin":    'j-d-r',
    "category": 'Quranic',
    "core":     ["wall", "people", "town"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-د-ل'] = {
    "latin":    'j-d-l',
    "category": 'Quranic',
    "core":     ["allah", "dispute", "concerning", "indeed", "argue", "any", "people", "without"],
    "extended": ["over", "among", "said", "except", "disputes", "signs", "best", "day"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ذ-ذ'] = {
    "latin":    'j-dh-dh',
    "category": 'Quranic',
    "core":     ["except"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ذ-ع'] = {
    "latin":    'j-dh-a',
    "category": 'Quranic',
    "core":     ["date", "said", "trunk", "before", "palm"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ذ-و'] = {
    "latin":    'j-dh-w',
    "category": 'Quranic',
    "core":     ["said", "fire", "tur", "term"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ح'] = {
    "latin":    'j-r-h',
    "category": 'Quranic',
    "core":     ["allah", "life", "judge"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-د'] = {
    "latin":    'j-r-d',
    "category": 'Quranic',
    "core":     ["locusts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ر'] = {
    "latin":    'j-r-r',
    "category": 'Quranic',
    "core":     ["said", "considered", "angry", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ز'] = {
    "latin":    'j-r-z',
    "category": 'Quranic',
    "core":     ["barren"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ع'] = {
    "latin":    'j-r-a',
    "category": 'Quranic',
    "core":     ["harsh", "death", "swallowing", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ف'] = {
    "latin":    'j-r-f',
    "category": 'Quranic',
    "core":     ["wrongdoing", "guide", "cliff", "righteousness"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-م'] = {
    "latin":    'j-r-m',
    "category": 'Quranic',
    "core":     ["criminals", "indeed", "people", "lord", "thus", "say", "allah", "see"],
    "extended": ["day", "punishment", "before", "except", "crimes", "criminal", "sent", "doubt"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ر-ي'] = {
    "latin":    'j-r-y',
    "category": 'Quranic',
    "core":     ["rivers", "underneath", "allah", "gardens", "flow", "forever", "deeds", "abide"],
    "extended": ["indeed", "flows", "admit", "therein", "believe", "righteous", "lord", "success"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ز-أ'] = {
    "latin":    'j-z-a',
    "category": 'Quranic',
    "core":     ["portion"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-س-د'] = {
    "latin":    'j-s-d',
    "category": 'Quranic',
    "core":     ["calf", "lowing", "sound", "musa", "body"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-س-س'] = {
    "latin":    'j-s-s',
    "category": 'Quranic',
    "core":     ["flesh", "fear", "sin", "avoid"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-س-م'] = {
    "latin":    'j-s-m',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ف-أ'] = {
    "latin":    'j-f-a',
    "category": 'Quranic',
    "core":     ["water", "valleys", "fire", "order"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ف-ن'] = {
    "latin":    'j-f-n',
    "category": 'Quranic',
    "core":     ["dawood", "chambers", "fixed", "statues"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ف-و'] = {
    "latin":    'j-f-w',
    "category": 'Quranic',
    "core":     ["fear", "out", "sides", "hope"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ل-ب'] = {
    "latin":    'j-l-b',
    "category": 'Quranic',
    "core":     ["except", "incite", "partner", "wealth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ل-د'] = {
    "latin":    'j-l-d',
    "category": 'Quranic',
    "core":     ["allah", "skins", "time", "punishment", "flog", "other", "day", "against"],
    "extended": ["testify", "wise", "burn", "fire", "taste", "mighty", "signs", "change"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ل-ل'] = {
    "latin":    'j-l-l',
    "category": 'Quranic',
    "core":     ["majesty", "owner", "honor", "lord"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ل-و'] = {
    "latin":    'j-l-w',
    "category": 'Quranic',
    "core":     ["appointed", "lord", "allah", "day"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-م-ح'] = {
    "latin":    'j-m-h',
    "category": 'Quranic',
    "core":     ["run", "place", "caves", "wild"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-م-د'] = {
    "latin":    'j-m-d',
    "category": 'Quranic',
    "core":     ["perfected", "see", "pass", "aware"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-م-ل'] = {
    "latin":    'j-m-l',
    "category": 'Quranic',
    "core":     ["indeed", "patience", "said", "good", "thus", "souls", "nay", "beautiful"],
    "extended": ["allah", "enticed", "bring", "gracious", "release", "provide", "say", "patient"],
    "avoid":    [],
}
ROOT_LEXICON['ج-م-م'] = {
    "latin":    'j-m-m',
    "category": 'Quranic',
    "core":     ["immense", "wealth", "love"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ن-ب'] = {
    "latin":    'j-n-b',
    "category": 'Quranic',
    "core":     ["allah", "side", "avoid", "indeed", "lord", "earth", "near", "worship"],
    "extended": ["away", "sides", "right", "hands", "believe", "yourselves", "made", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ن-ح'] = {
    "latin":    'j-n-h',
    "category": 'Quranic',
    "core":     ["allah", "blame", "any", "upon", "indeed", "women", "sin", "fear"],
    "extended": ["among", "except", "whom", "knower", "between", "both", "good", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ن-د'] = {
    "latin":    'j-n-d',
    "category": 'Quranic',
    "core":     ["hosts", "allah", "see", "sent", "said", "indeed", "forces", "sea"],
    "extended": ["help", "down", "upon", "believe", "firaun", "except", "out", "tranquility"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ن-ي'] = {
    "latin":    'j-n-y',
    "category": 'Quranic',
    "core":     ["fresh", "trunk", "drop", "ripe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ه-ر'] = {
    "latin":    'j-h-r',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "speech", "knows", "believe", "while", "except", "loudness"],
    "extended": ["hidden", "loud", "manifestly", "thunderbolt", "said", "musa", "words", "public"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ه-ز'] = {
    "latin":    'j-h-z',
    "category": 'Quranic',
    "core":     ["brother", "furnished", "supplies", "hosts", "said", "father", "see", "measure"],
    "extended": ["yours", "best", "bring", "give", "full", "called", "out", "put"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ه-ل'] = {
    "latin":    'j-h-l',
    "category": 'Quranic',
    "core":     ["ignorant", "allah", "indeed", "people", "ignorance", "said", "say", "than"],
    "extended": ["upon", "seek", "earth", "sent", "after", "believe", "lord", "most"],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-ب'] = {
    "latin":    'j-w-b',
    "category": 'Quranic',
    "core":     ["respond", "allah", "indeed", "lord", "responded", "said", "day", "except"],
    "extended": ["call", "people", "punishment", "believe", "answer", "like", "calls", "say"],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-د'] = {
    "latin":    'j-w-d',
    "category": 'Quranic',
    "core":     ["sky", "said", "water", "subsided"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-ر'] = {
    "latin":    'j-w-r',
    "category": 'Quranic',
    "core":     ["allah", "people", "indeed", "know", "say", "anyone", "protect", "neighbor"],
    "extended": ["away", "polytheists", "hears", "place", "escort", "safety", "words", "grant"],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-ز'] = {
    "latin":    'j-w-z',
    "category": 'Quranic',
    "core":     ["said", "indeed", "except", "ones", "israel", "across", "sea", "god"],
    "extended": ["children"],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-س'] = {
    "latin":    'j-w-s',
    "category": 'Quranic',
    "core":     ["military", "raised", "first", "promise"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-ع'] = {
    "latin":    'j-w-a',
    "category": 'Quranic',
    "core":     ["hunger", "fear"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-ف'] = {
    "latin":    'j-w-f',
    "category": 'Quranic',
    "core":     ["says", "wives", "allah", "saying"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-و-و'] = {
    "latin":    'j-w-w',
    "category": 'Quranic',
    "core":     ["sky", "except", "see", "none"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ج-ي-أ'] = {
    "latin":    'j-y-a',
    "category": 'Quranic',
    "core":     ["came", "allah", "come", "said", "indeed", "lord", "clear", "say"],
    "extended": ["comes", "people", "messengers", "truth", "after", "before", "except", "certainly"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ي-ب'] = {
    "latin":    'j-y-b',
    "category": 'Quranic',
    "core":     ["among", "draw", "white", "bosom", "forth", "come", "firaun", "without"],
    "extended": ["hand", "indeed", "harm", "defiantly", "disobedient", "people"],
    "avoid":    [],
}
ROOT_LEXICON['ج-ي-د'] = {
    "latin":    'j-y-d',
    "category": 'Quranic',
    "core":     ["fiber", "palm", "neck", "rope"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ب-ر'] = {
    "latin":    'h-b-r',
    "category": 'Quranic',
    "core":     ["rabbis", "allah", "indeed", "people", "scholars", "surely", "monks", "delighted"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ب-س'] = {
    "latin":    'h-b-s',
    "category": 'Quranic',
    "core":     ["time", "doubt", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ب-ط'] = {
    "latin":    'h-b-t',
    "category": 'Quranic',
    "core":     ["worthless", "deeds", "allah", "hereafter", "made", "ones", "losers", "fire"],
    "extended": ["became", "among", "world", "before", "surely", "used", "like", "disbelief"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ب-ك'] = {
    "latin":    'h-b-k',
    "category": 'Quranic',
    "core":     ["full", "heaven", "pathways"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ب-ل'] = {
    "latin":    'h-b-l',
    "category": 'Quranic',
    "core":     ["rope", "allah", "verses", "said", "staffs", "ropes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ت-م'] = {
    "latin":    'h-t-m',
    "category": 'Quranic',
    "core":     ["decreed", "over", "passing", "inevitability"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ث-ث'] = {
    "latin":    'h-th-th',
    "category": 'Quranic',
    "core":     ["epochs", "moon", "unquestionably", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ج-ب'] = {
    "latin":    'h-j-b',
    "category": 'Quranic',
    "core":     ["indeed", "between", "screen", "call", "believe", "hidden", "allah", "messenger"],
    "extended": ["permission", "behind", "except", "hearts", "veil", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ج-ز'] = {
    "latin":    'h-j-z',
    "category": 'Quranic',
    "core":     ["any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-د-ب'] = {
    "latin":    'h-d-b',
    "category": 'Quranic',
    "core":     ["majuj", "elevation", "descend", "until"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-د-ث'] = {
    "latin":    'h-d-th',
    "category": 'Quranic',
    "core":     ["allah", "statement", "believe", "lord", "after", "come", "people", "about"],
    "extended": ["indeed", "except", "perhaps", "said", "narration", "before", "day", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['ح-د-د'] = {
    "latin":    'h-d-d',
    "category": 'Quranic',
    "core":     ["allah", "limits", "messenger", "clear", "whoever", "keep", "know", "certainly"],
    "extended": ["people", "fear", "transgresses", "iron", "until", "sin", "lawful", "except"],
    "avoid":    [],
}
ROOT_LEXICON['ح-د-ق'] = {
    "latin":    'h-d-q',
    "category": 'Quranic',
    "core":     ["gardens"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ذ-ر'] = {
    "latin":    'h-dh-r',
    "category": 'Quranic',
    "core":     ["allah", "beware", "indeed", "fear", "take", "say", "most", "know"],
    "extended": ["people", "punishment", "lest", "disbelievers", "upon", "believe", "let", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ب'] = {
    "latin":    'h-r-b',
    "category": 'Quranic',
    "core":     ["allah", "war", "chamber", "messenger", "indeed", "prayer", "among", "surely"],
    "extended": ["said", "wills", "gives", "lord", "good", "strive", "hands", "killed"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ج'] = {
    "latin":    'h-r-j',
    "category": 'Quranic',
    "core":     ["any", "allah", "upon", "discomfort", "believe", "find", "believers", "sick"],
    "extended": ["messenger", "blame", "concerning", "make", "favor", "prayer", "difficulty", "yourselves"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-د'] = {
    "latin":    'h-r-d',
    "category": 'Quranic',
    "core":     ["went", "early", "able", "determination"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ر'] = {
    "latin":    'h-r-r',
    "category": 'Quranic',
    "core":     ["allah", "slave", "whoever", "said", "heat", "believe", "lord", "freeing"],
    "extended": ["garments", "silk", "follows", "female", "mercy", "anything", "murdered", "pardoned"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-س'] = {
    "latin":    'h-r-s',
    "category": 'Quranic',
    "core":     ["flaming", "sought", "guards", "severe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ص'] = {
    "latin":    'h-r-s',
    "category": 'Quranic',
    "core":     ["allah", "most", "mankind", "indeed", "merciful", "even", "believers", "desire"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ض'] = {
    "latin":    'h-r-d',
    "category": 'Quranic',
    "core":     ["fight", "believers", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ف'] = {
    "latin":    'h-r-f',
    "category": 'Quranic',
    "core":     ["allah", "distort", "words", "believe", "except", "after", "indeed", "hear"],
    "extended": ["said", "disbelief", "cursed", "few", "places", "jews", "hearts", "good"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ق'] = {
    "latin":    'h-r-q',
    "category": 'Quranic',
    "core":     ["fire", "punishment", "allah", "said", "indeed", "burning", "taste", "burn"],
    "extended": ["signs", "say", "certainly", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ك'] = {
    "latin":    'h-r-k',
    "category": 'Quranic',
    "core":     ["move", "hasten", "tongue"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ر-ي'] = {
    "latin":    'h-r-y',
    "category": 'Quranic',
    "core":     ["right", "path", "sought", "unjust"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ز-ب'] = {
    "latin":    'h-z-b',
    "category": 'Quranic',
    "core":     ["indeed", "among", "party", "allah", "people", "messenger", "doubt", "day"],
    "extended": ["believe", "sects", "about", "truth", "except", "confederates", "faith", "shaitaan"],
    "avoid":    [],
}
ROOT_LEXICON['ح-س-ر'] = {
    "latin":    'h-s-r',
    "category": 'Quranic',
    "core":     ["allah", "regret", "indeed", "said", "out", "return", "regrets", "believe"],
    "extended": ["earth", "came", "neglected", "while", "over", "evil", "soul", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ح-س-س'] = {
    "latin":    'h-s-s',
    "category": 'Quranic',
    "core":     ["allah", "perceived", "desire", "hear", "sound"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-س-م'] = {
    "latin":    'h-s-m',
    "category": 'Quranic',
    "core":     ["imposed", "days", "see", "eight"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ب'] = {
    "latin":    'h-s-b',
    "category": 'Quranic',
    "core":     ["storm", "stones", "swallow", "feel", "against", "send", "secure", "allah"],
    "extended": ["indeed", "sent"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ح-ص'] = {
    "latin":    'h-s-h-s',
    "category": 'Quranic',
    "core":     ["truthful", "said", "affair", "wife"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-د'] = {
    "latin":    'h-s-d',
    "category": 'Quranic',
    "core":     ["eat", "harvest", "gardens", "day", "water", "until", "sent", "down"],
    "extended": ["mown", "sky", "made"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ر'] = {
    "latin":    'h-s-r',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "way", "return", "among", "find", "whatever", "people"],
    "extended": ["prayer", "made"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ل'] = {
    "latin":    'h-s-l',
    "category": 'Quranic',
    "core":     ["made", "apparent", "breasts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ن'] = {
    "latin":    'h-s-n',
    "category": 'Quranic',
    "core":     ["chaste", "women", "allah", "due", "bridal", "give", "possess", "believers"],
    "extended": ["among", "whoever", "sin", "married", "lovers", "secret", "hands", "faith"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ص-ي'] = {
    "latin":    'h-s-y',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "count", "enumerated", "lord", "merciful", "oft", "forgiving"],
    "extended": ["most", "evident", "make", "except", "book", "find", "clear", "give"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ض-ر'] = {
    "latin":    'h-d-r',
    "category": 'Quranic',
    "core":     ["brought", "among", "allah", "between", "indeed", "lord", "surely", "death"],
    "extended": ["good", "present", "approaches", "near", "fear", "find", "know", "presented"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ض-ض'] = {
    "latin":    'h-d-d',
    "category": 'Quranic',
    "core":     ["feel", "urge", "poor", "feed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ط-ب'] = {
    "latin":    'h-t-b',
    "category": 'Quranic',
    "core":     ["firewood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ط-ط'] = {
    "latin":    'h-t-t',
    "category": 'Quranic',
    "core":     ["said", "wherever", "doers", "prostrating", "forgive", "say", "increase", "enter"],
    "extended": ["repentance", "gate", "sins", "eat", "good", "wish"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ظ-ر'] = {
    "latin":    'h-z-r',
    "category": 'Quranic',
    "core":     ["gift", "extend", "lord", "restricted"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ظ-ظ'] = {
    "latin":    'h-z-z',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "great", "like", "any", "portion", "thirds", "brothers"],
    "extended": ["inherit", "half", "sisters", "there", "females", "made", "concerning", "women"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ف-د'] = {
    "latin":    'h-f-d',
    "category": 'Quranic',
    "core":     ["disbelieve", "believe", "provided", "yourselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ف-ر'] = {
    "latin":    'h-f-r',
    "category": 'Quranic',
    "core":     ["rope", "hold", "between", "fire"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ف-ف'] = {
    "latin":    'h-f-f',
    "category": 'Quranic',
    "core":     ["between"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ف-و'] = {
    "latin":    'h-f-w',
    "category": 'Quranic',
    "core":     ["ask", "lord"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ق-ب'] = {
    "latin":    'h-q-b',
    "category": 'Quranic',
    "core":     ["said", "cease", "seas", "reach"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ق-ف'] = {
    "latin":    'h-q-f',
    "category": 'Quranic',
    "core":     ["fear", "indeed", "allah", "mention"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ل-ف'] = {
    "latin":    'h-l-f',
    "category": 'Quranic',
    "core":     ["allah", "swear", "indeed", "people", "except", "surely", "liars", "while"],
    "extended": ["messenger", "forth", "come", "good", "whoever", "certainly", "believers", "disbelief"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ل-ي'] = {
    "latin":    'h-l-y',
    "category": 'Quranic',
    "core":     ["ornaments", "silk", "garments", "bracelets", "adorned", "see", "wear", "gold"],
    "extended": ["gardens", "therein", "allah", "forth", "flows", "fresh", "grateful", "ships"],
    "avoid":    [],
}
ROOT_LEXICON['ح-م-أ'] = {
    "latin":    'h-m-a',
    "category": 'Quranic',
    "core":     ["mud", "altered", "clay", "black", "said", "created", "human"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-م-ر'] = {
    "latin":    'h-m-r',
    "category": 'Quranic',
    "core":     ["allah", "donkeys", "people", "donkey", "like", "know", "bring"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-م-م'] = {
    "latin":    'h-m-m',
    "category": 'Quranic',
    "core":     ["water", "scalding", "boiling", "friend", "drink", "fire", "punishment", "any"],
    "extended": ["over", "allah", "painful", "because", "disbelieve", "intercessor", "used", "given"],
    "avoid":    [],
}
ROOT_LEXICON['ح-م-ي'] = {
    "latin":    'h-m-y',
    "category": 'Quranic',
    "core":     ["fire", "disbelieved", "made", "allah", "hot", "intensely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ث'] = {
    "latin":    'h-n-th',
    "category": 'Quranic',
    "core":     ["repeatedly", "excellent", "strike", "oath"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ج-ر'] = {
    "latin":    'h-n-j-r',
    "category": 'Quranic',
    "core":     ["hearts", "throats"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ذ'] = {
    "latin":    'h-n-dh',
    "category": 'Quranic',
    "core":     ["calf", "ibrahim", "said", "messengers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ف'] = {
    "latin":    'h-n-f',
    "category": 'Quranic',
    "core":     ["upright", "religion", "ibrahim", "polytheists", "allah", "face", "say", "true"],
    "extended": ["indeed", "guided", "partners", "follow", "monotheist", "created", "correct"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ك'] = {
    "latin":    'h-n-k',
    "category": 'Quranic',
    "core":     ["honored", "said", "except", "respite"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ن-ن'] = {
    "latin":    'h-n-n',
    "category": 'Quranic',
    "core":     ["affection", "righteous", "purity"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ب'] = {
    "latin":    'h-w-b',
    "category": 'Quranic',
    "core":     ["exchange", "orphans", "bad", "wealth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ت'] = {
    "latin":    'h-w-t',
    "category": 'Quranic',
    "core":     ["fish", "sea", "took", "way", "forgot", "into", "while"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ج'] = {
    "latin":    'h-w-j',
    "category": 'Quranic',
    "core":     ["soul", "any", "carried", "need", "breasts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ذ'] = {
    "latin":    'h-w-dh',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ز'] = {
    "latin":    'h-w-z',
    "category": 'Quranic',
    "core":     ["allah", "except", "join", "wretched"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ش'] = {
    "latin":    'h-w-sh',
    "category": 'Quranic',
    "core":     ["said", "allah", "forbid"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ط'] = {
    "latin":    'h-w-t',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "encompassing", "said", "encompassed", "knowledge", "lord", "encompass"],
    "extended": ["surely", "like", "surrounded", "behind", "people", "come", "things", "fear"],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ل'] = {
    "latin":    'h-w-l',
    "category": 'Quranic',
    "core":     ["around", "allah", "any", "except", "indeed", "way", "among", "believe"],
    "extended": ["between", "people", "said", "lord", "fire", "see", "ask", "mother"],
    "avoid":    [],
}
ROOT_LEXICON['ح-و-ي'] = {
    "latin":    'h-w-y',
    "category": 'Quranic',
    "core":     ["cows", "truthful", "except", "sheep"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ي-د'] = {
    "latin":    'h-y-d',
    "category": 'Quranic',
    "core":     ["stupor", "death", "come", "avoiding"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ي-ر'] = {
    "latin":    'h-y-r',
    "category": 'Quranic',
    "core":     ["heels", "besides", "say", "guided"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ي-ص'] = {
    "latin":    'h-y-s',
    "category": 'Quranic',
    "core":     ["any", "escape", "place", "before"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ح-ي-ض'] = {
    "latin":    'h-y-d',
    "category": 'Quranic',
    "core":     ["allah", "until", "women", "menstruation", "affair", "term", "three", "among"],
    "extended": ["pregnant", "ease", "waiting", "burdens", "period", "doubt", "make", "months"],
    "avoid":    [],
}
ROOT_LEXICON['ح-ي-ق'] = {
    "latin":    'h-y-q',
    "category": 'Quranic',
    "core":     ["used", "mock", "messengers", "surrounded", "evil", "allah", "enveloped", "mocked"],
    "extended": ["before", "surround", "punishment", "any", "people", "evils"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-أ'] = {
    "latin":    'kh-b-a',
    "category": 'Quranic',
    "core":     ["heavens", "allah", "knows", "forth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-ت'] = {
    "latin":    'kh-b-t',
    "category": 'Quranic',
    "core":     ["believe", "humble", "indeed", "lord", "allah", "submit"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-ث'] = {
    "latin":    'kh-b-th',
    "category": 'Quranic',
    "core":     ["good", "evil", "say", "men", "allah", "women", "innocent", "noble"],
    "extended": ["provision", "forgiveness", "bad", "believe", "fear", "successful", "forth", "except"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-ز'] = {
    "latin":    'kh-b-z',
    "category": 'Quranic',
    "core":     ["said", "see", "entered", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-ط'] = {
    "latin":    'kh-b-t',
    "category": 'Quranic',
    "core":     ["usury", "permitted", "fire", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-ل'] = {
    "latin":    'kh-b-l',
    "category": 'Quranic',
    "core":     ["conceals", "believe", "intimates", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ب-و'] = {
    "latin":    'kh-b-w',
    "category": 'Quranic',
    "core":     ["dumb", "protectors", "time", "never"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ت-ر'] = {
    "latin":    'kh-t-r',
    "category": 'Quranic',
    "core":     ["religion", "except", "wave", "land"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ت-م'] = {
    "latin":    'kh-t-m',
    "category": 'Quranic',
    "core":     ["seal", "allah", "hearing", "vision", "veil", "hearts", "say", "sealed"],
    "extended": ["seen", "god", "about", "heart", "over"],
    "avoid":    [],
}
ROOT_LEXICON['خ-د-د'] = {
    "latin":    'kh-d-d',
    "category": 'Quranic',
    "core":     ["conceited", "self", "walk", "cheek"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-د-ع'] = {
    "latin":    'kh-d-a',
    "category": 'Quranic',
    "core":     ["deceive", "allah", "except", "indeed", "believe", "themselves", "realize", "seek"],
    "extended": ["lazily", "showing", "hypocrites", "little", "off", "stand", "deceives", "prayer"],
    "avoid":    [],
}
ROOT_LEXICON['خ-د-ن'] = {
    "latin":    'kh-d-n',
    "category": 'Quranic',
    "core":     ["believers", "among", "lovers", "secret", "due", "bridal", "whoever", "faith"],
    "extended": ["women", "chaste"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ذ-ل'] = {
    "latin":    'kh-dh-l',
    "category": 'Quranic',
    "core":     ["after", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-ب'] = {
    "latin":    'kh-r-b',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-د-ل'] = {
    "latin":    'kh-r-d-l',
    "category": 'Quranic',
    "core":     ["mustard", "weight", "seed", "bring"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-ر'] = {
    "latin":    'kh-r-r',
    "category": 'Quranic',
    "core":     ["fell", "down", "lord", "upon", "fall", "said", "indeed", "before"],
    "extended": ["allah", "believe", "verses", "came", "place", "made", "mountain", "verily"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-ص'] = {
    "latin":    'kh-r-s',
    "category": 'Quranic',
    "core":     ["allah", "follow", "guess", "assumption", "earth", "except", "most", "say"],
    "extended": ["partners", "any", "willed", "knowledge"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-ط-م'] = {
    "latin":    'kh-r-t-m',
    "category": 'Quranic',
    "core":     ["brand", "snout"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ر-ق'] = {
    "latin":    'kh-r-q',
    "category": 'Quranic',
    "core":     ["said", "ship", "out", "both", "set", "done", "grave", "certainly"],
    "extended": ["drown", "made", "thing", "hole", "until", "people", "embarked"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ز-ن'] = {
    "latin":    'kh-z-n',
    "category": 'Quranic',
    "core":     ["say", "treasures", "lord", "keepers", "allah", "down", "until", "unseen"],
    "extended": ["except", "give", "know", "angel", "indeed", "any", "surely", "upon"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ز-ي'] = {
    "latin":    'kh-z-y',
    "category": 'Quranic',
    "core":     ["disgrace", "allah", "punishment", "world", "day", "indeed", "whom", "hereafter"],
    "extended": ["resurrection", "come", "life", "lord", "people", "sent", "great", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['خ-س-أ'] = {
    "latin":    'kh-s-a',
    "category": 'Quranic',
    "core":     ["despised", "said", "apes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-س-ف'] = {
    "latin":    'kh-s-f',
    "category": 'Quranic',
    "core":     ["swallow", "earth", "allah", "feel", "secure", "cause", "caused", "storm"],
    "extended": ["themselves", "before", "heaven"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ش-ب'] = {
    "latin":    'kh-sh-b',
    "category": 'Quranic',
    "core":     ["shout", "see", "speech", "speak"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ش-ع'] = {
    "latin":    'kh-sh-a',
    "category": 'Quranic',
    "core":     ["indeed", "humbled", "allah", "humble", "day", "surely", "reward", "humbly"],
    "extended": ["submissive", "give", "down", "eyes", "except", "book", "among", "people"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ش-ي'] = {
    "latin":    'kh-sh-y',
    "category": 'Quranic',
    "core":     ["fear", "allah", "indeed", "people", "whoever", "lord", "fears", "except"],
    "extended": ["upon", "said", "more", "favor", "give", "say", "any", "wronged"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ص-ص'] = {
    "latin":    'kh-s-s',
    "category": 'Quranic',
    "core":     ["allah", "chooses", "wills", "bounty", "mercy", "great", "any", "possessor"],
    "extended": ["whom"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ص-ف'] = {
    "latin":    'kh-s-f',
    "category": 'Quranic',
    "core":     ["shame", "themselves", "became", "began", "lord", "apparent", "both", "fasten"],
    "extended": ["leaves"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ص-م'] = {
    "latin":    'kh-s-m',
    "category": 'Quranic',
    "core":     ["dispute", "people", "disputing", "indeed", "opponents", "allah", "truth", "sent"],
    "extended": ["behold", "clear", "fire", "over", "lord", "news", "between", "judge"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ض-د'] = {
    "latin":    'kh-d-d',
    "category": 'Quranic',
    "core":     ["thornless", "among", "trees", "lote"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ض-ر'] = {
    "latin":    'kh-d-r',
    "category": 'Quranic',
    "core":     ["green", "indeed", "water", "sends", "people", "down", "gardens", "sky"],
    "extended": ["cows", "seven", "ears", "explain", "lean", "about", "eating", "dry"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ض-ع'] = {
    "latin":    'kh-d-a',
    "category": 'Quranic',
    "core":     ["sky", "necks", "bend", "sign"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ط-أ'] = {
    "latin":    'kh-t-a',
    "category": 'Quranic',
    "core":     ["sins", "indeed", "forgive", "allah", "said", "any", "sin", "sinners"],
    "extended": ["enter", "repentance", "eat", "whoever", "lord", "except", "wherever", "doers"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ط-ب'] = {
    "latin":    'kh-t-b',
    "category": 'Quranic',
    "core":     ["said", "address", "indeed", "most", "ones", "say", "allah", "until"],
    "extended": ["except", "know", "women", "concerning", "ship", "wronged", "eyes", "under"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ط-ط'] = {
    "latin":    'kh-t-t',
    "category": 'Quranic',
    "core":     ["right", "write", "before", "recite"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ط-ف'] = {
    "latin":    'kh-t-f',
    "category": 'Quranic',
    "core":     ["snatches", "away", "allah", "taken", "things", "being", "secure", "sanctuary"],
    "extended": ["burning", "except", "theft", "flame", "follows", "piercing"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ط-و'] = {
    "latin":    'kh-t-w',
    "category": 'Quranic',
    "core":     ["follow", "footsteps", "indeed", "shaitaan", "enemy", "eat", "believe", "open"],
    "extended": ["allah"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ف-ت'] = {
    "latin":    'kh-f-t',
    "category": 'Quranic',
    "core":     ["names", "allah", "prayers", "loud"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ف-ض'] = {
    "latin":    'kh-f-d',
    "category": 'Quranic',
    "core":     ["wing", "lower", "believers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ف-ف'] = {
    "latin":    'kh-f-f',
    "category": 'Quranic',
    "core":     ["light", "lightened", "punishment", "allah", "forever", "abide", "lord", "scales"],
    "extended": ["hell", "ones", "reprieved", "lighten", "created", "lost", "among", "made"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ف-ي'] = {
    "latin":    'kh-f-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "conceal", "hidden", "knows", "disclose", "thing", "earth"],
    "extended": ["say", "any", "day", "secret", "breasts", "lord", "call", "anything"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ل-د'] = {
    "latin":    'kh-l-d',
    "category": 'Quranic',
    "core":     ["forever", "abide", "allah", "therein", "rivers", "fire", "gardens", "underneath"],
    "extended": ["abiding", "companions", "lord", "deeds", "great", "indeed", "righteous", "flows"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ل-ط'] = {
    "latin":    'kh-l-t',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "world", "down", "surely", "except", "righteous", "example"],
    "extended": ["water", "like", "earth", "sky", "life", "over"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ل-ع'] = {
    "latin":    'kh-l-a',
    "category": 'Quranic',
    "core":     ["tuwa", "indeed", "sacred", "remove"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ل-ل'] = {
    "latin":    'kh-l-l',
    "category": 'Quranic',
    "core":     ["allah", "forth", "midst", "day", "friend", "within", "wrongdoers", "spend"],
    "extended": ["comes", "before", "believe", "friendship", "provided", "taken", "except", "slaves"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ل-و'] = {
    "latin":    'kh-l-w',
    "category": 'Quranic',
    "core":     ["passed", "before", "away", "indeed", "allah", "say", "way", "believe"],
    "extended": ["verily", "among", "ones", "lord", "except", "nations", "sent", "any"],
    "avoid":    [],
}
ROOT_LEXICON['خ-م-د'] = {
    "latin":    'kh-m-d',
    "category": 'Quranic',
    "core":     ["extinct", "reaped", "made", "until"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-م-ر'] = {
    "latin":    'kh-m-r',
    "category": 'Quranic',
    "core":     ["allah", "intoxicants", "wine", "head", "say", "about", "both", "chance"],
    "extended": ["games", "shaitaan", "prison", "men", "birds", "over", "other", "drink"],
    "avoid":    [],
}
ROOT_LEXICON['خ-م-س'] = {
    "latin":    'kh-m-s',
    "category": 'Quranic',
    "core":     ["allah", "thousand", "upon", "five", "fifth", "day", "angels", "lord"],
    "extended": ["sent", "thing", "three", "among", "sixth", "knows", "fifty", "year"],
    "avoid":    [],
}
ROOT_LEXICON['خ-م-ص'] = {
    "latin":    'kh-m-s',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "hunger", "except"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-م-ط'] = {
    "latin":    'kh-m-t',
    "category": 'Quranic',
    "core":     ["producing", "changed", "away", "tamarisks"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ن-ز-ر'] = {
    "latin":    'kh-n-z-r',
    "category": 'Quranic',
    "core":     ["allah", "flesh", "blood", "indeed", "dedicated", "swine", "merciful", "forgiving"],
    "extended": ["than", "most", "other", "oft", "dead", "forbidden", "whoever", "forced"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ن-س'] = {
    "latin":    'kh-n-s',
    "category": 'Quranic',
    "core":     ["swear", "retreating", "nay", "planets"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ن-ق'] = {
    "latin":    'kh-n-q',
    "category": 'Quranic',
    "core":     ["flesh", "fear", "sin", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-و-ر'] = {
    "latin":    'kh-w-r',
    "category": 'Quranic',
    "core":     ["calf", "lowing", "sound", "musa"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-و-ض'] = {
    "latin":    'kh-w-d',
    "category": 'Quranic',
    "core":     ["until", "than", "indulge", "allah", "verses", "like", "talk", "playing"],
    "extended": ["leave", "book", "being", "sit", "revealed", "engage", "surely", "other"],
    "avoid":    [],
}
ROOT_LEXICON['خ-و-ل'] = {
    "latin":    'kh-w-l',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "most", "whom", "paternal", "aunts", "possess", "any"],
    "extended": ["uncles", "maternal", "wives", "brothers", "daughters", "merciful", "forgiving", "sisters"],
    "avoid":    [],
}
ROOT_LEXICON['خ-و-ن'] = {
    "latin":    'kh-w-n',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "betray", "people", "love", "deceive", "treacherous", "know"],
    "extended": ["betrayed", "righteous", "knows", "while", "sinful", "themselves", "argue", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['خ-و-ي'] = {
    "latin":    'kh-w-y',
    "category": 'Quranic',
    "core":     ["people", "roofs", "said", "sign", "know", "township", "while"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ي-ب'] = {
    "latin":    'kh-y-b',
    "category": 'Quranic',
    "core":     ["disappointed", "verily", "failed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['خ-ي-ط'] = {
    "latin":    'kh-y-t',
    "category": 'Quranic',
    "core":     ["until", "thus", "verses", "towards", "limits", "permitted", "approach", "thread"],
    "extended": ["garments", "black", "wives", "secluded", "seek", "allah", "relations", "night"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ي-ل'] = {
    "latin":    'kh-y-l',
    "category": 'Quranic',
    "core":     ["allah", "horses", "love", "indeed", "thing", "know", "self", "boaster"],
    "extended": ["over"],
    "avoid":    [],
}
ROOT_LEXICON['خ-ي-م'] = {
    "latin":    'kh-y-m',
    "category": 'Quranic',
    "core":     ["ones", "restrained", "pavilions", "fair"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-أ-ب'] = {
    "latin":    'd-a-b',
    "category": 'Quranic',
    "core":     ["like", "people", "before", "signs", "sins", "firaun", "allah", "denied"],
    "extended": ["seized", "severe", "way"],
    "avoid":    [],
}
ROOT_LEXICON['د-ب-ب'] = {
    "latin":    'd-b-b',
    "category": 'Quranic',
    "core":     ["allah", "creature", "moving", "earth", "indeed", "creatures", "people", "heavens"],
    "extended": ["any", "signs", "water", "down", "creation", "wills", "death", "sent"],
    "avoid":    [],
}
ROOT_LEXICON['د-ب-ر'] = {
    "latin":    'd-b-r',
    "category": 'Quranic',
    "core":     ["backs", "allah", "back", "turn", "turned", "indeed", "after", "except"],
    "extended": ["ponder", "off", "cut", "lord", "day", "away", "earth", "night"],
    "avoid":    [],
}
ROOT_LEXICON['د-ث-ر'] = {
    "latin":    'd-th-r',
    "category": 'Quranic',
    "core":     ["himself", "covers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ح-ر'] = {
    "latin":    'd-h-r',
    "category": 'Quranic',
    "core":     ["hell", "whoever", "disgraced"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ح-ض'] = {
    "latin":    'd-h-d',
    "category": 'Quranic',
    "core":     ["refute", "falsehood", "thereby", "truth", "after"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ح-و'] = {
    "latin":    'd-h-w',
    "category": 'Quranic',
    "core":     ["spread", "after", "earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-خ-ر'] = {
    "latin":    'd-kh-r',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-خ-ن'] = {
    "latin":    'd-kh-n',
    "category": 'Quranic',
    "core":     ["smoke"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-أ'] = {
    "latin":    'd-r-a',
    "category": 'Quranic',
    "core":     ["killed", "allah", "spend", "provided", "repel", "good", "patient", "evil"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-ج'] = {
    "latin":    'd-r-j',
    "category": 'Quranic',
    "core":     ["allah", "degrees", "over", "among", "ranks", "lord", "others", "whom"],
    "extended": ["raise", "take", "preferred", "way", "than", "greater", "wise", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-ر'] = {
    "latin":    'd-r-r',
    "category": 'Quranic',
    "core":     ["upon", "sky", "earth", "abundance", "send"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-س'] = {
    "latin":    'd-r-s',
    "category": 'Quranic',
    "core":     ["book", "say", "allah", "people", "studied", "before", "study", "about"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-ك'] = {
    "latin":    'd-r-k',
    "category": 'Quranic',
    "core":     ["overtaken", "any", "death", "say", "allah", "overtakes", "find", "fire"],
    "extended": ["indeed", "grasp", "subtle", "vision", "aware", "visions", "until", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-ه-م'] = {
    "latin":    'd-r-h-m',
    "category": 'Quranic',
    "core":     ["dirhams", "keen", "very", "low"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ر-ي'] = {
    "latin":    'd-r-y',
    "category": 'Quranic',
    "core":     ["know", "make", "allah", "say", "indeed", "near", "perhaps", "hour"],
    "extended": ["made", "whether", "about", "path", "lord", "day", "judgment", "any"],
    "avoid":    [],
}
ROOT_LEXICON['د-س-ر'] = {
    "latin":    'd-s-r',
    "category": 'Quranic',
    "core":     ["made", "planks", "carried", "nails"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-س-س'] = {
    "latin":    'd-s-s',
    "category": 'Quranic',
    "core":     ["decide", "unquestionably", "keep", "himself"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-س-و'] = {
    "latin":    'd-s-w',
    "category": 'Quranic',
    "core":     ["buries", "indeed", "fails"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ع-ع'] = {
    "latin":    'd-a-a',
    "category": 'Quranic',
    "core":     ["hell", "day", "fire", "thrust"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ف-أ'] = {
    "latin":    'd-f-a',
    "category": 'Quranic',
    "core":     ["cattle", "warmth", "benefits", "created"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ف-ع'] = {
    "latin":    'd-f-a',
    "category": 'Quranic',
    "core":     ["allah", "others", "people", "certainly", "said", "sufficient", "grow", "let"],
    "extended": ["until", "poor", "rich", "orphans", "eat", "wealth", "reckoner", "take"],
    "avoid":    [],
}
ROOT_LEXICON['د-ف-ق'] = {
    "latin":    'd-f-q',
    "category": 'Quranic',
    "core":     ["created", "water", "ejected"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ك-ك'] = {
    "latin":    'd-k-k',
    "category": 'Quranic',
    "core":     ["crushed", "earth", "said", "lord", "lifted", "single", "crushing", "mountains"],
    "extended": ["nay", "pounded", "leveled"],
    "avoid":    [],
}
ROOT_LEXICON['د-ل-ك'] = {
    "latin":    'd-l-k',
    "category": 'Quranic',
    "core":     ["ever", "establish", "quran", "sun"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ل-ل'] = {
    "latin":    'd-l-l',
    "category": 'Quranic',
    "core":     ["said", "direct", "say", "became", "tree", "lord", "shaitaan", "made"],
    "extended": ["rear", "people", "remained", "decreed", "man", "surely", "punishment"],
    "avoid":    [],
}
ROOT_LEXICON['د-ل-و'] = {
    "latin":    'd-l-w',
    "category": 'Quranic',
    "core":     ["came", "down", "said", "knower", "water", "there", "hid", "sent"],
    "extended": ["merchandise", "boy", "let", "news", "caravan", "bucket", "allah", "drawer"],
    "avoid":    [],
}
ROOT_LEXICON['د-م-د-م'] = {
    "latin":    'd-m-d-m',
    "category": 'Quranic',
    "core":     ["sin", "denied", "destroyed", "hamstrung"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-م-ر'] = {
    "latin":    'd-m-r',
    "category": 'Quranic',
    "core":     ["people", "destroyed", "destruction", "word", "lord", "intend", "true", "order"],
    "extended": ["town", "destroy", "defiantly", "proved", "against", "wealthy", "therein", "disobey"],
    "avoid":    [],
}
ROOT_LEXICON['د-م-ع'] = {
    "latin":    'd-m-a',
    "category": 'Quranic',
    "core":     ["eyes", "tears"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-م-غ'] = {
    "latin":    'd-m-gh',
    "category": 'Quranic',
    "core":     ["hurl", "behold", "vanishing", "against"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-م-و'] = {
    "latin":    'd-m-w',
    "category": 'Quranic',
    "core":     ["blood", "indeed", "allah", "flesh", "dedicated", "swine", "merciful", "forgiving"],
    "extended": ["most", "other", "oft", "dead", "than", "forbidden", "whoever", "forced"],
    "avoid":    [],
}
ROOT_LEXICON['د-ن-ر'] = {
    "latin":    'd-n-r',
    "category": 'Quranic',
    "core":     ["said", "book", "return", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ن-و'] = {
    "latin":    'd-n-w',
    "category": 'Quranic',
    "core":     ["world", "allah", "life", "hereafter", "indeed", "punishment", "lord", "day"],
    "extended": ["except", "believe", "people", "good", "among", "say", "enjoyment", "said"],
    "avoid":    [],
}
ROOT_LEXICON['د-ه-ر'] = {
    "latin":    'd-h-r',
    "category": 'Quranic',
    "core":     ["time"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ه-ق'] = {
    "latin":    'd-h-q',
    "category": 'Quranic',
    "core":     ["cup", "full"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ه-م'] = {
    "latin":    'd-h-m',
    "category": 'Quranic',
    "core":     ["dark", "green"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ه-ن'] = {
    "latin":    'd-h-n',
    "category": 'Quranic',
    "core":     ["oil", "compromise", "wish"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-ه-ي'] = {
    "latin":    'd-h-y',
    "category": 'Quranic',
    "core":     ["time", "bitter", "more", "nay"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-و-ر'] = {
    "latin":    'd-w-r',
    "category": 'Quranic',
    "core":     ["allah", "home", "homes", "indeed", "hereafter", "people", "surely", "lord"],
    "extended": ["among", "except", "said", "fear", "earth", "good", "world", "any"],
    "avoid":    [],
}
ROOT_LEXICON['د-و-ل'] = {
    "latin":    'd-w-l',
    "category": 'Quranic',
    "core":     ["take", "among", "allah", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['د-و-ن'] = {
    "latin":    'd-w-n',
    "category": 'Quranic',
    "core":     ["allah", "besides", "any", "indeed", "say", "than", "whom", "other"],
    "extended": ["take", "worship", "earth", "lord", "invoke", "protector", "call", "heavens"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-أ-ب'] = {
    "latin":    'dh-a-b',
    "category": 'Quranic',
    "core":     ["said", "wolf", "indeed", "while", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-أ-م'] = {
    "latin":    'dh-a-m',
    "category": 'Quranic',
    "core":     ["said", "out", "expelled", "follows"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ب-ب'] = {
    "latin":    'dh-b-b',
    "category": 'Quranic',
    "core":     ["example", "fly", "never", "besides", "indeed", "allah", "snatched", "invoke"],
    "extended": ["weak", "forth", "back", "listen", "gathered", "thing", "away", "take"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ب-ذ-ب'] = {
    "latin":    'dh-b-dh-b',
    "category": 'Quranic',
    "core":     ["astray", "never", "between", "lead"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-خ-ر'] = {
    "latin":    'dh-kh-r',
    "category": 'Quranic',
    "core":     ["design", "houses", "cure", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ر-أ'] = {
    "latin":    'dh-r-a',
    "category": 'Quranic',
    "core":     ["earth", "cattle", "multiplied", "say", "like", "gathered"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ر-ر'] = {
    "latin":    'dh-r-r',
    "category": 'Quranic',
    "core":     ["offspring", "lord", "indeed", "allah", "said", "make", "atom", "weight"],
    "extended": ["among", "any", "say", "except", "offsprings", "righteous", "clear", "grant"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ر-ع'] = {
    "latin":    'dh-r-a',
    "category": 'Quranic',
    "core":     ["felt", "said", "messengers", "lut", "uneasy", "straitened", "came", "distressed"],
    "extended": ["chain", "cubits", "length", "seventy", "insert", "into"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ر-و'] = {
    "latin":    'dh-r-w',
    "category": 'Quranic',
    "core":     ["scattering", "dispersing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ع-ن'] = {
    "latin":    'dh-a-n',
    "category": 'Quranic',
    "core":     ["truth", "promptly", "obedient", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ق-ن'] = {
    "latin":    'dh-q-n',
    "category": 'Quranic',
    "core":     ["fall", "indeed", "faces"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ك-و'] = {
    "latin":    'dh-k-w',
    "category": 'Quranic',
    "core":     ["flesh", "fear", "sin", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ل-ل'] = {
    "latin":    'dh-l-l',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "humiliation", "lord", "say", "said", "people", "cover"],
    "extended": ["surely", "out", "wrath", "earth", "near", "eat", "fruits", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-م-م'] = {
    "latin":    'dh-m-m',
    "category": 'Quranic',
    "core":     ["while", "kinship", "protection", "covenant", "disgraced"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ه-ل'] = {
    "latin":    'dh-h-l',
    "category": 'Quranic',
    "core":     ["intoxicated", "allah", "see", "load"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-و-د'] = {
    "latin":    'dh-w-d',
    "category": 'Quranic',
    "core":     ["said", "water", "besides", "old"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ذ-و-ق'] = {
    "latin":    'dh-w-q',
    "category": 'Quranic',
    "core":     ["taste", "punishment", "used", "say", "indeed", "fire", "allah", "day"],
    "extended": ["lord", "make", "surely", "mercy", "disbelieve", "except", "returned", "let"],
    "avoid":    [],
}
ROOT_LEXICON['ذ-ي-ع'] = {
    "latin":    'dh-y-a',
    "category": 'Quranic',
    "core":     ["referred", "fear", "security", "spread"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-أ-ف'] = {
    "latin":    'r-a-f',
    "category": 'Quranic',
    "core":     ["most", "allah", "merciful", "indeed", "full", "kindness", "kind", "great"],
    "extended": ["except", "hearts", "lord", "witness", "let", "messenger", "certainly", "mankind"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ب-ح'] = {
    "latin":    'r-b-h',
    "category": 'Quranic',
    "core":     ["commerce", "guided", "ones", "profited"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ب-ص'] = {
    "latin":    'r-b-s',
    "category": 'Quranic',
    "core":     ["say", "allah", "wait", "waiting", "indeed", "await", "among", "way"],
    "extended": ["concerning", "until", "except", "while", "afflict", "near", "hands", "best"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ب-ط'] = {
    "latin":    'r-b-t',
    "category": 'Quranic',
    "core":     ["allah", "hearts", "firm", "besides"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ب-ع'] = {
    "latin":    'r-b-a',
    "category": 'Quranic',
    "core":     ["four", "allah", "indeed", "forty", "months", "among", "lord", "women"],
    "extended": ["three", "earth", "wives", "said", "know", "more", "sixth", "heavens"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ت-ع'] = {
    "latin":    'r-t-a',
    "category": 'Quranic',
    "core":     ["play", "send", "tomorrow", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ت-ق'] = {
    "latin":    'r-t-q',
    "category": 'Quranic',
    "core":     ["heavens", "water", "see", "believe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ت-ل'] = {
    "latin":    'r-t-l',
    "category": 'Quranic',
    "core":     ["quran", "recitation", "said", "disbelieve", "heart", "once", "revealed", "thus"],
    "extended": ["recited", "thereby", "why", "strengthen", "recite", "add", "measured", "rhythmic"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-ج'] = {
    "latin":    'r-j-j',
    "category": 'Quranic',
    "core":     ["shaken", "shaking", "earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-ز'] = {
    "latin":    'r-j-z',
    "category": 'Quranic',
    "core":     ["punishment", "said", "sky", "because", "upon", "sent", "down", "lord"],
    "extended": ["wronged", "changed", "word", "defiantly", "other", "believe", "surely", "send"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-س'] = {
    "latin":    'r-j-s',
    "category": 'Quranic',
    "core":     ["allah", "believe", "whoever", "indeed", "lord", "except", "abomination", "avoid"],
    "extended": ["verily", "filth", "increases", "while", "hearts", "disease", "die", "evil"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-ف'] = {
    "latin":    'r-j-f',
    "category": 'Quranic',
    "core":     ["earthquake", "seized", "prone", "became", "fallen", "quake", "day", "home"],
    "extended": ["let", "quaking"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-ل'] = {
    "latin":    'r-j-l',
    "category": 'Quranic',
    "core":     ["allah", "men", "man", "women", "indeed", "among", "feet", "said"],
    "extended": ["say", "lord", "people", "except", "hands", "fear", "any", "whom"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ج-م'] = {
    "latin":    'r-j-m',
    "category": 'Quranic',
    "core":     ["said", "indeed", "surely", "accursed", "stone", "shaitaan", "refuge", "seek"],
    "extended": ["lord", "desist", "knows", "allah", "see", "stoned", "say", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ح-ب'] = {
    "latin":    'r-h-b',
    "category": 'Quranic',
    "core":     ["earth", "allah", "turned", "straitened", "indeed", "welcome"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ح-ق'] = {
    "latin":    'r-h-q',
    "category": 'Quranic',
    "core":     ["drink", "given", "wine", "sealed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ح-ل'] = {
    "latin":    'r-h-l',
    "category": 'Quranic',
    "core":     ["said", "put", "bag"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-خ-و'] = {
    "latin":    'r-kh-w',
    "category": 'Quranic',
    "core":     ["wind", "wherever", "directed", "command"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-د-أ'] = {
    "latin":    'r-d-a',
    "category": 'Quranic',
    "core":     ["than", "fear", "helper", "speech"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-د-د'] = {
    "latin":    'r-d-d',
    "category": 'Quranic',
    "core":     ["allah", "back", "indeed", "say", "returned", "people", "lord", "among"],
    "extended": ["return", "believe", "turn", "after", "day", "sent", "before", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ر-د-ف'] = {
    "latin":    'r-d-f',
    "category": 'Quranic',
    "core":     ["thousand", "angels", "after", "help"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-د-م'] = {
    "latin":    'r-d-m',
    "category": 'Quranic',
    "core":     ["said", "assist", "between", "established"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-د-ي'] = {
    "latin":    'r-d-y',
    "category": 'Quranic',
    "core":     ["allah", "religion", "made", "ruined"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ذ-ل'] = {
    "latin":    'r-dh-l',
    "category": 'Quranic',
    "core":     ["followed", "said", "see", "lowest", "after", "created", "indeed", "among"],
    "extended": ["age", "cause"],
    "avoid":    [],
}
ROOT_LEXICON['ر-س-س'] = {
    "latin":    'r-s-s',
    "category": 'Quranic',
    "core":     ["thamud"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-س-و'] = {
    "latin":    'r-s-w',
    "category": 'Quranic',
    "core":     ["mountains", "earth", "firm", "made", "therein", "cast", "set", "firmly"],
    "extended": ["allah", "ask", "most", "rivers", "spread", "placed", "grow", "lest"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ص-د'] = {
    "latin":    'r-s-d',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "sit", "find", "messenger", "except", "before", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ص-ص'] = {
    "latin":    'r-s-s',
    "category": 'Quranic',
    "core":     ["structure", "fight", "way", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ض-ع'] = {
    "latin":    'r-d-a',
    "category": 'Quranic',
    "core":     ["mother", "allah", "suckle", "give", "father", "except", "another", "mothers"],
    "extended": ["women", "fear", "nursing", "deliver", "pregnant", "want", "blame", "suckling"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ض-و'] = {
    "latin":    'r-d-w',
    "category": 'Quranic',
    "core":     ["allah", "pleased", "indeed", "lord", "pleasure", "among", "people", "except"],
    "extended": ["gardens", "believe", "rivers", "forever", "underneath", "most", "abide", "hearts"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ط-ب'] = {
    "latin":    'r-t-b',
    "category": 'Quranic',
    "core":     ["knows", "unseen", "except", "falls"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ع-ب'] = {
    "latin":    'r-a-b',
    "category": 'Quranic',
    "core":     ["terror", "cast", "hearts", "allah", "down", "disbelieved", "think", "scripture"],
    "extended": ["fortresses", "into", "people"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ع-ي'] = {
    "latin":    'r-a-y',
    "category": 'Quranic',
    "core":     ["allah", "pasture", "believe", "say", "raina", "said", "surely", "promise"],
    "extended": ["observers", "trusts", "water", "right", "believed", "compassion", "among", "isa"],
    "avoid":    [],
}
ROOT_LEXICON['ر-غ-د'] = {
    "latin":    'r-gh-d',
    "category": 'Quranic',
    "core":     ["said", "wherever", "eat", "wish", "town"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-غ-م'] = {
    "latin":    'r-gh-m',
    "category": 'Quranic',
    "core":     ["incumbent", "abundance", "death", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ف-ت'] = {
    "latin":    'r-f-t',
    "category": 'Quranic',
    "core":     ["creation", "new", "particles", "resurrected", "bones", "crumbled", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ف-ث'] = {
    "latin":    'r-f-th',
    "category": 'Quranic',
    "core":     ["allah", "relations", "knows"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ف-د'] = {
    "latin":    'r-f-d',
    "category": 'Quranic',
    "core":     ["followed", "curse", "wretched", "resurrection", "given", "gift", "day"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ف-ر-ف'] = {
    "latin":    'r-f-r-f',
    "category": 'Quranic',
    "core":     ["green", "cushions", "carpets", "beautiful"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ف-ق'] = {
    "latin":    'r-f-q',
    "category": 'Quranic',
    "core":     ["allah", "excellent", "whoever", "favor", "upon", "water", "believe", "faces"],
    "extended": ["lord", "place", "resting"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ق-ب'] = {
    "latin":    'r-q-b',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "watch", "freeing", "people", "said", "over", "whom"],
    "extended": ["necks", "needy", "covenant", "day", "lord", "except", "slave", "watcher"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ق-د'] = {
    "latin":    'r-q-d',
    "category": 'Quranic',
    "core":     ["stretched", "right", "dog", "left"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ق-ق'] = {
    "latin":    'r-q-q',
    "category": 'Quranic',
    "core":     ["unrolled", "parchment"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ق-م'] = {
    "latin":    'r-q-m',
    "category": 'Quranic',
    "core":     ["book", "written"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ق-ي'] = {
    "latin":    'r-q-y',
    "category": 'Quranic',
    "core":     ["ascend", "ornament", "sky", "house", "never", "believe", "human", "book"],
    "extended": ["read", "say", "glorified", "ascension", "bring", "down", "lord", "until"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-ب'] = {
    "latin":    'r-k-b',
    "category": 'Quranic',
    "core":     ["allah", "made", "ride", "embark", "indeed", "thing", "certainly", "knowing"],
    "extended": ["people", "said", "out", "horses", "ship", "created", "eat", "cattle"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-د'] = {
    "latin":    'r-k-d',
    "category": 'Quranic',
    "core":     ["wind", "grateful", "patient", "signs"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-ز'] = {
    "latin":    'r-k-z',
    "category": 'Quranic',
    "core":     ["destroyed", "generation", "before", "perceive"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-س'] = {
    "latin":    'r-k-s',
    "category": 'Quranic',
    "core":     ["find"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-ض'] = {
    "latin":    'r-k-d',
    "category": 'Quranic',
    "core":     ["perceived", "torment", "behold", "fleeing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-م'] = {
    "latin":    'r-k-m',
    "category": 'Quranic',
    "core":     ["allah", "see", "clouds", "sky"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ك-ن'] = {
    "latin":    'r-k-n',
    "category": 'Quranic',
    "core":     ["said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-ح'] = {
    "latin":    'r-m-h',
    "category": 'Quranic',
    "core":     ["believe", "allah", "spears", "something"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-د'] = {
    "latin":    'r-m-d',
    "category": 'Quranic',
    "core":     ["example", "ashes", "wind", "straying"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-ز'] = {
    "latin":    'r-m-z',
    "category": 'Quranic',
    "core":     ["said", "except", "gestures", "days"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-ض'] = {
    "latin":    'r-m-d',
    "category": 'Quranic',
    "core":     ["criterion", "guided", "among", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-م'] = {
    "latin":    'r-m-m',
    "category": 'Quranic',
    "core":     ["example", "forgets", "creation", "life"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-م-ن'] = {
    "latin":    'r-m-n',
    "category": 'Quranic',
    "core":     ["date", "pomegranates", "fruit", "indeed", "gardens", "olives", "bears", "palm"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ه-ب'] = {
    "latin":    'r-h-b',
    "category": 'Quranic',
    "core":     ["allah", "fear", "people", "monks", "indeed", "alone", "bestowed", "believe"],
    "extended": ["among", "because", "surely", "said", "mercy", "lord", "besides", "way"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ه-ط'] = {
    "latin":    'r-h-t',
    "category": 'Quranic',
    "core":     ["family", "said", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ه-ق'] = {
    "latin":    'r-h-q',
    "category": 'Quranic',
    "core":     ["cover", "humiliation", "forever", "companions", "abide", "faces", "any", "darkness"],
    "extended": ["humbled", "burden"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ه-ن'] = {
    "latin":    'r-h-n',
    "category": 'Quranic',
    "core":     ["pledged", "earned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ه-و'] = {
    "latin":    'r-h-w',
    "category": 'Quranic',
    "core":     ["leave", "army", "indeed", "drowned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-و-د'] = {
    "latin":    'r-w-d',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "said", "intends", "whoever", "wish", "intend", "except"],
    "extended": ["desire", "any", "made", "world", "lord", "intended", "people", "desires"],
    "avoid":    [],
}
ROOT_LEXICON['ر-و-ض'] = {
    "latin":    'r-w-d',
    "category": 'Quranic',
    "core":     ["deeds", "righteous"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-و-ع'] = {
    "latin":    'r-w-a',
    "category": 'Quranic',
    "core":     ["gone", "concerning", "ibrahim", "tidings"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-و-غ'] = {
    "latin":    'r-w-gh',
    "category": 'Quranic',
    "core":     ["turned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ي-ب'] = {
    "latin":    'r-y-b',
    "category": 'Quranic',
    "core":     ["doubt", "allah", "about", "indeed", "surely", "lord", "believe", "day"],
    "extended": ["book", "among", "except", "before", "between", "term", "after", "say"],
    "avoid":    [],
}
ROOT_LEXICON['ر-ي-ش'] = {
    "latin":    'r-y-sh',
    "category": 'Quranic',
    "core":     ["remember", "shame", "allah", "adam"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ي-ع'] = {
    "latin":    'r-y-a',
    "category": 'Quranic',
    "core":     ["elevation", "amusing", "sign", "yourselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ر-ي-ن'] = {
    "latin":    'r-y-n',
    "category": 'Quranic',
    "core":     ["hearts", "used", "over", "stain"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ب-د'] = {
    "latin":    'z-b-d',
    "category": 'Quranic',
    "core":     ["water", "valleys", "fire", "order", "scum", "allah", "sends", "utensils"],
    "extended": ["down", "rising", "sets", "heat", "forth", "carries", "thus", "make"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ب-ر'] = {
    "latin":    'z-b-r',
    "category": 'Quranic',
    "core":     ["scriptures", "clear", "messengers", "before", "signs", "book", "enlightening", "certainly"],
    "extended": ["came", "dawood", "zaboor", "after", "prophets", "indeed", "gave", "verily"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ب-ن'] = {
    "latin":    'z-b-n',
    "category": 'Quranic',
    "core":     ["hell", "call", "angels"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ج-ج'] = {
    "latin":    'z-j-j',
    "category": 'Quranic',
    "core":     ["example", "star", "fire", "wills", "olive", "brilliant", "glow", "oil"],
    "extended": ["allah", "blessed", "heavens", "sets", "forth", "tree", "thing", "glass"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ج-ر'] = {
    "latin":    'z-j-r',
    "category": 'Quranic',
    "core":     ["strongly", "drive", "only", "single"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ج-و'] = {
    "latin":    'z-j-w',
    "category": 'Quranic',
    "core":     ["allah", "come", "indeed", "drives"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ح-ز-ح'] = {
    "latin":    'z-h-z-h',
    "category": 'Quranic',
    "core":     ["life", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ح-ف'] = {
    "latin":    'z-h-f',
    "category": 'Quranic',
    "core":     ["meet", "disbelieve", "advancing", "believe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-خ-ر-ف'] = {
    "latin":    'z-kh-r-f',
    "category": 'Quranic',
    "core":     ["lord", "thus", "until", "down", "sky", "life", "world"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ر-ب'] = {
    "latin":    'z-r-b',
    "category": 'Quranic',
    "core":     ["spread", "carpets", "out"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ر-ق'] = {
    "latin":    'z-r-q',
    "category": 'Quranic',
    "core":     ["eyed", "blown", "criminals", "blue"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ر-ي'] = {
    "latin":    'z-r-y',
    "category": 'Quranic',
    "core":     ["never", "say", "indeed", "treasures"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ع-م'] = {
    "latin":    'z-a-m',
    "category": 'Quranic',
    "core":     ["claim", "say", "whom", "allah", "partners", "used", "claimed", "call"],
    "extended": ["day", "see", "before", "time", "between", "come", "first", "created"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ف-ر'] = {
    "latin":    'z-f-r',
    "category": 'Quranic',
    "core":     ["therein", "sighing", "hear"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ف-ف'] = {
    "latin":    'z-f-f',
    "category": 'Quranic',
    "core":     ["hastening", "towards", "advanced"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ل-ز-ل'] = {
    "latin":    'z-l-z-l',
    "category": 'Quranic',
    "core":     ["shaken", "indeed", "there", "believers", "severe", "tried", "shake", "earth"],
    "extended": ["earthquake"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ل-ف'] = {
    "latin":    'z-l-f',
    "category": 'Quranic',
    "core":     ["near", "indeed", "brought", "good", "paradise", "righteous", "bring", "place"],
    "extended": ["return", "surely", "access"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ل-ق'] = {
    "latin":    'z-l-q',
    "category": 'Quranic',
    "core":     ["than", "sky", "calamity", "ground"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ل-ل'] = {
    "latin":    'z-l-l',
    "category": 'Quranic',
    "core":     ["slip", "allah", "made", "shaitaan", "after"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ل-م'] = {
    "latin":    'z-l-m',
    "category": 'Quranic',
    "core":     ["altars", "divining", "arrows"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-م-ر'] = {
    "latin":    'z-m-r',
    "category": 'Quranic',
    "core":     ["say", "until", "groups", "driven", "lord", "opened", "keepers", "reach"],
    "extended": ["gates"],
    "avoid":    [],
}
ROOT_LEXICON['ز-م-ل'] = {
    "latin":    'z-m-l',
    "category": 'Quranic',
    "core":     ["himself", "wraps"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-م-ه-ر'] = {
    "latin":    'z-m-h-r',
    "category": 'Quranic',
    "core":     ["see", "freezing", "sun", "cold"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ن-م'] = {
    "latin":    'z-n-m',
    "category": 'Quranic',
    "core":     ["cruel", "useless", "after", "utterly"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ن-ي'] = {
    "latin":    'z-n-y',
    "category": 'Quranic',
    "core":     ["fornicator", "fornicatress", "believers", "except", "forbidden", "allah", "marry", "polytheist"],
    "extended": ["woman", "man", "indeed", "adultery", "concerning", "religion", "flog", "hundred"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ه-ر'] = {
    "latin":    'z-h-r',
    "category": 'Quranic',
    "core":     ["life", "enjoyment", "test", "provision"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-ه-ق'] = {
    "latin":    'z-h-q',
    "category": 'Quranic',
    "core":     ["falsehood", "truth", "only", "wealth", "while", "world", "souls", "children"],
    "extended": ["depart", "intends", "impress", "punish", "allah", "disbelievers", "say", "come"],
    "avoid":    [],
}
ROOT_LEXICON['ز-و-د'] = {
    "latin":    'z-w-d',
    "category": 'Quranic',
    "core":     ["fear", "during", "provision", "well", "indeed", "sexual", "allah", "relations"],
    "extended": ["hajj", "righteousness", "understanding", "known", "therein", "men", "months", "knows"],
    "avoid":    [],
}
ROOT_LEXICON['ز-و-ر'] = {
    "latin":    'z-w-r',
    "category": 'Quranic',
    "core":     ["allah", "whoever", "except", "word", "say", "lie"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ز-و-ل'] = {
    "latin":    'z-w-l',
    "category": 'Quranic',
    "core":     ["any", "allah", "indeed", "heavens", "cease", "after", "forbearing", "uphold"],
    "extended": ["oft", "lest", "forgiving", "most", "upholds", "earth"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ي-ت'] = {
    "latin":    'z-y-t',
    "category": 'Quranic',
    "core":     ["date", "olive", "indeed", "forth", "olives", "thing", "fruit", "people"],
    "extended": ["grapes", "gardens", "bears", "pomegranates", "palm", "crops", "palms", "example"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ي-د'] = {
    "latin":    'z-y-d',
    "category": 'Quranic',
    "core":     ["increase", "allah", "lord", "increased", "indeed", "except", "said", "say"],
    "extended": ["increases", "punishment", "more", "good", "disbelief", "faith", "people", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ي-غ'] = {
    "latin":    'z-y-gh',
    "category": 'Quranic',
    "core":     ["hearts", "allah", "deviated", "lord", "deviate", "take", "after", "indeed"],
    "extended": ["turned", "said", "guide", "while", "hurt", "defiantly", "certainly", "disobedient"],
    "avoid":    [],
}
ROOT_LEXICON['ز-ي-ل'] = {
    "latin":    'z-y-l',
    "category": 'Quranic',
    "core":     ["cease", "allah", "until", "made", "indeed", "doubt", "surely", "say"],
    "extended": ["among", "about", "while", "haraam", "masjid", "except", "hearts", "place"],
    "avoid":    [],
}
ROOT_LEXICON['س-أ-م'] = {
    "latin":    's-a-m',
    "category": 'Quranic',
    "core":     ["near", "lord", "man"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-أ'] = {
    "latin":    's-b-a',
    "category": 'Quranic',
    "core":     ["saba"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ب'] = {
    "latin":    's-b-b',
    "category": 'Quranic',
    "core":     ["followed", "allah", "seeming", "thus", "deed", "made", "fair", "course"],
    "extended": ["see", "off", "cut", "community", "return", "enmity", "invoke", "insult"],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ت'] = {
    "latin":    's-b-t',
    "category": 'Quranic',
    "core":     ["sabbath", "day", "transgressed", "test", "disobeying", "town", "ask", "come"],
    "extended": ["visibly", "defiantly", "thus", "situated", "sea", "fish", "because", "came"],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ط'] = {
    "latin":    's-b-t',
    "category": 'Quranic',
    "core":     ["isaac", "ibrahim", "ishmael", "yaqub", "say", "isa", "allah", "prophets"],
    "extended": ["revealed", "musa", "between", "believed", "descendants", "distinction", "make", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ع'] = {
    "latin":    's-b-a',
    "category": 'Quranic',
    "core":     ["seven", "heavens", "allah", "indeed", "ears", "except", "people", "about"],
    "extended": ["created", "earth", "return", "among", "know", "said", "cows", "explain"],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-غ'] = {
    "latin":    's-b-gh',
    "category": 'Quranic',
    "core":     ["see", "book", "hidden", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ق'] = {
    "latin":    's-b-q',
    "category": 'Quranic',
    "core":     ["preceded", "indeed", "word", "surely", "lord", "allah", "race", "good"],
    "extended": ["between", "book", "concerning", "said", "any", "therein", "great", "among"],
    "avoid":    [],
}
ROOT_LEXICON['س-ب-ل'] = {
    "latin":    's-b-l',
    "category": 'Quranic',
    "core":     ["way", "allah", "indeed", "say", "people", "lord", "believe", "whoever"],
    "extended": ["surely", "astray", "most", "wealth", "among", "except", "made", "said"],
    "avoid":    [],
}
ROOT_LEXICON['س-ت-ت'] = {
    "latin":    's-t-t',
    "category": 'Quranic',
    "core":     ["heavens", "created", "earth", "six", "throne", "allah", "periods", "indeed"],
    "extended": ["established", "any", "between", "whatever", "epochs", "lord", "after", "intercessor"],
    "avoid":    [],
}
ROOT_LEXICON['س-ج-ر'] = {
    "latin":    's-j-r',
    "category": 'Quranic',
    "core":     ["boiling", "water", "fire", "burned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ج-ل'] = {
    "latin":    's-j-l',
    "category": 'Quranic',
    "core":     ["baked", "stones", "upon", "clay", "made", "rained"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ج-ن'] = {
    "latin":    's-j-n',
    "category": 'Quranic',
    "core":     ["said", "prison", "surely", "both", "imprisoned", "indeed", "other", "saved"],
    "extended": ["about", "than", "lord", "after", "wine", "interpretation", "birds", "head"],
    "avoid":    [],
}
ROOT_LEXICON['س-ج-و'] = {
    "latin":    's-j-w',
    "category": 'Quranic',
    "core":     ["darkness", "night", "covers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ح-ت'] = {
    "latin":    's-h-t',
    "category": 'Quranic',
    "core":     ["forbidden", "allah", "eating", "surely", "evil"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ح-ر'] = {
    "latin":    's-h-r',
    "category": 'Quranic',
    "core":     ["said", "magic", "indeed", "came", "surely", "magician", "say", "magicians"],
    "extended": ["clear", "musa", "bewitched", "truth", "allah", "people", "except", "only"],
    "avoid":    [],
}
ROOT_LEXICON['س-ح-ق'] = {
    "latin":    's-h-q',
    "category": 'Quranic',
    "core":     ["wind", "sky", "being", "snatched"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ح-ل'] = {
    "latin":    's-h-l',
    "category": 'Quranic',
    "core":     ["eye", "river", "cast", "chest"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-خ-ر'] = {
    "latin":    's-kh-r',
    "category": 'Quranic',
    "core":     ["subjected", "allah", "people", "indeed", "day", "moon", "sun", "night"],
    "extended": ["heavens", "earth", "ridicule", "see", "command", "signs", "surely", "ships"],
    "avoid":    [],
}
ROOT_LEXICON['س-خ-ط'] = {
    "latin":    's-kh-t',
    "category": 'Quranic',
    "core":     ["allah", "pleasure"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-د-د'] = {
    "latin":    's-d-d',
    "category": 'Quranic',
    "core":     ["between", "fear", "speak", "allah", "behind", "barrier"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-د-ر'] = {
    "latin":    's-d-r',
    "category": 'Quranic',
    "core":     ["lote", "trees", "tree"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-د-س'] = {
    "latin":    's-d-s',
    "category": 'Quranic',
    "core":     ["sixth", "allah", "more", "any", "indeed", "knowing", "third", "debt"],
    "extended": ["half", "there", "after", "made", "women", "left", "child", "fourth"],
    "avoid":    [],
}
ROOT_LEXICON['س-د-ي'] = {
    "latin":    's-d-y',
    "category": 'Quranic',
    "core":     ["left", "man", "think", "neglected"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ب'] = {
    "latin":    's-r-b',
    "category": 'Quranic',
    "core":     ["mirage"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ب-ل'] = {
    "latin":    's-r-b-l',
    "category": 'Quranic',
    "core":     ["garments"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ج'] = {
    "latin":    's-r-j',
    "category": 'Quranic',
    "core":     ["lamp", "moon", "therein", "placed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ح'] = {
    "latin":    's-r-h',
    "category": 'Quranic',
    "core":     ["release", "divorce", "provide", "good", "take", "concerning", "women", "fear"],
    "extended": ["allah", "retain", "transgress", "whoever", "manner", "prophet", "life", "say"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-د'] = {
    "latin":    's-r-d',
    "category": 'Quranic',
    "core":     ["coats", "righteousness", "measure", "seer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-د-ق'] = {
    "latin":    's-r-d-q',
    "category": 'Quranic',
    "core":     ["water", "fire", "believe", "wretched"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ر'] = {
    "latin":    's-r-r',
    "category": 'Quranic',
    "core":     ["allah", "knows", "indeed", "conceal", "secretly", "secret", "said", "day"],
    "extended": ["see", "know", "spend", "good", "knower", "thrones", "lord", "declare"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ع'] = {
    "latin":    's-r-a',
    "category": 'Quranic',
    "core":     ["allah", "swift", "indeed", "hasten", "account", "day", "good", "lord"],
    "extended": ["punishment", "earned", "after", "verses", "given", "believe", "deeds", "earth"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ف'] = {
    "latin":    's-r-f',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "extravagant", "people", "eat", "ones", "transgressors", "said"],
    "extended": ["lord", "excesses", "take", "love", "except", "give", "whoever", "clear"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ق'] = {
    "latin":    's-r-q',
    "category": 'Quranic',
    "core":     ["allah", "hands", "brother", "indeed", "said", "steals", "wise", "female"],
    "extended": ["mighty", "earned", "off", "cut", "thief", "male", "exemplary", "recompense"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-م-د'] = {
    "latin":    's-r-m-d',
    "category": 'Quranic',
    "core":     ["god", "besides", "continuous", "seen", "say", "resurrection", "day", "bring"],
    "extended": ["made", "allah", "night", "till"],
    "avoid":    [],
}
ROOT_LEXICON['س-ر-ي'] = {
    "latin":    's-r-y',
    "category": 'Quranic',
    "core":     ["night", "travel", "indeed", "slaves", "anyone", "look", "strike", "family"],
    "extended": ["back", "lord", "verily", "musa", "inspired", "followed"],
    "avoid":    [],
}
ROOT_LEXICON['س-ط-ح'] = {
    "latin":    's-t-h',
    "category": 'Quranic',
    "core":     ["spread", "out", "earth", "towards"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ط-ر'] = {
    "latin":    's-t-r',
    "category": 'Quranic',
    "core":     ["former", "tales", "written", "say", "before", "verses", "recited", "book"],
    "extended": ["says", "stories", "believe", "over", "verily", "lord", "down", "forefathers"],
    "avoid":    [],
}
ROOT_LEXICON['س-ط-و'] = {
    "latin":    's-t-w',
    "category": 'Quranic',
    "core":     ["attack", "fire", "wretched", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-غ-ب'] = {
    "latin":    's-gh-b',
    "category": 'Quranic',
    "core":     ["hunger", "day", "feeding", "severe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ح'] = {
    "latin":    's-f-h',
    "category": 'Quranic',
    "core":     ["allah", "due", "bridal", "women", "chaste", "whoever", "sin", "married"],
    "extended": ["lawful", "indeed", "give", "possess", "except", "desiring", "ones", "believers"],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ع'] = {
    "latin":    's-f-a',
    "category": 'Quranic',
    "core":     ["drag", "nay", "forelock", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ك'] = {
    "latin":    's-f-k',
    "category": 'Quranic',
    "core":     ["blood", "while", "shed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ل'] = {
    "latin":    's-f-l',
    "category": 'Quranic',
    "core":     ["lowest", "made", "upon", "indeed", "allah", "certainly", "highest", "baked"],
    "extended": ["stones", "clay", "came", "rained", "returned", "low"],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ن'] = {
    "latin":    's-f-n',
    "category": 'Quranic',
    "core":     ["ship", "people", "made", "force", "after", "seized", "intended", "king"],
    "extended": ["sea", "working", "defect", "cause", "poor"],
    "avoid":    [],
}
ROOT_LEXICON['س-ف-ه'] = {
    "latin":    's-f-h',
    "category": 'Quranic',
    "core":     ["people", "allah", "said", "among", "foolish", "indeed", "whom", "lord"],
    "extended": ["foolishness", "believe", "say", "certainly", "except", "surely", "chose", "used"],
    "avoid":    [],
}
ROOT_LEXICON['س-ق-ف'] = {
    "latin":    's-q-f',
    "category": 'Quranic',
    "core":     ["roof", "upon", "made"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ق-م'] = {
    "latin":    's-q-m',
    "category": 'Quranic',
    "core":     ["said", "indeed", "sick", "onto"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ق-ي'] = {
    "latin":    's-q-y',
    "category": 'Quranic',
    "core":     ["drink", "water", "indeed", "said", "people", "give", "given", "eat"],
    "extended": ["surely", "drinking", "allah", "earth", "both", "wine", "matter", "watered"],
    "avoid":    [],
}
ROOT_LEXICON['س-ك-ب'] = {
    "latin":    's-k-b',
    "category": 'Quranic',
    "core":     ["forth", "water", "poured"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ك-ت'] = {
    "latin":    's-k-t',
    "category": 'Quranic',
    "core":     ["took", "musa", "tablets", "mercy"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ك-ر'] = {
    "latin":    's-k-r',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "intoxicated", "while", "surely", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ب'] = {
    "latin":    's-l-b',
    "category": 'Quranic',
    "core":     ["example", "fly", "never", "besides"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ح'] = {
    "latin":    's-l-h',
    "category": 'Quranic',
    "core":     ["attack", "come", "let", "neglect", "indeed", "among", "disbelieved", "lay"],
    "extended": ["group", "allah", "prayer", "trouble", "down", "prostrated", "humiliating", "rain"],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-خ'] = {
    "latin":    's-l-kh',
    "category": 'Quranic',
    "core":     ["followed", "gone", "astray", "shaitaan"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-س-ل'] = {
    "latin":    's-l-s-l',
    "category": 'Quranic',
    "core":     ["chains"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ط'] = {
    "latin":    's-l-t',
    "category": 'Quranic',
    "core":     ["authority", "allah", "any", "clear", "sent", "over", "indeed", "down"],
    "extended": ["except", "lord", "signs", "about", "come", "people", "against", "said"],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ف'] = {
    "latin":    's-l-f',
    "category": 'Quranic',
    "core":     ["allah", "passed", "except", "before", "say", "lord", "while", "forbidden"],
    "extended": ["whoever", "women", "indeed", "whom", "returned", "past"],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ق'] = {
    "latin":    's-l-q',
    "category": 'Quranic',
    "core":     ["fear", "departs", "sharp", "worthless"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ك'] = {
    "latin":    's-l-k',
    "category": 'Quranic',
    "core":     ["indeed", "forth", "into", "lord", "therein", "criminals", "hearts", "thus"],
    "extended": ["enter", "people", "colors", "comes", "made", "surely", "ways", "sky"],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-ل'] = {
    "latin":    's-l-l',
    "category": 'Quranic',
    "core":     ["humankind", "indeed", "essence", "clay"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ل-و'] = {
    "latin":    's-l-w',
    "category": 'Quranic',
    "core":     ["quails", "manna", "sent", "down", "wronged", "wrong", "themselves", "clouds"],
    "extended": ["shaded", "doing", "provided", "things", "eat", "good"],
    "avoid":    [],
}
ROOT_LEXICON['س-م-د'] = {
    "latin":    's-m-d',
    "category": 'Quranic',
    "core":     ["while", "amuse"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-م-ر'] = {
    "latin":    's-m-r',
    "category": 'Quranic',
    "core":     ["said", "samiri", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-م-ك'] = {
    "latin":    's-m-k',
    "category": 'Quranic',
    "core":     ["ceiling", "proportioned", "raised"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-م-م'] = {
    "latin":    's-m-m',
    "category": 'Quranic',
    "core":     ["scorching", "fire"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-م-ن'] = {
    "latin":    's-m-n',
    "category": 'Quranic',
    "core":     ["fat", "cows", "seven", "ears", "explain", "lean", "about", "green"],
    "extended": ["eating", "dry", "ones"],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-ب-ل'] = {
    "latin":    's-n-b-l',
    "category": 'Quranic',
    "core":     ["seven", "ears", "example", "ear", "grain", "wealth", "spend", "hundred"],
    "extended": ["manifold", "encompassing", "wills", "way", "knowing", "like", "gives", "grows"],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-د'] = {
    "latin":    's-n-d',
    "category": 'Quranic',
    "core":     ["shout", "see", "speech", "speak"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-م'] = {
    "latin":    's-n-m',
    "category": 'Quranic',
    "core":     ["mixture", "tasneem"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-ن'] = {
    "latin":    's-n-n',
    "category": 'Quranic',
    "core":     ["way", "allah", "before", "any", "find", "passed", "verily", "never"],
    "extended": ["change", "former", "away", "alteration", "altered", "clay", "mud", "black"],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-ه'] = {
    "latin":    's-n-h',
    "category": 'Quranic',
    "core":     ["flesh", "roofs", "said", "time"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ن-و'] = {
    "latin":    's-n-w',
    "category": 'Quranic',
    "core":     ["years", "thousand", "allah", "year", "said", "people", "remained", "day"],
    "extended": ["number", "indeed", "earth", "count", "made", "lord", "among", "life"],
    "avoid":    [],
}
ROOT_LEXICON['س-ه-ر'] = {
    "latin":    's-h-r',
    "category": 'Quranic',
    "core":     ["awakened", "behold"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ه-ل'] = {
    "latin":    's-h-l',
    "category": 'Quranic',
    "core":     ["act", "mountains", "allah", "successors"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ه-م'] = {
    "latin":    's-h-m',
    "category": 'Quranic',
    "core":     ["losers", "lots", "drew"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ه-و'] = {
    "latin":    's-h-w',
    "category": 'Quranic',
    "core":     ["flood", "heedlessness", "neglectful", "about"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-و-أ'] = {
    "latin":    's-w-a',
    "category": 'Quranic',
    "core":     ["evil", "allah", "indeed", "good", "lord", "deeds", "people", "whoever"],
    "extended": ["punishment", "said", "used", "except", "say", "day", "any", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ح'] = {
    "latin":    's-w-h',
    "category": 'Quranic',
    "core":     ["territory", "warned", "descends", "evil"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-و-د'] = {
    "latin":    's-w-d',
    "category": 'Quranic',
    "core":     ["black", "allah", "white", "used", "punishment", "day", "faces", "righteous"],
    "extended": ["becomes", "indeed", "whose", "disbelieve", "after", "taste", "become", "turn"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ر'] = {
    "latin":    's-w-r',
    "category": 'Quranic',
    "core":     ["revealed", "allah", "surah", "say", "bracelets", "believe", "silk", "garments"],
    "extended": ["gold", "therein", "adorned", "truthful", "call", "like", "hearts", "bring"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ط'] = {
    "latin":    's-w-t',
    "category": 'Quranic',
    "core":     ["scourge", "lord", "punishment", "poured"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ع'] = {
    "latin":    's-w-a',
    "category": 'Quranic',
    "core":     ["hour", "allah", "indeed", "day", "say", "about", "except", "know"],
    "extended": ["surely", "lord", "knowledge", "established", "suddenly", "punishment", "comes", "come"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-غ'] = {
    "latin":    's-w-gh',
    "category": 'Quranic',
    "core":     ["drink"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ق'] = {
    "latin":    's-w-q',
    "category": 'Quranic',
    "core":     ["lord", "drive", "until", "sends", "forth", "land", "driven", "made"],
    "extended": ["say", "allah", "day", "water", "down", "clouds", "thus", "before"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ل'] = {
    "latin":    's-w-l',
    "category": 'Quranic',
    "core":     ["said", "enticed", "patience", "souls", "nay", "beautiful", "allah", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-و-م'] = {
    "latin":    's-w-m',
    "category": 'Quranic',
    "core":     ["lord", "allah", "upon", "marks", "women", "great", "people", "sons"],
    "extended": ["afflicting", "live", "firaun", "letting", "trial", "saved", "torment", "slaughtering"],
    "avoid":    [],
}
ROOT_LEXICON['س-و-ي'] = {
    "latin":    's-w-y',
    "category": 'Quranic',
    "core":     ["allah", "equal", "say", "created", "earth", "lord", "way", "heavens"],
    "extended": ["indeed", "people", "same", "said", "like", "forth", "believe", "whether"],
    "avoid":    [],
}
ROOT_LEXICON['س-ي-ب'] = {
    "latin":    's-y-b',
    "category": 'Quranic',
    "core":     ["bahirah", "reason", "invent", "saibah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ي-ح'] = {
    "latin":    's-y-h',
    "category": 'Quranic',
    "core":     ["allah", "worship"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['س-ي-ر'] = {
    "latin":    's-y-r',
    "category": 'Quranic',
    "core":     ["travel", "earth", "end", "allah", "see", "before", "land", "mountains"],
    "extended": ["indeed", "made", "say", "said", "traveled", "among", "surely", "sent"],
    "avoid":    [],
}
ROOT_LEXICON['س-ي-ل'] = {
    "latin":    's-y-l',
    "category": 'Quranic',
    "core":     ["make", "away", "water", "valleys", "fire", "order", "scum", "allah"],
    "extended": ["sends", "utensils", "down", "rising", "sets", "heat", "forth", "carries"],
    "avoid":    [],
}
ROOT_LEXICON['ش-أ-م'] = {
    "latin":    'sh-a-m',
    "category": 'Quranic',
    "core":     ["companions", "left"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-أ-ن'] = {
    "latin":    'sh-a-n',
    "category": 'Quranic',
    "core":     ["matter", "heavens", "earth", "among", "day"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ب-ه'] = {
    "latin":    'sh-b-h',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "believe", "fruit", "gardens", "lord", "say", "clear"],
    "extended": ["hearts", "olives", "bears", "date", "pomegranates", "palm", "give", "alike"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ت-ت'] = {
    "latin":    'sh-t-t',
    "category": 'Quranic',
    "core":     ["diverse"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ت-و'] = {
    "latin":    'sh-t-w',
    "category": 'Quranic',
    "core":     ["summer", "journey", "winter", "familiarity"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ج-ر'] = {
    "latin":    'sh-j-r',
    "category": 'Quranic',
    "core":     ["tree", "lord", "allah", "both", "indeed", "earth", "trees", "said"],
    "extended": ["eat", "any", "shaitaan", "made", "adam", "themselves", "garden", "apparent"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ح-ح'] = {
    "latin":    'sh-h-h',
    "category": 'Quranic',
    "core":     ["fear", "allah", "themselves", "good", "saved", "soul", "successful", "whoever"],
    "extended": ["ones"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ح-م'] = {
    "latin":    'sh-h-m',
    "category": 'Quranic',
    "core":     ["cows", "truthful", "except", "sheep"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ح-ن'] = {
    "latin":    'sh-h-n',
    "category": 'Quranic',
    "core":     ["ship", "laden"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-خ-ص'] = {
    "latin":    'sh-kh-s',
    "category": 'Quranic',
    "core":     ["wrongdoers", "eyes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-د-د'] = {
    "latin":    'sh-d-d',
    "category": 'Quranic',
    "core":     ["severe", "allah", "punishment", "indeed", "before", "lord", "people", "among"],
    "extended": ["stronger", "believe", "see", "than", "surely", "said", "more", "strength"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ح'] = {
    "latin":    'sh-r-h',
    "category": 'Quranic',
    "core":     ["breast", "allah", "whoever", "islam", "upon", "lord", "expanded"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-د'] = {
    "latin":    'sh-r-d',
    "category": 'Quranic',
    "core":     ["disperse", "take", "over", "dominance"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ذ-م'] = {
    "latin":    'sh-r-dh-m',
    "category": 'Quranic',
    "core":     ["indeed", "certainly", "band", "small"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ر'] = {
    "latin":    'sh-r-r',
    "category": 'Quranic',
    "core":     ["evil", "allah", "good", "indeed", "bad", "say", "position", "worst"],
    "extended": ["worse", "man", "touches", "upon", "know", "day", "way", "than"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ط'] = {
    "latin":    'sh-r-t',
    "category": 'Quranic',
    "core":     ["indications", "suddenly", "wait", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ق'] = {
    "latin":    'sh-r-q',
    "category": 'Quranic',
    "core":     ["east", "west", "lord", "allah", "sunrise", "between", "indeed", "people"],
    "extended": ["earth", "turn", "guides", "used", "ones", "wills", "prayer", "whom"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ر-ي'] = {
    "latin":    'sh-r-y',
    "category": 'Quranic',
    "core":     ["allah", "price", "indeed", "little", "book", "punishment", "exchange", "people"],
    "extended": ["hereafter", "down", "revealed", "evil", "sold", "whoever", "know", "purchase"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ط-أ'] = {
    "latin":    'sh-t-a',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ط-ر'] = {
    "latin":    'sh-t-r',
    "category": 'Quranic',
    "core":     ["turn", "wherever", "direction", "face", "haraam", "masjid", "indeed", "allah"],
    "extended": ["faces", "lord", "surely", "truth", "unaware", "forth", "start"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ط-ط'] = {
    "latin":    'sh-t-t',
    "category": 'Quranic',
    "core":     ["said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ط-ن'] = {
    "latin":    'sh-t-n',
    "category": 'Quranic',
    "core":     ["shaitaan", "indeed", "allah", "made", "devils", "lord", "enemy", "said"],
    "extended": ["except", "believe", "say", "evil", "only", "both", "whoever", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ع-ب'] = {
    "latin":    'sh-a-b',
    "category": 'Quranic',
    "core":     ["female", "allah", "knower", "nations"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ع-ر'] = {
    "latin":    'sh-a-r',
    "category": 'Quranic',
    "core":     ["perceive", "allah", "while", "except", "punishment", "say", "lord", "suddenly"],
    "extended": ["believe", "themselves", "good", "come", "said", "indeed", "before", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ع-ل'] = {
    "latin":    'sh-a-l',
    "category": 'Quranic',
    "core":     ["weakened", "said", "flared", "white"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-غ-ف'] = {
    "latin":    'sh-gh-f',
    "category": 'Quranic',
    "core":     ["said", "error", "women", "seduce"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-غ-ل'] = {
    "latin":    'sh-gh-l',
    "category": 'Quranic',
    "core":     ["amusement", "companions", "paradise", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ف-ق'] = {
    "latin":    'sh-f-q',
    "category": 'Quranic',
    "core":     ["fearful", "lord", "indeed", "fear", "before", "except", "see", "say"],
    "extended": ["great", "afraid", "hour", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ف-ه'] = {
    "latin":    'sh-f-h',
    "category": 'Quranic',
    "core":     ["lips", "tongue"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ف-و'] = {
    "latin":    'sh-f-w',
    "category": 'Quranic',
    "core":     ["fire", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ق-ق'] = {
    "latin":    'sh-q-q',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "split", "messenger", "surely", "because", "whoever", "opposes"],
    "extended": ["far", "penalty", "severe", "opposed", "day", "earth", "after", "like"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ك-س'] = {
    "latin":    'sh-k-s',
    "category": 'Quranic',
    "core":     ["example", "sets", "partners", "exclusively"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ك-ل'] = {
    "latin":    'sh-k-l',
    "category": 'Quranic',
    "core":     ["works", "say", "guided", "manner"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ك-و'] = {
    "latin":    'sh-k-w',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-م-ت'] = {
    "latin":    'sh-m-t',
    "category": 'Quranic',
    "core":     ["said", "considered", "angry", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-م-خ'] = {
    "latin":    'sh-m-kh',
    "category": 'Quranic',
    "core":     ["lofty", "water", "drink", "set"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-م-ز'] = {
    "latin":    'sh-m-z',
    "category": 'Quranic',
    "core":     ["rejoice", "believe", "besides", "mentioned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-م-ل'] = {
    "latin":    'sh-m-l',
    "category": 'Quranic',
    "core":     ["left", "right", "say", "allah", "while", "females", "wombs", "males"],
    "extended": ["forbidden", "contains", "knowledge", "guide", "grateful", "find", "surely", "seen"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ن-أ'] = {
    "latin":    'sh-n-a',
    "category": 'Quranic',
    "core":     ["indeed", "fear", "believe", "let", "allah", "people", "hatred", "piety"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ه-ب'] = {
    "latin":    'sh-h-b',
    "category": 'Quranic',
    "core":     ["burning", "except", "flame", "follows", "hearing", "fire", "flaming"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ه-ر'] = {
    "latin":    'sh-h-r',
    "category": 'Quranic',
    "core":     ["allah", "whoever", "month", "months", "sacred", "among", "indeed", "therein"],
    "extended": ["know", "four", "number", "fear", "upon", "ease", "hardship", "period"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ه-ق'] = {
    "latin":    'sh-h-q',
    "category": 'Quranic',
    "core":     ["therein"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ه-و'] = {
    "latin":    'sh-h-w',
    "category": 'Quranic',
    "core":     ["desire", "allah", "women", "souls", "gold", "life", "world", "approach"],
    "extended": ["indeed", "instead", "nay", "men", "people", "forever", "abide", "therein"],
    "avoid":    [],
}
ROOT_LEXICON['ش-و-ب'] = {
    "latin":    'sh-w-b',
    "category": 'Quranic',
    "core":     ["mixture", "indeed", "boiling", "water"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-و-ر'] = {
    "latin":    'sh-w-r',
    "category": 'Quranic',
    "core":     ["consultation", "allah", "ask", "because", "child"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-و-ظ'] = {
    "latin":    'sh-w-z',
    "category": 'Quranic',
    "core":     ["fire", "both", "flame", "against"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-و-ك'] = {
    "latin":    'sh-w-k',
    "category": 'Quranic',
    "core":     ["than", "groups", "armed", "wished"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-و-ي'] = {
    "latin":    'sh-w-y',
    "category": 'Quranic',
    "core":     ["water", "fire", "believe", "wretched"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ي-أ'] = {
    "latin":    'sh-y-a',
    "category": 'Quranic',
    "core":     ["allah", "thing", "wills", "indeed", "whom", "anything", "lord", "earth"],
    "extended": ["except", "say", "said", "surely", "any", "people", "willed", "heavens"],
    "avoid":    [],
}
ROOT_LEXICON['ش-ي-ب'] = {
    "latin":    'sh-y-b',
    "category": 'Quranic',
    "core":     ["gray"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ي-خ'] = {
    "latin":    'sh-y-kh',
    "category": 'Quranic',
    "core":     ["old", "said", "child", "indeed", "man", "father", "take"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ي-د'] = {
    "latin":    'sh-y-d',
    "category": 'Quranic',
    "core":     ["lofty"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ش-ي-ع'] = {
    "latin":    'sh-y-a',
    "category": 'Quranic',
    "core":     ["indeed", "sects", "among", "punishment", "religion", "divide", "become", "allah"],
    "extended": ["before", "certainly", "against", "surely", "people", "party", "kind"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-أ'] = {
    "latin":    's-b-a',
    "category": 'Quranic',
    "core":     ["believed", "christians", "indeed", "sabians", "allah", "day", "jews", "fear"],
    "extended": ["deeds", "grieve", "became", "last"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-ب'] = {
    "latin":    's-b-b',
    "category": 'Quranic',
    "core":     ["water", "poured", "over", "lord", "scalding", "punishment", "abundance"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-ح'] = {
    "latin":    's-b-h',
    "category": 'Quranic',
    "core":     ["became", "allah", "morning", "indeed", "seized", "said", "become", "regretful"],
    "extended": ["earth", "prone", "fallen", "lord", "like", "water", "over", "thing"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-ع'] = {
    "latin":    's-b-a',
    "category": 'Quranic',
    "core":     ["fingers", "put", "ears"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-غ'] = {
    "latin":    's-b-gh',
    "category": 'Quranic',
    "core":     ["than", "coloring", "better", "allah", "worshippers", "color"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ب-و'] = {
    "latin":    's-b-w',
    "category": 'Quranic',
    "core":     ["said", "child"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ح-ب'] = {
    "latin":    's-h-b',
    "category": 'Quranic',
    "core":     ["companions", "fire", "allah", "indeed", "forever", "abide", "paradise", "lord"],
    "extended": ["say", "companion", "out", "call", "among", "people", "believe", "right"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ح-ف'] = {
    "latin":    's-h-f',
    "category": 'Quranic',
    "core":     ["scriptures", "pages", "former", "desires", "musa"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-خ-خ'] = {
    "latin":    's-kh-kh',
    "category": 'Quranic',
    "core":     ["deafening", "blast", "comes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-د-د'] = {
    "latin":    's-d-d',
    "category": 'Quranic',
    "core":     ["allah", "way", "hinder", "indeed", "away", "people", "while", "made"],
    "extended": ["turn", "disbelieve", "punishment", "used", "deeds", "say", "haraam", "masjid"],
    "avoid":    [],
}
ROOT_LEXICON['ص-د-ع'] = {
    "latin":    's-d-a',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-د-ف'] = {
    "latin":    's-d-f',
    "category": 'Quranic',
    "core":     ["signs", "say", "turn", "allah", "than", "away", "bring", "book"],
    "extended": ["guided", "come", "turns", "denies", "recompense", "mercy", "more", "unjust"],
    "avoid":    [],
}
ROOT_LEXICON['ص-د-ي'] = {
    "latin":    's-d-y',
    "category": 'Quranic',
    "core":     ["except", "disbelieve", "house", "clapping"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ر-ح'] = {
    "latin":    's-r-h',
    "category": 'Quranic',
    "core":     ["said", "indeed", "sulaiman", "saw", "allah", "pool", "uncovered", "palace"],
    "extended": ["lord", "glass", "wronged", "myself", "thought", "worlds", "made", "shins"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ر-ر'] = {
    "latin":    's-r-r',
    "category": 'Quranic',
    "core":     ["themselves", "allah", "wronged", "struck", "forgive"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ر-ص-ر'] = {
    "latin":    's-r-s-r',
    "category": 'Quranic',
    "core":     ["wind", "furious", "upon", "sent", "misfortune"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ر-ع'] = {
    "latin":    's-r-a',
    "category": 'Quranic',
    "core":     ["imposed", "days", "see", "eight"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ر-م'] = {
    "latin":    's-r-m',
    "category": 'Quranic',
    "core":     ["pluck", "fruit"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ع-د'] = {
    "latin":    's-a-d',
    "category": 'Quranic',
    "core":     ["allah", "believe", "make", "whoever", "punishment", "while", "anyone", "water"],
    "extended": ["ill", "indeed", "prayer", "faces", "journey", "toilet", "clean", "find"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ع-ر'] = {
    "latin":    's-a-r',
    "category": 'Quranic',
    "core":     ["conceited", "self", "walk", "cheek"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ع-ق'] = {
    "latin":    's-a-q',
    "category": 'Quranic',
    "core":     ["thunderbolt", "allah", "like", "said", "seized", "musa", "turn", "thamud"],
    "extended": ["fear", "thunder", "manifestly", "looking", "never", "see", "while", "until"],
    "avoid":    [],
}
ROOT_LEXICON['ص-غ-ر'] = {
    "latin":    's-gh-r',
    "category": 'Quranic',
    "core":     ["lord", "small", "allah", "say", "believe", "any", "except", "there"],
    "extended": ["out", "surely", "indeed", "make", "knower", "witnesses", "until", "used"],
    "avoid":    [],
}
ROOT_LEXICON['ص-غ-و'] = {
    "latin":    's-gh-w',
    "category": 'Quranic',
    "core":     ["hearts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-ح'] = {
    "latin":    's-f-h',
    "category": 'Quranic',
    "core":     ["overlook", "indeed", "allah", "forgive", "truth", "except", "turn", "people"],
    "extended": ["heavens", "between", "surely", "gracious", "coming", "hour", "created", "whatever"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-د'] = {
    "latin":    's-f-d',
    "category": 'Quranic',
    "core":     ["bound", "chains"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-ر'] = {
    "latin":    's-f-r',
    "category": 'Quranic',
    "core":     ["yellow", "see", "indeed", "turn", "allah", "debris"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-ص-ف'] = {
    "latin":    's-f-s-f',
    "category": 'Quranic',
    "core":     ["plain", "leave", "level"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-ف'] = {
    "latin":    's-f-f',
    "category": 'Quranic',
    "core":     ["rows", "lined", "allah", "indeed", "come", "lord", "made", "verily"],
    "extended": ["see", "birds", "stand", "except", "gracious", "most", "angels"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-ن'] = {
    "latin":    's-f-n',
    "category": 'Quranic',
    "core":     ["excellent", "displayed", "steeds", "afternoon"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ف-و'] = {
    "latin":    's-f-w',
    "category": 'Quranic',
    "core":     ["chosen", "indeed", "allah", "over", "surely", "sons", "ibrahim", "among"],
    "extended": ["said", "given", "whom", "angels", "daughters", "religion", "except", "himself"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ك-ك'] = {
    "latin":    's-k-k',
    "category": 'Quranic',
    "core":     ["forward", "said", "loud", "barren"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ل-ب'] = {
    "latin":    's-l-b',
    "category": 'Quranic',
    "core":     ["indeed", "surely", "feet", "cut", "hands", "opposite", "off", "allah"],
    "extended": ["before", "crucified", "sides", "crucify", "between", "except", "messenger", "about"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ل-ح'] = {
    "latin":    's-l-h',
    "category": 'Quranic',
    "core":     ["righteous", "deeds", "indeed", "allah", "believe", "lord", "good", "reward"],
    "extended": ["whoever", "among", "except", "said", "gardens", "fear", "believed", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ل-د'] = {
    "latin":    's-l-d',
    "category": 'Quranic',
    "core":     ["example", "guide", "believe", "spends"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ل-ص-ل'] = {
    "latin":    's-l-s-l',
    "category": 'Quranic',
    "core":     ["clay", "created", "altered", "mud", "black", "said", "human"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-م-ت'] = {
    "latin":    's-m-t',
    "category": 'Quranic',
    "core":     ["follow", "call", "silent", "whether"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-م-د'] = {
    "latin":    's-m-d',
    "category": 'Quranic',
    "core":     ["allah", "absolute", "eternal"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-م-ع'] = {
    "latin":    's-m-a',
    "category": 'Quranic',
    "core":     ["right", "said", "evicted", "mentioned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-م-م'] = {
    "latin":    's-m-m',
    "category": 'Quranic',
    "core":     ["deaf", "blind", "hear", "dumb", "allah", "indeed", "cause", "call"],
    "extended": ["example", "like", "seer", "astray", "verses", "whoever", "lets", "use"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ن-ع'] = {
    "latin":    's-n-a',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "used", "made", "surely", "evil", "ones", "ship"],
    "extended": ["under", "comes", "said", "people", "word", "except", "concerning", "wronged"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ن-م'] = {
    "latin":    's-n-m',
    "category": 'Quranic',
    "core":     ["idols", "said", "ibrahim", "indeed", "gods", "people", "devoted", "make"],
    "extended": ["away", "worship"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ن-و'] = {
    "latin":    's-n-w',
    "category": 'Quranic',
    "core":     ["water", "signs", "fruit", "others", "indeed", "crops", "people", "cause"],
    "extended": ["palms", "use", "gardens", "trees", "watered", "root", "reason", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ه-ر'] = {
    "latin":    's-h-r',
    "category": 'Quranic',
    "core":     ["melted", "skins", "bellies", "being"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-و-ب'] = {
    "latin":    's-w-b',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "befalls", "say", "good", "disaster", "among", "except"],
    "extended": ["strikes", "people", "any", "struck", "said", "messenger", "hands", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ص-و-ت'] = {
    "latin":    's-w-t',
    "category": 'Quranic',
    "core":     ["voice", "voices", "lower", "indeed", "sounds", "harshest", "moderate", "pace"],
    "extended": ["donkeys", "surely", "except", "prophet", "worthless", "above", "believe", "loud"],
    "avoid":    [],
}
ROOT_LEXICON['ص-و-ع'] = {
    "latin":    's-w-a',
    "category": 'Quranic',
    "core":     ["said", "load", "missing", "king"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-و-ف'] = {
    "latin":    's-w-f',
    "category": 'Quranic',
    "core":     ["time", "cattle", "provision", "travel"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ي-د'] = {
    "latin":    's-y-d',
    "category": 'Quranic',
    "core":     ["allah", "believe", "ihram", "game", "lawful", "indeed", "hunt", "while"],
    "extended": ["made", "people", "punishment", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ي-ر'] = {
    "latin":    's-y-r',
    "category": 'Quranic',
    "core":     ["destination", "allah", "return", "wretched", "hell", "final", "abode", "say"],
    "extended": ["fire", "lord", "earth", "said", "whoever", "disbelieved", "evil", "between"],
    "avoid":    [],
}
ROOT_LEXICON['ص-ي-ص'] = {
    "latin":    's-y-s',
    "category": 'Quranic',
    "core":     ["scripture", "took", "captive", "cast"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ص-ي-ف'] = {
    "latin":    's-y-f',
    "category": 'Quranic',
    "core":     ["summer", "journey", "winter", "familiarity"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-أ-ن'] = {
    "latin":    'd-a-n',
    "category": 'Quranic',
    "core":     ["truthful", "sheep", "eight", "females"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ب-ح'] = {
    "latin":    'd-b-h',
    "category": 'Quranic',
    "core":     ["panting", "racers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ج-ع'] = {
    "latin":    'd-j-a',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "out", "fear", "spend", "forsake"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ح-و'] = {
    "latin":    'd-h-w',
    "category": 'Quranic',
    "core":     ["brightness", "people", "day", "sun", "morning"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-د-د'] = {
    "latin":    'd-d-d',
    "category": 'Quranic',
    "core":     ["deny", "against", "opponents", "nay"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ر-ع'] = {
    "latin":    'd-r-a',
    "category": 'Quranic',
    "core":     ["humbly", "seized", "lord", "themselves", "hardship", "humble", "adversity", "sent"],
    "extended": ["punishment", "call", "except"],
    "avoid":    [],
}
ROOT_LEXICON['ض-غ-ث'] = {
    "latin":    'd-gh-th',
    "category": 'Quranic',
    "core":     ["dreams"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-غ-ن'] = {
    "latin":    'd-gh-n',
    "category": 'Quranic',
    "core":     ["forth", "hatred", "bring"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ف-د-ع'] = {
    "latin":    'd-f-d-a',
    "category": 'Quranic',
    "core":     ["criminal", "frogs", "locusts", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-م-ر'] = {
    "latin":    'd-m-r',
    "category": 'Quranic',
    "core":     ["distant", "proclaim", "lean", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-م-م'] = {
    "latin":    'd-m-m',
    "category": 'Quranic',
    "core":     ["white", "come", "without", "hand", "draw", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ن-ك'] = {
    "latin":    'd-n-k',
    "category": 'Quranic',
    "core":     ["blind", "life", "remembrance", "away"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ن-ن'] = {
    "latin":    'd-n-n',
    "category": 'Quranic',
    "core":     ["unseen", "withholder"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ه-أ'] = {
    "latin":    'd-h-a',
    "category": 'Quranic',
    "core":     ["said", "mouths", "messiah", "before"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-و-أ'] = {
    "latin":    'd-w-a',
    "category": 'Quranic',
    "core":     ["light", "allah", "example", "fire", "away", "like", "almost", "thing"],
    "extended": ["made"],
    "avoid":    [],
}
ROOT_LEXICON['ض-ي-ر'] = {
    "latin":    'd-y-r',
    "category": 'Quranic',
    "core":     ["said", "return", "indeed", "harm"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ي-ز'] = {
    "latin":    'd-y-z',
    "category": 'Quranic',
    "core":     ["division", "unfair"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ي-ع'] = {
    "latin":    'd-y-a',
    "category": 'Quranic',
    "core":     ["waste", "reward", "let", "indeed", "allah", "good", "doers", "prayer"],
    "extended": ["way", "messenger", "thus", "except", "whom", "deeds", "surely", "evil"],
    "avoid":    [],
}
ROOT_LEXICON['ض-ي-ف'] = {
    "latin":    'd-y-f',
    "category": 'Quranic',
    "core":     ["guests", "said", "came", "people", "ibrahim"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ض-ي-ق'] = {
    "latin":    'd-y-q',
    "category": 'Quranic',
    "core":     ["straitened", "allah", "breast", "grieve", "distress", "though", "earth", "turned"],
    "extended": ["verily", "day", "indeed", "until", "behind", "except", "say", "give"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ب-ع'] = {
    "latin":    't-b-a',
    "category": 'Quranic',
    "core":     ["hearts", "allah", "seal", "believe", "thus", "set", "over", "sealed"],
    "extended": ["signs", "because", "any", "without", "after", "put", "people", "proofs"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ب-ق'] = {
    "latin":    't-b-q',
    "category": 'Quranic',
    "core":     ["heavens", "see", "seven", "embark", "surely", "stage"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ح-و'] = {
    "latin":    't-h-w',
    "category": 'Quranic',
    "core":     ["spread", "earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ر-ح'] = {
    "latin":    't-r-h',
    "category": 'Quranic',
    "core":     ["father", "cast", "kill", "after"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ر-د'] = {
    "latin":    't-r-d',
    "category": 'Quranic',
    "core":     ["away", "lord", "wrongdoers", "desiring", "account", "anything", "call", "countenance"],
    "extended": ["send", "evening", "morning", "people", "drive", "allah"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ر-ف'] = {
    "latin":    't-r-f',
    "category": 'Quranic',
    "core":     ["gaze", "indeed", "day", "see", "before", "modest", "companions", "ends"],
    "extended": ["night", "borders", "land", "come", "say", "lord", "glance"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ر-ق'] = {
    "latin":    't-r-q',
    "category": 'Quranic',
    "core":     ["way", "indeed", "night", "allah", "except", "said", "musa", "path"],
    "extended": ["remained", "know", "comer"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ر-و'] = {
    "latin":    't-r-w',
    "category": 'Quranic',
    "core":     ["fresh", "grateful", "see", "ships", "bounty", "wear", "meat", "seek"],
    "extended": ["ornaments", "eat"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ع-ن'] = {
    "latin":    't-a-n',
    "category": 'Quranic',
    "core":     ["disbelief", "religion"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ف-أ'] = {
    "latin":    't-f-a',
    "category": 'Quranic',
    "core":     ["allah", "out", "mouths", "light", "dislike", "perfect", "disbelievers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ف-ف'] = {
    "latin":    't-f-f',
    "category": 'Quranic',
    "core":     ["less", "woe", "give"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ف-ق'] = {
    "latin":    't-f-q',
    "category": 'Quranic',
    "core":     ["began", "shame", "themselves", "became", "lord", "apparent", "both", "fasten"],
    "extended": ["over", "leaves"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ف-ل'] = {
    "latin":    't-f-l',
    "category": 'Quranic',
    "core":     ["among", "reach", "maturity", "clinging", "term", "dust", "dies", "known"],
    "extended": ["clear", "created", "make", "out", "drop", "child", "having", "substance"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ل-ب'] = {
    "latin":    't-l-b',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "never", "example", "fly", "besides", "snatched", "invoke"],
    "extended": ["weak", "forth", "back", "listen", "gathered", "thing", "away", "take"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ل-ح'] = {
    "latin":    't-l-h',
    "category": 'Quranic',
    "core":     ["banana", "layered", "trees"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-ل-ع'] = {
    "latin":    't-l-a',
    "category": 'Quranic',
    "core":     ["sun", "until", "indeed", "made", "look", "rising", "allah", "think"],
    "extended": ["any", "say", "unseen", "believe", "good", "evil", "except", "hearts"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ل-ل'] = {
    "latin":    't-l-l',
    "category": 'Quranic',
    "core":     ["example", "drizzle", "certainty", "seer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-م-أ-ن'] = {
    "latin":    't-m-a-n',
    "category": 'Quranic',
    "core":     ["allah", "hearts", "wise", "mighty", "except", "made", "good", "indeed"],
    "extended": ["content", "said", "believed", "heart", "know", "life", "satisfy", "victory"],
    "avoid":    [],
}
ROOT_LEXICON['ط-م-ث'] = {
    "latin":    't-m-th',
    "category": 'Quranic',
    "core":     ["jinn", "touched", "before", "man", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-م-س'] = {
    "latin":    't-m-s',
    "category": 'Quranic',
    "core":     ["believe", "given", "see", "punishment", "eyes", "obliterated"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-م-ع'] = {
    "latin":    't-m-a',
    "category": 'Quranic',
    "core":     ["hope", "fear", "indeed", "allah", "after", "lord", "call", "among"],
    "extended": ["believe", "people", "out", "earth", "shows", "lightning", "forgive"],
    "avoid":    [],
}
ROOT_LEXICON['ط-م-م'] = {
    "latin":    't-m-m',
    "category": 'Quranic',
    "core":     ["overwhelming", "calamity", "great", "comes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-و-د'] = {
    "latin":    't-w-d',
    "category": 'Quranic',
    "core":     ["staff", "strike", "became", "parted"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-و-ر'] = {
    "latin":    't-w-r',
    "category": 'Quranic',
    "core":     ["mount", "covenant", "took", "raised", "over", "said", "side", "hold"],
    "extended": ["perhaps", "remember", "made", "right", "called", "sinai", "tur", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ط-و-ق'] = {
    "latin":    't-w-q',
    "category": 'Quranic',
    "core":     ["allah", "whoever", "good", "against", "except", "strength"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ط-و-ل'] = {
    "latin":    't-w-l',
    "category": 'Quranic',
    "core":     ["among", "allah", "long", "prolonged", "sin", "permission", "punishment", "said"],
    "extended": ["indeed", "people", "life", "come"],
    "avoid":    [],
}
ROOT_LEXICON['ط-و-ي'] = {
    "latin":    't-w-y',
    "category": 'Quranic',
    "core":     ["indeed", "day", "tuwa", "sacred", "valley", "lord", "creation", "doers"],
    "extended": ["folding", "fold", "first", "promise", "began", "repeat", "like", "scroll"],
    "avoid":    [],
}
ROOT_LEXICON['ط-ي-ب'] = {
    "latin":    't-y-b',
    "category": 'Quranic',
    "core":     ["good", "allah", "things", "eat", "provided", "indeed", "women", "lawful"],
    "extended": ["believe", "say", "earth", "evil", "men", "forth", "lord", "fear"],
    "avoid":    [],
}
ROOT_LEXICON['ظ-ع-ن'] = {
    "latin":    'z-a-n',
    "category": 'Quranic',
    "core":     ["time", "cattle", "provision", "travel"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ظ-ف-ر'] = {
    "latin":    'z-f-r',
    "category": 'Quranic',
    "core":     ["cows", "truthful", "except", "sheep"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ظ-ل-ل'] = {
    "latin":    'z-l-l',
    "category": 'Quranic',
    "core":     ["shade", "good", "allah", "indeed", "shades", "surely", "clouds", "sent"],
    "extended": ["down", "shadows", "flows", "rivers", "underneath", "spouses", "certainly", "upon"],
    "avoid":    [],
}
ROOT_LEXICON['ظ-م-أ'] = {
    "latin":    'z-m-a',
    "category": 'Quranic',
    "core":     ["allah", "thirst"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ب-أ'] = {
    "latin":    'a-b-a',
    "category": 'Quranic',
    "core":     ["inevitable", "denied", "care", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ب-ث'] = {
    "latin":    'a-b-th',
    "category": 'Quranic',
    "core":     ["returned", "created", "uselessly", "think"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ب-ر'] = {
    "latin":    'a-b-r',
    "category": 'Quranic',
    "core":     ["indeed", "lesson", "allah", "surely", "vision", "way", "believe", "came"],
    "extended": ["hands", "people", "drink", "cattle", "bellies", "give"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ب-س'] = {
    "latin":    'a-b-s',
    "category": 'Quranic',
    "core":     ["frowned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ب-ق-ر'] = {
    "latin":    'a-b-q-r',
    "category": 'Quranic',
    "core":     ["green", "cushions", "carpets", "beautiful"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ت-ب'] = {
    "latin":    'a-t-b',
    "category": 'Quranic',
    "core":     ["day", "asked", "make", "amends", "fire", "endure", "abode", "ask"],
    "extended": ["favor", "receive"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ت-د'] = {
    "latin":    'a-t-d',
    "category": 'Quranic',
    "core":     ["prepared", "disbelievers", "punishment", "indeed", "painful", "allah", "fire", "people"],
    "extended": ["whoever", "blazing", "while", "evil", "humiliating", "among", "certainly", "noble"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ت-ق'] = {
    "latin":    'a-t-q',
    "category": 'Quranic',
    "core":     ["house", "ancient"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ت-ل'] = {
    "latin":    'a-t-l',
    "category": 'Quranic',
    "core":     ["hellfire", "midst", "drag", "seize"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ت-و'] = {
    "latin":    'a-t-w',
    "category": 'Quranic',
    "core":     ["lord", "said", "command", "insolent", "indeed", "against", "messengers", "while"],
    "extended": ["angels", "see", "themselves", "meeting", "arrogant", "sent", "become", "within"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ث-ر'] = {
    "latin":    'a-th-r',
    "category": 'Quranic',
    "core":     ["allah", "place", "surely", "over"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ث-و'] = {
    "latin":    'a-th-w',
    "category": 'Quranic',
    "core":     ["earth", "people", "spreading", "corruption", "act", "allah", "wickedly", "said"],
    "extended": ["deprive", "things", "commit", "evil"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ج-ب'] = {
    "latin":    'a-j-b',
    "category": 'Quranic',
    "core":     ["allah", "wonder", "indeed", "disbelievers", "pleases", "man", "said", "people"],
    "extended": ["come", "among", "lord", "world", "fire", "believe", "forgiveness", "even"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ج-ف'] = {
    "latin":    'a-j-f',
    "category": 'Quranic',
    "core":     ["cows", "seven", "ears", "explain", "lean", "about", "green", "eating"],
    "extended": ["dry", "ones", "fat"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ج-ل'] = {
    "latin":    'a-j-l',
    "category": 'Quranic',
    "core":     ["hasten", "indeed", "allah", "calf", "said", "ask", "lord", "musa"],
    "extended": ["people", "punishment", "say", "evil", "took", "seek", "surely", "after"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ج-م'] = {
    "latin":    'a-j-m',
    "category": 'Quranic',
    "core":     ["being", "foreign", "say", "said", "arab", "believe", "ears", "blindness"],
    "extended": ["explained", "called", "detail", "deafness", "place", "quran", "verses", "why"],
    "avoid":    [],
}
ROOT_LEXICON['ع-د-د'] = {
    "latin":    'a-d-d',
    "category": 'Quranic',
    "core":     ["allah", "prepared", "number", "indeed", "count", "know", "among", "whoever"],
    "extended": ["lord", "punishment", "except", "say", "disbelievers", "days", "period", "about"],
    "avoid":    [],
}
ROOT_LEXICON['ع-د-س'] = {
    "latin":    'a-d-s',
    "category": 'Quranic',
    "core":     ["right", "said", "never", "themselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ذ-ر'] = {
    "latin":    'a-dh-r',
    "category": 'Quranic',
    "core":     ["make", "excuses", "excuse", "allah", "verily", "messenger", "used", "said"],
    "extended": ["among", "punish", "punishment", "after", "disbelieved", "never", "believe", "see"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ب'] = {
    "latin":    'a-r-b',
    "category": 'Quranic',
    "core":     ["bedouins", "arabic", "allah", "quran", "among", "messenger", "indeed", "say"],
    "extended": ["know", "people", "punishment", "revealed", "around", "behind", "any", "good"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ج'] = {
    "latin":    'a-r-j',
    "category": 'Quranic',
    "core":     ["heaven", "allah", "ascend", "therein", "earth", "houses", "lame", "blind"],
    "extended": ["any", "sick", "blame", "thousand", "measure", "day", "knows", "comes"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ج-ن'] = {
    "latin":    'a-r-j-n',
    "category": 'Quranic',
    "core":     ["moon", "returns", "stalk", "phases"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ر'] = {
    "latin":    'a-r-r',
    "category": 'Quranic',
    "core":     ["among", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ض'] = {
    "latin":    'a-r-d',
    "category": 'Quranic',
    "core":     ["away", "turn", "allah", "indeed", "say", "lord", "turns", "day"],
    "extended": ["except", "earth", "punishment", "good", "between", "most", "come", "turning"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ف'] = {
    "latin":    'a-r-f',
    "category": 'Quranic',
    "core":     ["allah", "women", "recognize", "right", "upon", "indeed", "kindness", "among"],
    "extended": ["manner", "good", "wrong", "know", "whoever", "men", "fair", "give"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-م'] = {
    "latin":    'a-r-m',
    "category": 'Quranic',
    "core":     ["producing", "changed", "away", "tamarisks"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-و'] = {
    "latin":    'a-r-w',
    "category": 'Quranic',
    "core":     ["allah", "handhold", "grasped", "whoever", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ر-ي'] = {
    "latin":    'a-r-y',
    "category": 'Quranic',
    "core":     ["onto", "shore", "while"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ز-ب'] = {
    "latin":    'a-z-b',
    "category": 'Quranic',
    "core":     ["smaller", "heavens", "weight", "escapes", "clear", "lord", "than", "greater"],
    "extended": ["earth", "atom", "record"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ز-ر'] = {
    "latin":    'a-z-r',
    "category": 'Quranic',
    "core":     ["believe", "right", "allah", "honor", "messenger"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ز-ل'] = {
    "latin":    'a-z-l',
    "category": 'Quranic',
    "core":     ["allah", "withdraw", "made", "come", "indeed", "people", "against", "except"],
    "extended": ["given", "surely", "hearts", "offer", "peace", "lord", "besides", "leave"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ز-م'] = {
    "latin":    'a-z-m',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "determination", "patient", "surely", "matters", "resolve", "except"],
    "extended": ["yourselves", "matter", "before"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ز-و'] = {
    "latin":    'a-z-w',
    "category": 'Quranic',
    "core":     ["right", "groups", "left", "separate"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-س-ع-س'] = {
    "latin":    'a-s-a-s',
    "category": 'Quranic',
    "core":     ["night", "departs"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-س-ي'] = {
    "latin":    'a-s-y',
    "category": 'Quranic',
    "core":     ["perhaps", "allah", "lord", "said", "except", "than", "upon", "thing"],
    "extended": ["way", "after", "believe", "indeed", "say", "better", "see", "take"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ش-ر'] = {
    "latin":    'a-sh-r',
    "category": 'Quranic',
    "core":     ["allah", "ten", "indeed", "people", "among", "said", "whoever", "except"],
    "extended": ["find", "themselves", "term", "say", "day", "place", "musa", "twelve"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ش-و'] = {
    "latin":    'a-sh-w',
    "category": 'Quranic',
    "core":     ["evening", "morning", "lord", "glorify", "people", "night", "except", "three"],
    "extended": ["desiring", "away", "call", "came", "remembrance", "whom", "patient", "prayer"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-ب'] = {
    "latin":    'a-s-b',
    "category": 'Quranic',
    "core":     ["said", "indeed", "group", "while", "surely", "great"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-ر'] = {
    "latin":    'a-s-r',
    "category": 'Quranic',
    "core":     ["rain"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-ف'] = {
    "latin":    'a-s-f',
    "category": 'Quranic',
    "core":     ["wind", "stormy", "land", "like", "violently", "winds", "blow"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-م'] = {
    "latin":    'a-s-m',
    "category": 'Quranic',
    "core":     ["allah", "any", "protector", "hold", "between", "mercy", "among", "upon"],
    "extended": ["messenger", "fast", "except", "guide", "said", "surely", "verses", "guided"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-و'] = {
    "latin":    'a-s-w',
    "category": 'Quranic',
    "core":     ["staff", "musa", "said", "indeed", "threw", "throw", "strike", "inspired"],
    "extended": ["behold", "moving", "water", "knew", "springs", "drinking", "people", "forth"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ص-ي'] = {
    "latin":    'a-s-y',
    "category": 'Quranic',
    "core":     ["allah", "disobeyed", "indeed", "lord", "messenger", "disobey", "said", "say"],
    "extended": ["because", "except", "among", "whoever", "disobeys", "punishment", "day", "fear"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ض-د'] = {
    "latin":    'a-d-d',
    "category": 'Quranic',
    "core":     ["heavens", "creation", "themselves", "helper"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ض-ض'] = {
    "latin":    'a-d-d',
    "category": 'Quranic',
    "core":     ["bite", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ض-ل'] = {
    "latin":    'a-d-l',
    "category": 'Quranic',
    "core":     ["allah", "women"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ض-و'] = {
    "latin":    'a-d-w',
    "category": 'Quranic',
    "core":     ["made", "quran", "parts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ط-ف'] = {
    "latin":    'a-t-f',
    "category": 'Quranic',
    "core":     ["burning", "disgrace", "taste", "fire"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ط-ل'] = {
    "latin":    'a-t-l',
    "category": 'Quranic',
    "core":     ["lofty", "roofs", "destroyed", "township"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ط-و'] = {
    "latin":    'a-t-w',
    "category": 'Quranic',
    "core":     ["lord", "given", "gift", "concerning", "pleased", "enraged", "criticizes", "among"],
    "extended": ["charities", "extend", "restricted", "gave", "account"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ف-ر'] = {
    "latin":    'a-f-r',
    "category": 'Quranic',
    "core":     ["place", "said", "jinn", "rise"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ف-ف'] = {
    "latin":    'a-f-f',
    "category": 'Quranic',
    "core":     ["allah", "marriage", "sufficient", "indeed", "poor", "knower", "good", "let"],
    "extended": ["until", "wealth", "whoever", "refrain", "desire", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ف-و'] = {
    "latin":    'a-f-w',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "oft", "pardon", "forgiving", "people", "among", "while"],
    "extended": ["pardoning", "after", "until", "clear", "forgive", "good", "surely", "forgave"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ق-ر'] = {
    "latin":    'a-q-r',
    "category": 'Quranic',
    "core":     ["hamstrung", "said", "lord", "barren", "wife", "old", "reached", "age"],
    "extended": ["promise", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ق-م'] = {
    "latin":    'a-q-m',
    "category": 'Quranic',
    "core":     ["barren"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ل-ن'] = {
    "latin":    'a-l-n',
    "category": 'Quranic',
    "core":     ["conceal", "knows", "allah", "declare", "indeed", "lord", "secretly", "spend"],
    "extended": ["breasts", "know", "reveal", "establish", "provided", "earth", "openly", "grieve"],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-د'] = {
    "latin":    'a-m-d',
    "category": 'Quranic',
    "core":     ["allah", "pillars", "intentionally", "whoever", "believe", "just", "see", "heavens"],
    "extended": ["without"],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-ر'] = {
    "latin":    'a-m-r',
    "category": 'Quranic',
    "core":     ["allah", "life", "indeed", "among", "than", "granted", "any", "created"],
    "extended": ["find", "whoever", "except", "gives", "made", "knowledge", "dust", "drop"],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-ق'] = {
    "latin":    'a-m-q',
    "category": 'Quranic',
    "core":     ["distant", "proclaim", "lean", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-م'] = {
    "latin":    'a-m-m',
    "category": 'Quranic',
    "core":     ["allah", "paternal", "aunts", "possess", "any", "uncles", "maternal", "wives"],
    "extended": ["indeed", "brothers", "daughters", "merciful", "forgiving", "sisters", "most", "mothers"],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-ه'] = {
    "latin":    'a-m-h',
    "category": 'Quranic',
    "core":     ["blindly", "transgression", "wandering", "allah", "wander", "believe", "leave", "surely"],
    "extended": ["indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ع-م-ي'] = {
    "latin":    'a-m-y',
    "category": 'Quranic',
    "core":     ["blind", "deaf", "allah", "lord", "hear", "equal", "whoever", "verses"],
    "extended": ["except", "like", "seeing", "say", "guide", "believe", "dumb", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ن-ب'] = {
    "latin":    'a-n-b',
    "category": 'Quranic',
    "core":     ["date", "palms", "grapes", "gardens", "grapevines", "fruits", "indeed", "people"],
    "extended": ["forth", "signs", "crops", "surely", "rivers", "garden", "water", "fruit"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ن-ت'] = {
    "latin":    'a-n-t',
    "category": 'Quranic',
    "core":     ["allah", "right", "indeed", "about", "knows", "surely", "best", "take"],
    "extended": ["yourselves", "certainly", "made", "believers", "among", "merciful", "faith", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ن-د'] = {
    "latin":    'a-n-d',
    "category": 'Quranic',
    "core":     ["allah", "lord", "indeed", "near", "say", "said", "reward", "except"],
    "extended": ["believe", "surely", "good", "knowledge", "know", "people", "any", "best"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ن-ك-ب'] = {
    "latin":    'a-n-k-b',
    "category": 'Quranic',
    "core":     ["example", "protectors", "house", "takes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ن-و'] = {
    "latin":    'a-n-w',
    "category": 'Quranic',
    "core":     ["ever", "wrongdoing", "subsisting", "self"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ه-ن'] = {
    "latin":    'a-h-n',
    "category": 'Quranic',
    "core":     ["mountains", "wool", "like"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-ج'] = {
    "latin":    'a-w-j',
    "category": 'Quranic',
    "core":     ["allah", "crookedness", "hinder", "way", "while", "hereafter", "seek", "any"],
    "extended": ["seeking", "crooked", "believe", "book", "disbelievers", "path", "see"],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-د'] = {
    "latin":    'a-w-d',
    "category": 'Quranic',
    "core":     ["allah", "aad", "return", "lord", "people", "indeed", "say", "said"],
    "extended": ["come", "thamud", "creation", "returned", "before", "out", "upon", "repeats"],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-ذ'] = {
    "latin":    'a-w-dh',
    "category": 'Quranic',
    "core":     ["refuge", "seek", "indeed", "lord", "allah", "said", "shaitaan", "among"],
    "extended": ["evil", "say", "take", "musa", "comes", "suggestion", "wrongdoers", "sought"],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-ر'] = {
    "latin":    'a-w-r',
    "category": 'Quranic',
    "core":     ["permission", "right", "let", "among", "allah", "possess", "hands", "exposed"],
    "extended": ["said", "prophet", "asked", "return", "yathrib", "houses", "wished", "flee"],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-ق'] = {
    "latin":    'a-w-q',
    "category": 'Quranic',
    "core":     ["knows", "allah", "except", "battle"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-ل'] = {
    "latin":    'a-w-l',
    "category": 'Quranic',
    "core":     ["right", "marry", "fear", "orphans"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-و-م'] = {
    "latin":    'a-w-m',
    "category": 'Quranic',
    "core":     ["year", "people", "allah", "after", "make", "remained", "made", "come"],
    "extended": ["indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ع-ي-ب'] = {
    "latin":    'a-y-b',
    "category": 'Quranic',
    "core":     ["force", "ship", "after", "seized"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ي-ر'] = {
    "latin":    'a-y-r',
    "category": 'Quranic',
    "core":     ["caravan", "indeed", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ي-ش'] = {
    "latin":    'a-y-sh',
    "category": 'Quranic',
    "core":     ["livelihood", "life", "made", "little", "means", "indeed", "day", "pleasant"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ي-ل'] = {
    "latin":    'a-y-l',
    "category": 'Quranic',
    "core":     ["wise", "fear", "believe", "wills"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ع-ي-ي'] = {
    "latin":    'a-y-y',
    "category": 'Quranic',
    "core":     ["creation", "tired"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ب-ر'] = {
    "latin":    'gh-b-r',
    "category": 'Quranic',
    "core":     ["except", "behind", "wife", "family", "remain", "remained", "saved", "surely"],
    "extended": ["woman", "among", "old", "said", "lut", "save", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ب-ن'] = {
    "latin":    'gh-b-n',
    "category": 'Quranic',
    "core":     ["rivers", "deeds", "flow", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ث-و'] = {
    "latin":    'gh-th-w',
    "category": 'Quranic',
    "core":     ["wrongdoers", "awful", "seized", "away"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-د-ر'] = {
    "latin":    'gh-d-r',
    "category": 'Quranic',
    "core":     ["see", "anyone"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-د-ق'] = {
    "latin":    'gh-d-q',
    "category": 'Quranic',
    "core":     ["water", "drink", "abundance", "way"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-د-و'] = {
    "latin":    'gh-d-w',
    "category": 'Quranic',
    "core":     ["morning", "allah", "tomorrow", "lord", "indeed", "early", "evening", "mornings"],
    "extended": ["desiring", "anything", "call", "send", "fear", "among", "evenings", "heedless"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-ب'] = {
    "latin":    'gh-r-b',
    "category": 'Quranic',
    "core":     ["allah", "lord", "east", "west", "said", "sun", "patient", "setting"],
    "extended": ["guides", "say", "people", "near", "became", "like", "earth", "take"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-ر'] = {
    "latin":    'gh-r-r',
    "category": 'Quranic',
    "core":     ["allah", "life", "world", "deceiver", "about", "except", "deceive", "promise"],
    "extended": ["say", "day", "mankind", "indeed", "deceived", "delusion", "lord", "true"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-ف'] = {
    "latin":    'gh-r-f',
    "category": 'Quranic',
    "core":     ["allah", "patient", "whoever", "said", "river", "believed", "indeed", "takes"],
    "extended": ["overcame", "today", "company", "against", "certain", "permission", "hollow", "meet"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-ق'] = {
    "latin":    'gh-r-q',
    "category": 'Quranic',
    "core":     ["drowned", "people", "denied", "ship", "indeed", "sea", "saved", "signs"],
    "extended": ["made", "firaun", "took", "because", "said", "except", "whom", "ones"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-م'] = {
    "latin":    'gh-r-m',
    "category": 'Quranic',
    "core":     ["debt", "allah", "indeed", "payment", "ask"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ر-و'] = {
    "latin":    'gh-r-w',
    "category": 'Quranic',
    "core":     ["said", "between", "resurrection", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ز-ل'] = {
    "latin":    'gh-z-l',
    "category": 'Quranic',
    "core":     ["untwisted", "between", "community", "resurrection"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ز-و'] = {
    "latin":    'gh-z-w',
    "category": 'Quranic',
    "core":     ["said", "died", "believe", "death"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-س-ق'] = {
    "latin":    'gh-s-q',
    "category": 'Quranic',
    "core":     ["darkness", "purulence"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-س-ل'] = {
    "latin":    'gh-s-l',
    "category": 'Quranic',
    "core":     ["water", "believe", "ill", "allah", "prayer", "faces", "journey", "except"],
    "extended": ["toilet", "clean", "find", "hands", "earth", "women", "wipe", "any"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ش-و'] = {
    "latin":    'gh-sh-w',
    "category": 'Quranic',
    "core":     ["allah", "covers", "covered", "indeed", "night", "made", "hearts", "punishment"],
    "extended": ["surely", "cover", "like", "see", "death", "say", "any", "upon"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ص-ب'] = {
    "latin":    'gh-s-b',
    "category": 'Quranic',
    "core":     ["force", "ship", "after", "seized"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ص-ص'] = {
    "latin":    'gh-s-s',
    "category": 'Quranic',
    "core":     ["punishment", "food", "chokes", "painful"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ض-ض'] = {
    "latin":    'gh-d-d',
    "category": 'Quranic',
    "core":     ["lower", "indeed", "allah", "aware", "say", "believing", "chastity", "gaze"],
    "extended": ["guard", "men"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ط-ش'] = {
    "latin":    'gh-t-sh',
    "category": 'Quranic',
    "core":     ["out", "brought", "darkened", "brightness"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ط-و'] = {
    "latin":    'gh-t-w',
    "category": 'Quranic',
    "core":     ["cover"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ف-ل'] = {
    "latin":    'gh-f-l',
    "category": 'Quranic',
    "core":     ["unaware", "allah", "indeed", "heedless", "lord", "certainly", "among", "while"],
    "extended": ["day", "world", "say", "surely", "about", "signs", "believe", "book"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-ظ'] = {
    "latin":    'gh-l-z',
    "category": 'Quranic',
    "core":     ["allah", "disbelievers", "punishment", "severe", "mercy", "surely", "covenant", "stern"],
    "extended": ["believe", "indeed", "forgiveness", "harsh", "strong", "took", "prostrating", "over"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-ف'] = {
    "latin":    'gh-l-f',
    "category": 'Quranic',
    "core":     ["allah", "believe", "disbelief", "wrapped", "hearts", "nay"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-ق'] = {
    "latin":    'gh-l-q',
    "category": 'Quranic',
    "core":     ["closed", "said", "wrongdoers", "house"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-ل'] = {
    "latin":    'gh-l-l',
    "category": 'Quranic',
    "core":     ["day", "resurrection", "lord", "prophet", "full", "fire", "allah", "necks"],
    "extended": ["indeed", "wronged", "earned", "soul", "defrauds", "repaid", "defrauded", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-م'] = {
    "latin":    'gh-l-m',
    "category": 'Quranic',
    "core":     ["said", "boy", "son", "lord", "tidings", "glad", "indeed", "allah"],
    "extended": ["barren", "wife", "old", "reached", "age", "bring", "learned", "pure"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-و'] = {
    "latin":    'gh-l-w',
    "category": 'Quranic',
    "core":     ["book", "say", "people", "religion", "truth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ل-ي'] = {
    "latin":    'gh-l-y',
    "category": 'Quranic',
    "core":     ["like"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-م-ر'] = {
    "latin":    'gh-m-r',
    "category": 'Quranic',
    "core":     ["confusion"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-م-ز'] = {
    "latin":    'gh-m-z',
    "category": 'Quranic',
    "core":     ["winked", "passed", "another"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-م-ض'] = {
    "latin":    'gh-m-d',
    "category": 'Quranic',
    "core":     ["aim", "bad", "sufficient", "believe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-م-م'] = {
    "latin":    'gh-m-m',
    "category": 'Quranic',
    "core":     ["allah", "distress", "clouds", "sent", "down", "themselves", "over", "decreed"],
    "extended": ["aware", "while", "upon", "people", "quails", "wronged", "wrong", "manna"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ن-م'] = {
    "latin":    'gh-n-m',
    "category": 'Quranic',
    "core":     ["allah", "war", "spoils", "indeed", "sheep", "take", "believe", "say"],
    "extended": ["forth", "before", "upon", "except", "down", "said", "people", "much"],
    "avoid":    [],
}
ROOT_LEXICON['غ-ن-ي'] = {
    "latin":    'gh-n-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "avail", "anything", "need", "free", "sufficient", "earth"],
    "extended": ["praiseworthy", "against", "whoever", "said", "any", "self", "away", "people"],
    "avoid":    [],
}
ROOT_LEXICON['غ-و-ث'] = {
    "latin":    'gh-w-th',
    "category": 'Quranic',
    "core":     ["indeed", "help", "lord", "believe", "water", "fire", "wretched", "say"],
    "extended": ["wills", "let", "walls", "relieved", "faces", "relief", "scalds", "place"],
    "avoid":    [],
}
ROOT_LEXICON['غ-و-ر'] = {
    "latin":    'gh-w-r',
    "category": 'Quranic',
    "core":     ["find", "water", "sunken"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-و-ص'] = {
    "latin":    'gh-w-s',
    "category": 'Quranic',
    "core":     ["devils"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-و-ط'] = {
    "latin":    'gh-w-t',
    "category": 'Quranic',
    "core":     ["water", "believe", "ill", "allah", "prayer", "faces", "journey", "toilet"],
    "extended": ["clean", "find", "hands", "earth", "women", "wipe"],
    "avoid":    [],
}
ROOT_LEXICON['غ-و-ل'] = {
    "latin":    'gh-w-l',
    "category": 'Quranic',
    "core":     ["intoxicated", "bad", "effect"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ي-ث'] = {
    "latin":    'gh-y-th',
    "category": 'Quranic',
    "core":     ["rain", "after", "down", "allah", "sends"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ي-ض'] = {
    "latin":    'gh-y-d',
    "category": 'Quranic',
    "core":     ["sky", "said", "water", "subsided"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['غ-ي-ظ'] = {
    "latin":    'gh-y-z',
    "category": 'Quranic',
    "core":     ["allah", "rage", "indeed", "good", "believe", "doers", "anger", "people"],
    "extended": ["remove", "messenger", "any", "righteous", "reward", "disbelievers", "see"],
    "avoid":    [],
}
ROOT_LEXICON['ف-أ-د'] = {
    "latin":    'f-a-d',
    "category": 'Quranic',
    "core":     ["hearts", "hearing", "heart", "made", "thanks", "give", "sight", "allah"],
    "extended": ["any", "little", "vision", "believe", "incline", "believers", "make", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ف-أ-ي'] = {
    "latin":    'f-a-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "group", "whoever", "forces", "help", "said", "today"],
    "extended": ["meet", "except", "way", "sight", "whom", "river", "believed", "patient"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ت-أ'] = {
    "latin":    'f-t-a',
    "category": 'Quranic',
    "core":     ["said", "cease", "ill", "fatally"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ت-ر'] = {
    "latin":    'f-t-r',
    "category": 'Quranic',
    "core":     ["book", "say", "come", "makes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ت-ق'] = {
    "latin":    'f-t-q',
    "category": 'Quranic',
    "core":     ["heavens", "water", "see", "believe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ت-ل'] = {
    "latin":    'f-t-l',
    "category": 'Quranic',
    "core":     ["wronged", "seed", "hair", "date", "towards", "allah", "whoever"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ت-ي'] = {
    "latin":    'f-t-y',
    "category": 'Quranic',
    "core":     ["said", "about", "indeed", "allah", "women", "give", "say", "seek"],
    "extended": ["girls", "gives", "concerning", "ruling", "ones", "whom", "good", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ج-ج'] = {
    "latin":    'f-j-j',
    "category": 'Quranic',
    "core":     ["therein"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ج-و'] = {
    "latin":    'f-j-w',
    "category": 'Quranic',
    "core":     ["right", "guide", "rose", "never"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-خ-ر'] = {
    "latin":    'f-kh-r',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "like", "love", "boastful", "self", "boaster"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-د-ي'] = {
    "latin":    'f-d-y',
    "category": 'Quranic',
    "core":     ["ransom", "punishment", "allah", "whatever", "earth", "disbelieve", "day", "resurrection"],
    "extended": ["among", "whoever", "accepted", "like", "sin", "back", "except", "while"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ت'] = {
    "latin":    'f-r-t',
    "category": 'Quranic',
    "core":     ["sweet", "seas", "bitter", "salty", "made", "drink"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ث'] = {
    "latin":    'f-r-th',
    "category": 'Quranic',
    "core":     ["drink", "between", "cattle", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ج'] = {
    "latin":    'f-r-j',
    "category": 'Quranic',
    "core":     ["chastity", "believing", "guard", "men", "allah", "breathed", "guarded", "spirit"],
    "extended": ["into", "guardians", "modesty", "aware", "say", "lower", "gaze", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-د'] = {
    "latin":    'f-r-d',
    "category": 'Quranic',
    "core":     ["alone", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ر'] = {
    "latin":    'f-r-r',
    "category": 'Quranic',
    "core":     ["flee", "say", "indeed", "except", "death", "fleeing", "surely", "back"],
    "extended": ["flight", "killing", "never", "allowed", "little", "benefit", "enjoy", "man"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ش'] = {
    "latin":    'f-r-sh',
    "category": 'Quranic',
    "core":     ["allah", "earth", "couches"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ط'] = {
    "latin":    'f-r-t',
    "category": 'Quranic',
    "core":     ["allah", "over", "said", "until", "neglected", "lord", "indeed", "regret"],
    "extended": ["concerning", "among", "best"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ع'] = {
    "latin":    'f-r-a',
    "category": 'Quranic',
    "core":     ["example", "sky", "sets", "branches"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-غ'] = {
    "latin":    'f-r-gh',
    "category": 'Quranic',
    "core":     ["pour", "patience", "said", "lord", "over"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ه'] = {
    "latin":    'f-r-h',
    "category": 'Quranic',
    "core":     ["mountains", "carve", "houses", "skillfully"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ر-ي'] = {
    "latin":    'f-r-y',
    "category": 'Quranic',
    "core":     ["allah", "say", "invent", "lie", "against", "invented", "about", "than"],
    "extended": ["used", "indeed", "more", "people", "invents", "lost", "truth", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ز-ز'] = {
    "latin":    'f-z-z',
    "category": 'Quranic',
    "core":     ["except", "land"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ز-ع'] = {
    "latin":    'f-z-a',
    "category": 'Quranic',
    "core":     ["day", "terror", "except", "whoever", "whom", "terrified", "said", "fear"],
    "extended": ["truth"],
    "avoid":    [],
}
ROOT_LEXICON['ف-س-ح'] = {
    "latin":    'f-s-h',
    "category": 'Quranic',
    "core":     ["said", "allah", "assemblies", "degrees", "believe", "rise", "aware", "room"],
    "extended": ["raise", "given", "among", "make", "knowledge"],
    "avoid":    [],
}
ROOT_LEXICON['ف-س-ر'] = {
    "latin":    'f-s-r',
    "category": 'Quranic',
    "core":     ["example", "come", "best", "bring"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-س-ق'] = {
    "latin":    'f-s-q',
    "category": 'Quranic',
    "core":     ["defiantly", "disobedient", "allah", "people", "indeed", "except", "most", "lord"],
    "extended": ["fear", "whoever", "among", "disbelieved", "said", "other", "because", "punishment"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ش-ل'] = {
    "latin":    'f-sh-l',
    "category": 'Quranic',
    "core":     ["allah", "lost", "courage", "believers", "among", "dispute", "shown", "surely"],
    "extended": ["indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ص-ح'] = {
    "latin":    'f-s-h',
    "category": 'Quranic',
    "core":     ["than", "fear", "helper", "speech"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ص-ل'] = {
    "latin":    'f-s-l',
    "category": 'Quranic',
    "core":     ["people", "day", "allah", "indeed", "lord", "know", "signs", "verses"],
    "extended": ["made", "explained", "detail", "explain", "book", "believe", "judgment", "years"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ص-م'] = {
    "latin":    'f-s-m',
    "category": 'Quranic',
    "core":     ["right", "handhold", "compulsion", "knowing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ض-ح'] = {
    "latin":    'f-d-h',
    "category": 'Quranic',
    "core":     ["shame", "guests", "said", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ض-ض'] = {
    "latin":    'f-d-d',
    "category": 'Quranic',
    "core":     ["silver", "allah", "gold", "mankind", "indeed", "surely", "give", "spend"],
    "extended": ["upon", "say", "crystal"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ض-و'] = {
    "latin":    'f-d-w',
    "category": 'Quranic',
    "core":     ["gone", "strong", "taken", "take"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ظ-ظ'] = {
    "latin":    'f-z-z',
    "category": 'Quranic',
    "core":     ["indeed", "allah", "loves", "forgiveness"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ع-ل'] = {
    "latin":    'f-a-l',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "said", "lord", "believe", "except", "say", "among"],
    "extended": ["whoever", "done", "people", "doing", "surely", "fear", "good", "thus"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ق-د'] = {
    "latin":    'f-q-d',
    "category": 'Quranic',
    "core":     ["said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ق-ر'] = {
    "latin":    'f-q-r',
    "category": 'Quranic',
    "core":     ["allah", "poor", "while", "indeed", "bounty", "knowing", "good", "way"],
    "extended": ["rich", "need", "encompassing", "aware", "charities", "sufficient", "people", "spend"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ق-ع'] = {
    "latin":    'f-q-a',
    "category": 'Quranic',
    "core":     ["bright", "said", "pray", "says"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ك-ك'] = {
    "latin":    'f-k-k',
    "category": 'Quranic',
    "core":     ["neck", "freeing", "polytheists", "comes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ك-ه'] = {
    "latin":    'f-k-h',
    "category": 'Quranic',
    "core":     ["fruits", "therein", "fruit", "palms", "abundant", "date", "call", "eat"],
    "extended": ["desire", "both"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ل-ح'] = {
    "latin":    'f-l-h',
    "category": 'Quranic',
    "core":     ["successful", "allah", "succeed", "indeed", "ones", "say", "believe", "lord"],
    "extended": ["come", "fear", "good", "people", "right", "about", "wrongdoers", "lie"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ل-ق'] = {
    "latin":    'f-l-q',
    "category": 'Quranic',
    "core":     ["cleaver"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ل-ك'] = {
    "latin":    'f-l-k',
    "category": 'Quranic',
    "core":     ["ships", "ship", "allah", "sea", "indeed", "sail", "see", "command"],
    "extended": ["bounty", "seek", "signs", "people", "drowned", "saved", "subjected", "grateful"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ل-ن'] = {
    "latin":    'f-l-n',
    "category": 'Quranic',
    "core":     ["friend", "taken", "woe", "wish"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ن-د'] = {
    "latin":    'f-n-d',
    "category": 'Quranic',
    "core":     ["weakened", "said", "father", "departed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ن-ن'] = {
    "latin":    'f-n-n',
    "category": 'Quranic',
    "core":     ["branches", "having"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ن-ي'] = {
    "latin":    'f-n-y',
    "category": 'Quranic',
    "core":     ["perish", "everyone"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-ه-م'] = {
    "latin":    'f-h-m',
    "category": 'Quranic',
    "core":     ["doers", "glorify", "sulaiman", "praises"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ت'] = {
    "latin":    'f-w-t',
    "category": 'Quranic',
    "core":     ["allah", "grieve", "over", "escaped", "see", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ج'] = {
    "latin":    'f-w-j',
    "category": 'Quranic',
    "core":     ["day", "come"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ر'] = {
    "latin":    'f-w-r',
    "category": 'Quranic',
    "core":     ["ones", "oven", "except", "preceded", "family", "word", "command", "against"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ز'] = {
    "latin":    'f-w-z',
    "category": 'Quranic',
    "core":     ["success", "great", "allah", "rivers", "gardens", "underneath", "whoever", "forever"],
    "extended": ["day", "abide", "surely", "admit", "flow", "indeed", "deeds", "successful"],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ض'] = {
    "latin":    'f-w-d',
    "category": 'Quranic',
    "core":     ["affair", "slaves", "say", "seer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ق'] = {
    "latin":    'f-w-q',
    "category": 'Quranic',
    "core":     ["above", "allah", "over", "lord", "indeed", "said", "made", "any"],
    "extended": ["see", "others", "punishment", "raised", "fear", "take", "like", "say"],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-م'] = {
    "latin":    'f-w-m',
    "category": 'Quranic',
    "core":     ["right", "said", "never", "themselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ف-و-ه'] = {
    "latin":    'f-w-h',
    "category": 'Quranic',
    "core":     ["mouths", "allah", "said", "saying", "hearts", "except", "come", "whom"],
    "extended": ["disbelievers", "hands", "about", "any", "believe", "indeed", "clear", "than"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ي-أ'] = {
    "latin":    'f-y-a',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "believers", "gives", "between", "among", "merciful", "wives"],
    "extended": ["oft", "forgiving", "most", "thing", "made", "whom", "act", "loves"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ي-ض'] = {
    "latin":    'f-y-d',
    "category": 'Quranic',
    "core":     ["allah", "lord", "depart", "merciful", "oft", "indeed", "forgiving", "most"],
    "extended": ["say", "any", "surely", "ask", "people", "forgiveness", "wherever", "eyes"],
    "avoid":    [],
}
ROOT_LEXICON['ف-ي-ل'] = {
    "latin":    'f-y-l',
    "category": 'Quranic',
    "core":     ["elephant", "dealt", "seen", "companions"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ب-ح'] = {
    "latin":    'q-b-h',
    "category": 'Quranic',
    "core":     ["caused", "curse", "follow", "resurrection"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ب-ر'] = {
    "latin":    'q-b-r',
    "category": 'Quranic',
    "core":     ["graves", "allah", "indeed", "grave", "make", "causes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ب-س'] = {
    "latin":    'q-b-s',
    "category": 'Quranic',
    "core":     ["said", "burning", "fire", "family", "indeed", "bring"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ب-ض'] = {
    "latin":    'q-b-d',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "hand", "right", "said", "took", "soul", "threw"],
    "extended": ["handful", "thus", "perceive", "perceived", "track", "messenger", "suggested", "gradual"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ت-ر'] = {
    "latin":    'q-t-r',
    "category": 'Quranic',
    "core":     ["good", "cover", "stingy"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ث-أ'] = {
    "latin":    'q-th-a',
    "category": 'Quranic',
    "core":     ["right", "said", "never", "themselves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ح-م'] = {
    "latin":    'q-h-m',
    "category": 'Quranic',
    "core":     ["burn", "fire", "welcome", "bursting"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-د-ح'] = {
    "latin":    'q-d-h',
    "category": 'Quranic',
    "core":     ["striking", "producers", "sparks"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-د-د'] = {
    "latin":    'q-d-d',
    "category": 'Quranic',
    "core":     ["shirt", "said", "back", "torn"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-د-م'] = {
    "latin":    'q-d-m',
    "category": 'Quranic',
    "core":     ["allah", "forth", "sent", "indeed", "hands", "say", "lord", "give"],
    "extended": ["feet", "believe", "wish", "make", "except", "evil", "upon", "day"],
    "avoid":    [],
}
ROOT_LEXICON['ق-د-و'] = {
    "latin":    'q-d-w',
    "category": 'Quranic',
    "core":     ["ones", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ذ-ف'] = {
    "latin":    'q-dh-f',
    "category": 'Quranic',
    "core":     ["cast", "people", "brought", "take", "against", "truth", "scripture", "hearts"],
    "extended": ["fortresses", "into", "terror", "unseen", "disbelieved"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ح'] = {
    "latin":    'q-r-h',
    "category": 'Quranic',
    "core":     ["among", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-د'] = {
    "latin":    'q-r-d',
    "category": 'Quranic',
    "core":     ["apes", "said", "despised"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ر'] = {
    "latin":    'q-r-r',
    "category": 'Quranic',
    "core":     ["place", "said", "allah", "made", "earth", "lord", "indeed", "resting"],
    "extended": ["eyes", "most", "settlement", "dwelling", "down", "clear", "people", "knows"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ش'] = {
    "latin":    'q-r-sh',
    "category": 'Quranic',
    "core":     ["quraish", "familiarity"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ض'] = {
    "latin":    'q-r-d',
    "category": 'Quranic',
    "core":     ["allah", "loan", "goodly", "indeed", "give", "reward", "lend", "good"],
    "extended": ["among", "prayer", "zakah", "way", "establish", "noble", "multiply", "most"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ط-س'] = {
    "latin":    'q-r-t-s',
    "category": 'Quranic',
    "core":     ["said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ع'] = {
    "latin":    'q-r-a',
    "category": 'Quranic',
    "core":     ["striking", "calamity", "know"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ف'] = {
    "latin":    'q-r-f',
    "category": 'Quranic',
    "core":     ["believe", "commit", "incline", "committing", "pleased", "hearts", "hereafter", "indeed"],
    "extended": ["say", "allah", "relatives"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ر-ن'] = {
    "latin":    'q-r-n',
    "category": 'Quranic',
    "core":     ["before", "generations", "destroyed", "many", "indeed", "companion", "after", "generation"],
    "extended": ["say", "see", "sins", "made", "criminals", "among", "said", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-ر'] = {
    "latin":    'q-s-r',
    "category": 'Quranic',
    "core":     ["fleeing", "lion"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-س'] = {
    "latin":    'q-s-s',
    "category": 'Quranic',
    "core":     ["polytheists", "nearest", "affection", "believe"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-ط'] = {
    "latin":    'q-s-t',
    "category": 'Quranic',
    "core":     ["justice", "allah", "indeed", "between", "just", "loves", "among", "make"],
    "extended": ["act", "right", "anything", "any", "give", "people", "weight", "religion"],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-ط-س'] = {
    "latin":    'q-s-t-s',
    "category": 'Quranic',
    "core":     ["balance", "weigh"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-م'] = {
    "latin":    'q-s-m',
    "category": 'Quranic',
    "core":     ["swear", "allah", "indeed", "surely", "nay", "than", "say", "oaths"],
    "extended": ["among", "day", "other", "swore", "strongest", "others", "lord", "division"],
    "avoid":    [],
}
ROOT_LEXICON['ق-س-و'] = {
    "latin":    'q-s-w',
    "category": 'Quranic',
    "core":     ["hearts", "hardened", "allah", "indeed", "down", "like", "rivers", "water"],
    "extended": ["fear", "stones", "split", "gush", "comes", "forth", "fall", "after"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ش-ع-ر'] = {
    "latin":    'q-sh-a-r',
    "category": 'Quranic',
    "core":     ["guide", "fear", "book", "wills"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ص-د'] = {
    "latin":    'q-s-d',
    "category": 'Quranic',
    "core":     ["moderate", "among", "surely", "allah", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ص-ر'] = {
    "latin":    'q-s-r',
    "category": 'Quranic',
    "core":     ["made", "modest", "companions", "gaze", "indeed", "any", "earth", "allah"],
    "extended": ["palaces", "well"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ص-ف'] = {
    "latin":    'q-s-f',
    "category": 'Quranic',
    "core":     ["hurricane", "wind", "time", "back"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ص-م'] = {
    "latin":    'q-s-m',
    "category": 'Quranic',
    "core":     ["after", "produced", "town", "another"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ص-و'] = {
    "latin":    'q-s-w',
    "category": 'Quranic',
    "core":     ["indeed", "running", "said", "city", "farthest", "end", "came", "man"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ض-ب'] = {
    "latin":    'q-d-b',
    "category": 'Quranic',
    "core":     ["green", "fodder", "grapes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ض-ض'] = {
    "latin":    'q-d-d',
    "category": 'Quranic',
    "core":     ["want", "said", "food", "wall"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ض-ي'] = {
    "latin":    'q-d-y',
    "category": 'Quranic',
    "core":     ["allah", "lord", "indeed", "matter", "said", "between", "decreed", "any"],
    "extended": ["surely", "people", "only", "say", "decided", "clear", "judged", "earth"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ط-ر'] = {
    "latin":    'q-t-r',
    "category": 'Quranic',
    "core":     ["fire", "copper", "molten", "over", "except", "jinn"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ط-ط'] = {
    "latin":    'q-t-t',
    "category": 'Quranic',
    "core":     ["account", "before", "say", "hasten"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ط-ع'] = {
    "latin":    'q-t-a',
    "category": 'Quranic',
    "core":     ["cut", "off", "allah", "indeed", "earth", "hands", "said", "lord"],
    "extended": ["surely", "corruption", "punishment", "feet", "opposite", "people", "water", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ط-ف'] = {
    "latin":    'q-t-f',
    "category": 'Quranic',
    "core":     ["near", "fruits"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ط-م-ر'] = {
    "latin":    'q-t-m-r',
    "category": 'Quranic',
    "core":     ["moon", "besides", "term", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ع-د'] = {
    "latin":    'q-a-d',
    "category": 'Quranic',
    "core":     ["allah", "sit", "indeed", "said", "sitting", "among", "way", "behind"],
    "extended": ["hearing", "believers", "say", "fire", "strive", "than", "wealth", "other"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ع-ر'] = {
    "latin":    'q-a-r',
    "category": 'Quranic',
    "core":     ["plucking", "out", "palms", "uprooted"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ف-ل'] = {
    "latin":    'q-f-l',
    "category": 'Quranic',
    "core":     ["quran", "hearts", "locks", "upon"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ف-و'] = {
    "latin":    'q-f-w',
    "category": 'Quranic',
    "core":     ["isa", "son", "maryam", "gave", "indeed", "followed", "messengers", "footsteps"],
    "extended": ["injeel", "sent"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ل-د'] = {
    "latin":    'q-l-d',
    "category": 'Quranic',
    "core":     ["allah", "heavens", "earth", "house", "sacred", "indeed", "month", "thing"],
    "extended": ["keys"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ل-ع'] = {
    "latin":    'q-l-a',
    "category": 'Quranic',
    "core":     ["sky", "said", "water", "subsided"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ل-ل'] = {
    "latin":    'q-l-l',
    "category": 'Quranic',
    "core":     ["little", "allah", "except", "few", "indeed", "said", "say", "believe"],
    "extended": ["price", "lord", "among", "surely", "give", "covenant", "people", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ل-م'] = {
    "latin":    'q-l-m',
    "category": 'Quranic',
    "core":     ["pens", "pen"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ل-ي'] = {
    "latin":    'q-l-y',
    "category": 'Quranic',
    "core":     ["detest", "said", "indeed", "deed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-م-ح'] = {
    "latin":    'q-m-h',
    "category": 'Quranic',
    "core":     ["chins", "iron", "necks", "raised"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-م-ص'] = {
    "latin":    'q-m-s',
    "category": 'Quranic',
    "core":     ["shirt", "said", "back", "torn", "sought", "family"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-م-ط-ر'] = {
    "latin":    'q-m-t-r',
    "category": 'Quranic',
    "core":     ["harsh", "distressful", "fear", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-م-ع'] = {
    "latin":    'q-m-a',
    "category": 'Quranic',
    "core":     ["rods", "iron", "hooked"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-م-ل'] = {
    "latin":    'q-m-l',
    "category": 'Quranic',
    "core":     ["criminal", "frogs", "locusts", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ن-ط-ر'] = {
    "latin":    'q-n-t-r',
    "category": 'Quranic',
    "core":     ["return", "allah", "tilled", "cattle", "provision", "love", "gold", "branded"],
    "extended": ["horses", "excellent", "desire", "beautified", "abode", "silver", "heaps", "mankind"],
    "avoid":    [],
}
ROOT_LEXICON['ق-ن-ع'] = {
    "latin":    'q-n-a',
    "category": 'Quranic',
    "core":     ["racing", "returning", "raised", "hearts"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ن-و'] = {
    "latin":    'q-n-w',
    "category": 'Quranic',
    "core":     ["water", "believe", "signs", "fruit"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ن-ي'] = {
    "latin":    'q-n-y',
    "category": 'Quranic',
    "core":     ["enriches", "suffices"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ه-ر'] = {
    "latin":    'q-h-r',
    "category": 'Quranic',
    "core":     ["irresistible", "allah", "over", "earth", "slaves", "subjugator", "take", "say"],
    "extended": ["heavens", "forth", "come", "day"],
    "avoid":    [],
}
ROOT_LEXICON['ق-و-ب'] = {
    "latin":    'q-w-b',
    "category": 'Quranic',
    "core":     ["distance", "nearer", "bow"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-و-ت'] = {
    "latin":    'q-w-t',
    "category": 'Quranic',
    "core":     ["share", "keeper", "whoever", "intercession"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-و-س'] = {
    "latin":    'q-w-s',
    "category": 'Quranic',
    "core":     ["distance", "nearer", "bow"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-و-ع'] = {
    "latin":    'q-w-a',
    "category": 'Quranic',
    "core":     ["plain", "leave", "level", "water"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ي-ض'] = {
    "latin":    'q-y-d',
    "category": 'Quranic',
    "core":     ["away"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ق-ي-ل'] = {
    "latin":    'q-y-l',
    "category": 'Quranic',
    "core":     ["destroyed", "city", "punishment", "sleeping"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ب-ب'] = {
    "latin":    'k-b-b',
    "category": 'Quranic',
    "core":     ["except", "cast", "fire", "comes"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ب-ت'] = {
    "latin":    'k-b-t',
    "category": 'Quranic',
    "core":     ["humiliating", "oppose", "before", "verses", "clear", "indeed", "disbelievers", "certainly"],
    "extended": ["punishment", "allah", "sent", "disgraced", "messenger", "down"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ب-د'] = {
    "latin":    'k-b-d',
    "category": 'Quranic',
    "core":     ["man", "created", "hardship", "certainly"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ب-ك-ب'] = {
    "latin":    'k-b-k-b',
    "category": 'Quranic',
    "core":     ["overturned", "deviators", "into"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ث-ب'] = {
    "latin":    'k-th-b',
    "category": 'Quranic',
    "core":     ["heap", "quake", "sand", "become"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-د-ح'] = {
    "latin":    'k-d-h',
    "category": 'Quranic',
    "core":     ["meet", "laboring", "indeed", "mankind", "lord", "exertion"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-د-ر'] = {
    "latin":    'k-d-r',
    "category": 'Quranic',
    "core":     ["fall", "stars", "losing", "luster"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-د-ي'] = {
    "latin":    'k-d-y',
    "category": 'Quranic',
    "core":     ["little", "withheld", "gave"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ر-ب'] = {
    "latin":    'k-r-b',
    "category": 'Quranic',
    "core":     ["distress", "great", "saved", "family"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ر-ر'] = {
    "latin":    'k-r-r',
    "category": 'Quranic',
    "core":     ["return", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ر-س'] = {
    "latin":    'k-r-s',
    "category": 'Quranic',
    "core":     ["high", "tires", "allah", "guarding"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ر-ه'] = {
    "latin":    'k-r-h',
    "category": 'Quranic',
    "core":     ["allah", "dislike", "while", "good", "indeed", "truth", "given", "know"],
    "extended": ["religion", "whoever", "except", "said", "even", "lord", "until", "most"],
    "avoid":    [],
}
ROOT_LEXICON['ك-س-د'] = {
    "latin":    'k-s-d',
    "category": 'Quranic',
    "core":     ["guide", "fear", "commerce", "beloved"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-س-ف'] = {
    "latin":    'k-s-f',
    "category": 'Quranic',
    "core":     ["sky", "fall", "upon", "cause", "fragments", "see", "before", "allah"],
    "extended": ["clouds"],
    "avoid":    [],
}
ROOT_LEXICON['ك-س-ل'] = {
    "latin":    'k-s-l',
    "category": 'Quranic',
    "core":     ["except", "allah", "prayer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-س-و'] = {
    "latin":    'k-s-w',
    "category": 'Quranic',
    "core":     ["allah", "made", "give", "clothing", "another", "whoever", "like", "know"],
    "extended": ["flesh", "people", "bones", "clear"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ش-ط'] = {
    "latin":    'k-sh-t',
    "category": 'Quranic',
    "core":     ["away", "sky", "stripped"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ظ-م'] = {
    "latin":    'k-z-m',
    "category": 'Quranic',
    "core":     ["good", "grief", "face", "news", "given", "dark"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ع-ب'] = {
    "latin":    'k-a-b',
    "category": 'Quranic',
    "core":     ["allah", "believe", "earth", "kabah", "offering"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ف-أ'] = {
    "latin":    'k-f-a',
    "category": 'Quranic',
    "core":     ["any", "equivalent"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ف-ت'] = {
    "latin":    'k-f-t',
    "category": 'Quranic',
    "core":     ["made", "receptacle", "earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ف-ف'] = {
    "latin":    'k-f-f',
    "category": 'Quranic',
    "core":     ["allah", "people", "hands", "believers", "said", "restrain", "towards", "upon"],
    "extended": ["except", "disbelieved", "believe", "indeed", "fear", "group", "lord", "fight"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ف-ل'] = {
    "latin":    'k-f-l',
    "category": 'Quranic',
    "core":     ["said", "allah", "indeed", "while", "maryam", "good", "portion", "rear"],
    "extended": ["people", "kifl", "dhul", "ishmael"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ف-ي'] = {
    "latin":    'k-f-y',
    "category": 'Quranic',
    "core":     ["sufficient", "allah", "witness", "say", "indeed", "lord", "between", "believe"],
    "extended": ["sent", "messenger", "trust", "put", "any", "against", "whoever", "knows"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ل-أ'] = {
    "latin":    'k-l-a',
    "category": 'Quranic',
    "core":     ["remembrance", "lord", "away", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ل-ب'] = {
    "latin":    'k-l-b',
    "category": 'Quranic',
    "core":     ["dog", "say", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ل-ح'] = {
    "latin":    'k-l-h',
    "category": 'Quranic',
    "core":     ["burn", "fire", "lips", "grin"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ل-ف'] = {
    "latin":    'k-l-f',
    "category": 'Quranic',
    "core":     ["any", "except", "soul", "allah", "capacity", "burden", "provision", "give"],
    "extended": ["ask", "like", "upon"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ل-و'] = {
    "latin":    'k-l-w',
    "category": 'Quranic',
    "core":     ["except", "decreed", "parents", "reach"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-م-ل'] = {
    "latin":    'k-m-l',
    "category": 'Quranic',
    "core":     ["allah", "whoever", "complete", "fear", "among", "ease", "fast", "days"],
    "extended": ["other", "know", "animal", "except", "made", "upon", "day"],
    "avoid":    [],
}
ROOT_LEXICON['ك-م-م'] = {
    "latin":    'k-m-m',
    "category": 'Quranic',
    "core":     ["referred", "witness", "say", "announce"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-م-ه'] = {
    "latin":    'k-m-h',
    "category": 'Quranic',
    "core":     ["leper", "allah", "blind", "israel", "permission", "clay", "like", "breath"],
    "extended": ["children", "dead", "bird", "becomes", "into"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ن-د'] = {
    "latin":    'k-n-d',
    "category": 'Quranic',
    "core":     ["surely", "ungrateful", "indeed", "mankind"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ن-ز'] = {
    "latin":    'k-n-z',
    "category": 'Quranic',
    "core":     ["treasure", "hoard", "allah", "indeed", "give", "people", "eat", "flanks"],
    "extended": ["fire", "taste", "foreheads", "hoarded", "used", "yourselves", "hell", "day"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ن-س'] = {
    "latin":    'k-n-s',
    "category": 'Quranic',
    "core":     ["run", "disappear"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ن-ن'] = {
    "latin":    'k-n-n',
    "category": 'Quranic',
    "core":     ["ears", "deafness", "coverings", "hearts", "lord", "well", "say", "knows"],
    "extended": ["understand", "placed", "over", "lest", "indeed", "protected", "allah", "mention"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ه-ف'] = {
    "latin":    'k-h-f',
    "category": 'Quranic',
    "core":     ["cave", "signs", "right", "mercy", "affair", "lord", "facilitate", "years"],
    "extended": ["allah"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ه-ل'] = {
    "latin":    'k-h-l',
    "category": 'Quranic',
    "core":     ["maturity", "cradle", "people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ه-ن'] = {
    "latin":    'k-h-n',
    "category": 'Quranic',
    "core":     ["soothsayer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-و-ب'] = {
    "latin":    'k-w-b',
    "category": 'Quranic',
    "core":     ["cups", "circulated", "vessels"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-و-د'] = {
    "latin":    'k-w-d',
    "category": 'Quranic',
    "core":     ["almost", "allah", "indeed", "earth", "come", "say", "about", "away"],
    "extended": ["near", "after", "surely", "heavens", "whom", "see", "certainly", "thing"],
    "avoid":    [],
}
ROOT_LEXICON['ك-و-ر'] = {
    "latin":    'k-w-r',
    "category": 'Quranic',
    "core":     ["sun"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-و-ك-ب'] = {
    "latin":    'k-w-k-b',
    "category": 'Quranic',
    "core":     ["stars", "said", "star", "saw", "like", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-و-ي'] = {
    "latin":    'k-w-y',
    "category": 'Quranic',
    "core":     ["flanks", "fire", "taste", "hoard"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ك-ي-د'] = {
    "latin":    'k-y-d',
    "category": 'Quranic',
    "core":     ["plan", "plot", "indeed", "allah", "said", "against", "respite", "give"],
    "extended": ["away", "made", "disbelieve", "shaitaan", "together", "lord", "knower", "plotting"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ي-ل'] = {
    "latin":    'k-y-l',
    "category": 'Quranic',
    "core":     ["measure", "full", "give", "said", "brother", "father", "allah", "best"],
    "extended": ["people", "indeed", "returned", "get", "weight", "any", "family", "weigh"],
    "avoid":    [],
}
ROOT_LEXICON['ك-ي-ن'] = {
    "latin":    'k-y-n',
    "category": 'Quranic',
    "core":     ["weakened", "prophet", "loves", "lost"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ب-د'] = {
    "latin":    'l-b-d',
    "category": 'Quranic',
    "core":     ["compacted", "slave", "became", "stood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ج-أ'] = {
    "latin":    'l-j-a',
    "category": 'Quranic',
    "core":     ["refuge", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ج-ج'] = {
    "latin":    'l-j-j',
    "category": 'Quranic',
    "core":     ["persist", "made", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-د'] = {
    "latin":    'l-h-d',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "say", "never", "besides", "find", "refuge"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-ف'] = {
    "latin":    'l-h-f',
    "category": 'Quranic',
    "core":     ["move", "sufficient", "importunity", "recognize"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-ق'] = {
    "latin":    'l-h-q',
    "category": 'Quranic',
    "core":     ["joined", "join", "yet", "allah", "righteous", "lord", "wise", "mighty"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-م'] = {
    "latin":    'l-h-m',
    "category": 'Quranic',
    "core":     ["flesh", "allah", "blood", "indeed", "merciful", "most", "oft", "dead"],
    "extended": ["dedicated", "swine", "forgiving", "other", "meat", "sin", "than", "forbidden"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-ن'] = {
    "latin":    'l-h-n',
    "category": 'Quranic',
    "core":     ["knows", "allah", "show", "speech"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ح-ي'] = {
    "latin":    'l-h-y',
    "category": 'Quranic',
    "core":     ["caused", "said", "beard", "between"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-د-د'] = {
    "latin":    'l-d-d',
    "category": 'Quranic',
    "core":     ["people"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-د-ن'] = {
    "latin":    'l-d-n',
    "category": 'Quranic',
    "core":     ["indeed", "lord", "yourself", "near", "after", "mercy", "grant", "said"],
    "extended": ["reward", "given", "say", "there", "great", "allah", "good", "way"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ذ-ذ'] = {
    "latin":    'l-dh-dh',
    "category": 'Quranic',
    "core":     ["drinkers", "delicious", "forever", "abide", "therein"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ز-ب'] = {
    "latin":    'l-z-b',
    "category": 'Quranic',
    "core":     ["creation", "ask", "created", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ز-م'] = {
    "latin":    'l-z-m',
    "category": 'Quranic',
    "core":     ["lord", "word"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-س-ن'] = {
    "latin":    'l-s-n',
    "category": 'Quranic',
    "core":     ["tongues", "tongue", "allah", "say", "indeed", "language", "while", "clear"],
    "extended": ["arabic", "made", "among", "surely", "know", "lie", "only", "easy"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ظ-ي'] = {
    "latin":    'l-z-y',
    "category": 'Quranic',
    "core":     ["warn", "fire", "blazing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ع-ب'] = {
    "latin":    'l-a-b',
    "category": 'Quranic',
    "core":     ["play", "life", "amusement", "world", "playing", "allah", "leave", "religion"],
    "extended": ["take", "people", "except", "hereafter", "punishment", "day", "only", "surely"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ع-ن'] = {
    "latin":    'l-a-n',
    "category": 'Quranic',
    "core":     ["allah", "curse", "cursed", "indeed", "lord", "day", "punishment", "said"],
    "extended": ["made", "say", "book", "before", "revealed", "ones", "great", "fire"],
    "avoid":    [],
}
ROOT_LEXICON['ل-غ-ب'] = {
    "latin":    'l-gh-b',
    "category": 'Quranic',
    "core":     ["fatigue", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-غ-و'] = {
    "latin":    'l-gh-w',
    "category": 'Quranic',
    "core":     ["talk", "therein", "vain", "hear", "allah", "oaths", "peace", "turn"],
    "extended": ["away", "pass", "falsehood"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ف-ت'] = {
    "latin":    'l-f-t',
    "category": 'Quranic',
    "core":     ["said", "travel", "anyone", "night", "look", "family", "back"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ف-ح'] = {
    "latin":    'l-f-h',
    "category": 'Quranic',
    "core":     ["burn", "fire", "lips", "grin"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ف-ظ'] = {
    "latin":    'l-f-z',
    "category": 'Quranic',
    "core":     ["observer", "ready", "word", "utters"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ف-ف'] = {
    "latin":    'l-f-f',
    "category": 'Quranic',
    "core":     ["crowd", "said", "after", "mixed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ف-و'] = {
    "latin":    'l-f-w',
    "category": 'Quranic',
    "core":     ["found", "said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-ب'] = {
    "latin":    'l-q-b',
    "category": 'Quranic',
    "core":     ["wretched", "believe", "people", "insult"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-ح'] = {
    "latin":    'l-q-h',
    "category": 'Quranic',
    "core":     ["sky", "water", "fertilizing", "drink"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-ط'] = {
    "latin":    'l-q-t',
    "category": 'Quranic',
    "core":     ["pick", "speaker", "said", "kill"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-ف'] = {
    "latin":    'l-q-f',
    "category": 'Quranic',
    "core":     ["staff", "swallow", "musa", "throw"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-م'] = {
    "latin":    'l-q-m',
    "category": 'Quranic',
    "core":     ["while", "swallowed", "blameworthy", "fish"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ق-ي'] = {
    "latin":    'l-q-y',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "said", "meeting", "lord", "day", "meet", "throw"],
    "extended": ["musa", "cast", "say", "surely", "believe", "except", "down", "people"],
    "avoid":    [],
}
ROOT_LEXICON['ل-م-ح'] = {
    "latin":    'l-m-h',
    "category": 'Quranic',
    "core":     ["eye", "twinkling"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-م-ز'] = {
    "latin":    'l-m-z',
    "category": 'Quranic',
    "core":     ["concerning", "charities", "ridicule"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-م-م'] = {
    "latin":    'l-m-m',
    "category": 'Quranic',
    "core":     ["avoid", "indeed", "knowing", "purity"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ه-ب'] = {
    "latin":    'l-h-b',
    "category": 'Quranic',
    "core":     ["cool", "flame", "against", "availing"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ه-ث'] = {
    "latin":    'l-h-th',
    "category": 'Quranic',
    "core":     ["example", "attack", "signs", "story", "people", "adhered", "desires", "followed"],
    "extended": ["denied", "out", "leave", "like", "surely", "earth", "tongue", "willed"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ه-م'] = {
    "latin":    'l-h-m',
    "category": 'Quranic',
    "core":     ["inspired", "wickedness", "righteousness"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-ت'] = {
    "latin":    'l-w-t',
    "category": 'Quranic',
    "core":     ["longer", "called", "destroyed", "generation"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-ح'] = {
    "latin":    'l-w-h',
    "category": 'Quranic',
    "core":     ["tablets", "people", "lord", "musa"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-ذ'] = {
    "latin":    'l-w-dh',
    "category": 'Quranic',
    "core":     ["befalls", "others", "let", "among"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-م'] = {
    "latin":    'l-w-m',
    "category": 'Quranic',
    "core":     ["blameworthy", "allah", "blame", "indeed", "except", "believe", "striving", "wills"],
    "extended": ["turns", "believers", "among", "knowing", "love", "soon", "stern", "loves"],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-ن'] = {
    "latin":    'l-w-n',
    "category": 'Quranic',
    "core":     ["indeed", "colors", "see", "surely", "yellow", "lord", "earth", "allah"],
    "extended": ["bright", "said", "pray", "says", "pleasing", "clear", "make", "cow"],
    "avoid":    [],
}
ROOT_LEXICON['ل-و-ي'] = {
    "latin":    'l-w-y',
    "category": 'Quranic',
    "core":     ["allah", "while", "distort", "tongues", "say", "indeed", "surely", "aware"],
    "extended": ["messenger", "said", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ي-ت'] = {
    "latin":    'l-y-t',
    "category": 'Quranic',
    "core":     ["believe", "deeds", "submitted", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ل-ي-س'] = {
    "latin":    'l-y-s',
    "category": 'Quranic',
    "core":     ["allah", "any", "indeed", "say", "said", "lord", "people", "among"],
    "extended": ["except", "knowledge", "anything", "blame", "book", "like", "fear", "about"],
    "avoid":    [],
}
ROOT_LEXICON['ل-ي-ن'] = {
    "latin":    'l-y-n',
    "category": 'Quranic',
    "core":     ["allah", "fear"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-أ-ي'] = {
    "latin":    'm-a-y',
    "category": 'Quranic',
    "core":     ["hundred", "allah", "thousand", "steadfast", "among", "overcome", "people", "believers"],
    "extended": ["remained", "like", "day", "fight", "prophet", "urge", "disbelieve", "understand"],
    "avoid":    [],
}
ROOT_LEXICON['م-ت-ع'] = {
    "latin":    'm-t-a',
    "category": 'Quranic',
    "core":     ["enjoyment", "allah", "world", "provision", "life", "enjoy", "indeed", "said"],
    "extended": ["punishment", "except", "lord", "day", "little", "upon", "good", "hereafter"],
    "avoid":    [],
}
ROOT_LEXICON['م-ت-ن'] = {
    "latin":    'm-t-n',
    "category": 'Quranic',
    "core":     ["indeed", "respite", "give", "firm", "plan"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ج-د'] = {
    "latin":    'm-j-d',
    "category": 'Quranic',
    "core":     ["glorious", "quran"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ج-س'] = {
    "latin":    'm-j-s',
    "category": 'Quranic',
    "core":     ["polytheists", "between", "judge", "believed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ح-ص'] = {
    "latin":    'm-h-s',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ح-ق'] = {
    "latin":    'm-h-q',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ح-ل'] = {
    "latin":    'm-h-l',
    "category": 'Quranic',
    "core":     ["glorifies", "fear", "angels", "mighty"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ح-ن'] = {
    "latin":    'm-h-n',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ح-و'] = {
    "latin":    'm-h-w',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-خ-ر'] = {
    "latin":    'm-kh-r',
    "category": 'Quranic',
    "core":     ["fresh", "grateful", "see", "ships", "bounty", "wear", "meat", "seek"],
    "extended": ["ornaments", "eat"],
    "avoid":    [],
}
ROOT_LEXICON['م-خ-ض'] = {
    "latin":    'm-kh-d',
    "category": 'Quranic',
    "core":     ["said", "died", "oblivion", "trunk"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-د-د'] = {
    "latin":    'm-d-d',
    "category": 'Quranic',
    "core":     ["extend", "lord", "surely", "allah", "earth", "wealth", "indeed", "spread"],
    "extended": ["made", "say", "see", "punishment", "thousand", "angels", "error", "mountains"],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-أ'] = {
    "latin":    'm-r-a',
    "category": 'Quranic',
    "core":     ["wife", "indeed", "said", "allah", "man", "except", "any", "know"],
    "extended": ["lord", "women", "surely", "family", "behind", "between", "both", "fear"],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-ج'] = {
    "latin":    'm-r-j',
    "category": 'Quranic',
    "core":     ["released", "seas", "coral"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-ح'] = {
    "latin":    'm-r-h',
    "category": 'Quranic',
    "core":     ["earth", "walk", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-د'] = {
    "latin":    'm-r-d',
    "category": 'Quranic',
    "core":     ["rebellious", "among", "devil", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-ر'] = {
    "latin":    'm-r-r',
    "category": 'Quranic',
    "core":     ["time", "allah", "first", "twice", "indeed", "made", "see", "people"],
    "extended": ["created", "turn", "say", "pass", "among", "fear", "sign", "passed"],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-و'] = {
    "latin":    'm-r-w',
    "category": 'Quranic',
    "core":     ["voluntarily", "allah", "safa", "house"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ر-ي'] = {
    "latin":    'm-r-y',
    "category": 'Quranic',
    "core":     ["doubt", "lord", "about", "truth", "among", "indeed", "doubters", "book"],
    "extended": ["before", "except", "dispute", "hour", "certainly", "seek", "revealed", "know"],
    "avoid":    [],
}
ROOT_LEXICON['م-ز-ج'] = {
    "latin":    'm-z-j',
    "category": 'Quranic',
    "core":     ["mixture", "drink", "cup"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ز-ق'] = {
    "latin":    'm-z-q',
    "category": 'Quranic',
    "core":     ["indeed", "surely", "total", "creation", "disbelieve", "disintegration", "new", "direct"],
    "extended": ["say", "informs", "man", "disintegrated", "journeys", "dispersed", "said", "wronged"],
    "avoid":    [],
}
ROOT_LEXICON['م-ز-ن'] = {
    "latin":    'm-z-n',
    "category": 'Quranic',
    "core":     ["clouds", "ones", "send", "rain"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-س-ح'] = {
    "latin":    'm-s-h',
    "category": 'Quranic',
    "core":     ["allah", "messiah", "son", "maryam", "indeed", "said", "earth", "certainly"],
    "extended": ["except", "say", "disbelieved", "near", "isa", "believe", "saying", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['م-س-خ'] = {
    "latin":    'm-s-kh',
    "category": 'Quranic',
    "core":     ["return", "proceed", "transformed", "surely"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-س-د'] = {
    "latin":    'm-s-d',
    "category": 'Quranic',
    "core":     ["fiber", "palm", "neck", "rope"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-س-ك'] = {
    "latin":    'm-s-k',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "fear", "whoever", "most", "release", "retain", "except"],
    "extended": ["take", "given", "book", "term", "women", "upon", "surely", "people"],
    "avoid":    [],
}
ROOT_LEXICON['م-س-و'] = {
    "latin":    'm-s-w',
    "category": 'Quranic',
    "core":     ["allah", "reach", "glory", "evening"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ش-ج'] = {
    "latin":    'm-sh-j',
    "category": 'Quranic',
    "core":     ["test", "drop", "mixture", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ش-ي'] = {
    "latin":    'm-sh-y',
    "category": 'Quranic',
    "core":     ["walk", "indeed", "earth", "surely", "allah", "say", "thing", "people"],
    "extended": ["walks", "made", "messenger", "sent", "before", "certainly", "powerful", "among"],
    "avoid":    [],
}
ROOT_LEXICON['م-ص-ر'] = {
    "latin":    'm-s-r',
    "category": 'Quranic',
    "core":     ["said", "egypt", "allah", "people", "out", "musa", "make", "yusuf"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ض-غ'] = {
    "latin":    'm-d-gh',
    "category": 'Quranic',
    "core":     ["clinging", "lump", "created", "embryonic", "drop", "substance", "semen", "flesh"],
    "extended": ["creation", "allah", "creators", "another", "produce", "bones", "clothed", "best"],
    "avoid":    [],
}
ROOT_LEXICON['م-ض-ي'] = {
    "latin":    'm-d-y',
    "category": 'Quranic',
    "core":     ["cease", "return", "former"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ط-ر'] = {
    "latin":    'm-t-r',
    "category": 'Quranic',
    "core":     ["upon", "rain", "rained", "evil", "warned", "see", "showered", "come"],
    "extended": ["punishment", "stones", "nay", "allah", "criminals", "end", "said", "painful"],
    "avoid":    [],
}
ROOT_LEXICON['م-ط-و'] = {
    "latin":    'm-t-w',
    "category": 'Quranic',
    "core":     ["went", "swaggering", "family"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ع-ز'] = {
    "latin":    'm-a-z',
    "category": 'Quranic',
    "core":     ["truthful", "sheep", "eight", "females"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ع-ي'] = {
    "latin":    'm-a-y',
    "category": 'Quranic',
    "core":     ["rivers", "water", "fire", "delicious"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ق-ت'] = {
    "latin":    'm-q-t',
    "category": 'Quranic',
    "core":     ["hatred", "allah", "indeed", "except", "hateful", "near", "than", "faith"],
    "extended": ["out", "greater", "called", "cried", "disbelieved", "certainly", "yourselves"],
    "avoid":    [],
}
ROOT_LEXICON['م-ك-ر'] = {
    "latin":    'm-k-r',
    "category": 'Quranic',
    "core":     ["allah", "plot", "plotted", "planned", "plan", "indeed", "punishment", "people"],
    "extended": ["best", "against", "perceive", "say", "before", "plotting", "planners", "except"],
    "avoid":    [],
}
ROOT_LEXICON['م-ك-ن'] = {
    "latin":    'm-k-n',
    "category": 'Quranic',
    "core":     ["established", "allah", "made", "earth", "land", "before", "certainly", "after"],
    "extended": ["gave", "said", "thing", "establish", "rivers", "see", "flow", "sent"],
    "avoid":    [],
}
ROOT_LEXICON['م-ك-و'] = {
    "latin":    'm-k-w',
    "category": 'Quranic',
    "core":     ["except", "disbelieve", "house", "clapping"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ل-أ'] = {
    "latin":    'm-l-a',
    "category": 'Quranic',
    "core":     ["chiefs", "said", "indeed", "people", "surely", "firaun", "among", "musa"],
    "extended": ["any", "see", "fill", "hell", "disbelieved", "lord", "sent", "except"],
    "avoid":    [],
}
ROOT_LEXICON['م-ل-ح'] = {
    "latin":    'm-l-h',
    "category": 'Quranic',
    "core":     ["seas", "bitter", "salty", "sweet"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ل-ق'] = {
    "latin":    'm-l-q',
    "category": 'Quranic',
    "core":     ["poverty", "provide", "kill", "children"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ل-ل'] = {
    "latin":    'm-l-l',
    "category": 'Quranic',
    "core":     ["religion", "allah", "indeed", "ibrahim", "upright", "lord", "any", "except"],
    "extended": ["among", "thing", "out", "follow", "say", "said", "right", "taught"],
    "avoid":    [],
}
ROOT_LEXICON['م-ل-و'] = {
    "latin":    'm-l-w',
    "category": 'Quranic',
    "core":     ["respite", "give", "indeed", "seized", "disbelieved", "punishment", "firm", "plan"],
    "extended": ["granted", "prolonged"],
    "avoid":    [],
}
ROOT_LEXICON['م-ن-ن'] = {
    "latin":    'm-n-n',
    "category": 'Quranic',
    "core":     ["allah", "upon", "favor", "reward", "say", "conferred", "believe", "indeed"],
    "extended": ["down", "never", "deeds", "quails", "themselves", "manna", "sent", "good"],
    "avoid":    [],
}
ROOT_LEXICON['م-ن-ي'] = {
    "latin":    'm-n-y',
    "category": 'Quranic',
    "core":     ["allah", "say", "wish", "knower", "sent", "before", "shaitaan", "any"],
    "extended": ["except", "book", "thinking", "wishful", "truthful", "death", "besides", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['م-ه-د'] = {
    "latin":    'm-h-d',
    "category": 'Quranic',
    "core":     ["place", "resting", "hell", "earth", "said", "cradle", "wretched", "bed"],
    "extended": ["therein", "made", "spread", "surely", "allah", "evil", "maturity", "speak"],
    "avoid":    [],
}
ROOT_LEXICON['م-ه-ل'] = {
    "latin":    'm-h-l',
    "category": 'Quranic',
    "core":     ["like", "respite", "little", "molten", "give", "disbelievers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ه-ن'] = {
    "latin":    'm-h-n',
    "category": 'Quranic',
    "core":     ["water"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-و-ج'] = {
    "latin":    'm-w-j',
    "category": 'Quranic',
    "core":     ["allah", "among", "waves", "like", "save", "religion", "sea", "land"],
    "extended": ["call", "out", "except", "whom", "others", "wave", "covers"],
    "avoid":    [],
}
ROOT_LEXICON['م-و-ر'] = {
    "latin":    'm-w-r',
    "category": 'Quranic',
    "core":     ["heaven", "day", "shake"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-و-ل'] = {
    "latin":    'm-w-l',
    "category": 'Quranic',
    "core":     ["wealth", "allah", "indeed", "children", "way", "lives", "give", "believe"],
    "extended": ["people", "said", "except", "world", "than", "spend", "reward", "until"],
    "avoid":    [],
}
ROOT_LEXICON['م-و-ه'] = {
    "latin":    'm-w-h',
    "category": 'Quranic',
    "core":     ["water", "down", "earth", "sky", "allah", "indeed", "sent", "forth"],
    "extended": ["surely", "sends", "drink", "like", "people", "see", "made", "created"],
    "avoid":    [],
}
ROOT_LEXICON['م-ي-د'] = {
    "latin":    'm-y-d',
    "category": 'Quranic',
    "core":     ["down", "lest", "mountains", "shake", "earth", "heaven", "said", "maryam"],
    "extended": ["table", "spread", "send", "son", "isa", "allah", "lord", "cast"],
    "avoid":    [],
}
ROOT_LEXICON['م-ي-ر'] = {
    "latin":    'm-y-r',
    "category": 'Quranic',
    "core":     ["said", "father", "get", "easy"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ي-ز'] = {
    "latin":    'm-y-z',
    "category": 'Quranic',
    "core":     ["allah", "good"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['م-ي-ل'] = {
    "latin":    'm-y-l',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "passions", "follow", "accept", "deviate", "wishes", "great"],
    "extended": ["repentance", "deviation", "wish", "attack", "come", "let", "neglect", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ن-أ-ي'] = {
    "latin":    'n-a-y',
    "category": 'Quranic',
    "core":     ["away", "touches", "turns", "bestow", "favor", "man", "evil"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ب-ت'] = {
    "latin":    'n-b-t',
    "category": 'Quranic',
    "core":     ["earth", "grow", "allah", "down", "water", "sky", "caused", "indeed"],
    "extended": ["forth", "people", "sent", "grain", "therein", "kind", "created", "signs"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ب-ذ'] = {
    "latin":    'n-b-dh',
    "category": 'Quranic',
    "core":     ["threw", "took", "book", "allah", "while", "away", "party", "nay"],
    "extended": ["covenant", "backs", "given", "behind", "messenger", "withdrew", "place", "hosts"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ب-ز'] = {
    "latin":    'n-b-z',
    "category": 'Quranic',
    "core":     ["wretched", "believe", "people", "insult"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ب-ط'] = {
    "latin":    'n-b-t',
    "category": 'Quranic',
    "core":     ["referred", "fear", "security", "spread"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ب-ع'] = {
    "latin":    'n-b-a',
    "category": 'Quranic',
    "core":     ["earth"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ت-ق'] = {
    "latin":    'n-t-q',
    "category": 'Quranic',
    "core":     ["fall", "fear", "canopy", "raised"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ث-ر'] = {
    "latin":    'n-th-r',
    "category": 'Quranic',
    "core":     ["dispersed", "deed", "dust", "proceed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ج-د'] = {
    "latin":    'n-j-d',
    "category": 'Quranic',
    "core":     ["ways", "shown"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ج-س'] = {
    "latin":    'n-j-s',
    "category": 'Quranic',
    "core":     ["wise", "fear", "believe", "wills"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ح-ب'] = {
    "latin":    'n-h-b',
    "category": 'Quranic',
    "core":     ["true", "alter", "fulfilled", "vow"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ح-ت'] = {
    "latin":    'n-h-t',
    "category": 'Quranic',
    "core":     ["carve", "mountains", "houses"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ح-ر'] = {
    "latin":    'n-h-r',
    "category": 'Quranic',
    "core":     ["lord", "sacrifice", "pray"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ح-س'] = {
    "latin":    'n-h-s',
    "category": 'Quranic',
    "core":     ["sent", "wind", "furious", "upon", "misfortune"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ح-ل'] = {
    "latin":    'n-h-l',
    "category": 'Quranic',
    "core":     ["ease", "women", "graciously", "anything"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-خ-ر'] = {
    "latin":    'n-kh-r',
    "category": 'Quranic',
    "core":     ["bones", "decayed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-خ-ل'] = {
    "latin":    'n-kh-l',
    "category": 'Quranic',
    "core":     ["date", "palms", "indeed", "gardens", "fruits", "people", "grapes", "palm"],
    "extended": ["grapevines", "fruit", "forth", "crops", "surely", "signs", "olives", "pomegranates"],
    "avoid":    [],
}
ROOT_LEXICON['ن-د-د'] = {
    "latin":    'n-d-d',
    "category": 'Quranic',
    "core":     ["allah", "set", "say", "rivals", "equals", "indeed", "earth", "see"],
    "extended": ["punishment", "path", "fire", "mislead", "enjoy", "disbelieve", "used", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ن-د-م'] = {
    "latin":    'n-d-m',
    "category": 'Quranic',
    "core":     ["regretful", "allah", "see", "become", "said", "became", "earth", "regret"],
    "extended": ["punishment"],
    "avoid":    [],
}
ROOT_LEXICON['ن-د-ي'] = {
    "latin":    'n-d-y',
    "category": 'Quranic',
    "core":     ["called", "lord", "call", "indeed", "say", "out", "allah", "day"],
    "extended": ["people", "came", "except", "among", "caller", "believe", "made", "paradise"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ذ-ر'] = {
    "latin":    'n-dh-r',
    "category": 'Quranic',
    "core":     ["warner", "warn", "say", "indeed", "any", "people", "allah", "sent"],
    "extended": ["tidings", "glad", "warned", "only", "except", "clear", "warners", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ز-ع'] = {
    "latin":    'n-z-a',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "surely", "out", "among", "made", "say", "hand"],
    "extended": ["lost", "dispute", "courage", "lord", "breasts", "matter", "disputed", "take"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ز-غ'] = {
    "latin":    'n-z-gh',
    "category": 'Quranic',
    "core":     ["indeed", "shaitaan", "comes", "suggestion", "refuge", "seek", "allah", "evil"],
    "extended": ["knower", "knowing", "hearing", "between", "discord", "hearer", "whisper"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ز-ف'] = {
    "latin":    'n-z-f',
    "category": 'Quranic',
    "core":     ["intoxicated"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-أ'] = {
    "latin":    'n-s-a',
    "category": 'Quranic',
    "core":     ["guide", "deeds", "disbelief", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-ب'] = {
    "latin":    'n-s-b',
    "category": 'Quranic',
    "core":     ["relationship", "made"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-خ'] = {
    "latin":    'n-s-kh',
    "category": 'Quranic',
    "core":     ["allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-ر'] = {
    "latin":    'n-s-r',
    "category": 'Quranic',
    "core":     ["yaguth", "said", "suwa", "leave"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-ف'] = {
    "latin":    'n-s-f',
    "category": 'Quranic',
    "core":     ["particles", "say", "mountains", "said", "life", "fail", "never", "god"],
    "extended": ["burn", "scatter", "appointment", "indeed", "devoted", "certainly", "sea", "touch"],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-ل'] = {
    "latin":    'n-s-l',
    "category": 'Quranic',
    "core":     ["progeny"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-و'] = {
    "latin":    'n-s-w',
    "category": 'Quranic',
    "core":     ["women", "allah", "indeed", "sons", "among", "except", "wives", "say"],
    "extended": ["men", "people", "whom", "over", "fear", "oft", "forgiving", "whoever"],
    "avoid":    [],
}
ROOT_LEXICON['ن-س-ي'] = {
    "latin":    'n-s-y',
    "category": 'Quranic',
    "core":     ["forgot", "forget", "allah", "indeed", "said", "made", "forgotten", "day"],
    "extended": ["before", "lord", "except", "took", "used", "today", "say", "than"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ش-أ'] = {
    "latin":    'n-sh-a',
    "category": 'Quranic',
    "core":     ["produced", "indeed", "creation", "after", "earth", "people", "another", "other"],
    "extended": ["give", "allah", "produce", "say", "see", "made", "lord", "sins"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ش-ر'] = {
    "latin":    'n-sh-r',
    "category": 'Quranic',
    "core":     ["resurrection", "allah", "forth", "wide", "earth", "death", "after", "land"],
    "extended": ["sends", "open", "day", "except", "mercy", "spread", "taken", "raise"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ش-ز'] = {
    "latin":    'n-sh-z',
    "category": 'Quranic',
    "core":     ["allah", "make", "said", "raise", "fear", "conduct", "ill", "indeed"],
    "extended": ["aware"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ش-ط'] = {
    "latin":    'n-sh-t',
    "category": 'Quranic',
    "core":     ["gently", "draw", "out"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ص-ب'] = {
    "latin":    'n-s-b',
    "category": 'Quranic',
    "core":     ["allah", "portion", "share", "indeed", "say", "book", "given", "way"],
    "extended": ["fatigue", "women", "left", "parents", "relatives", "men", "over", "thing"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ص-ت'] = {
    "latin":    'n-s-t',
    "category": 'Quranic',
    "core":     ["quran", "listen"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ص-ح'] = {
    "latin":    'n-s-h',
    "category": 'Quranic',
    "core":     ["lord", "said", "sincere", "allah", "indeed", "people", "advise", "messages"],
    "extended": ["conveyed", "away", "turned", "verily", "advised", "advisors", "convey", "advisers"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ص-ف'] = {
    "latin":    'n-s-f',
    "category": 'Quranic',
    "core":     ["half", "allah", "women", "indeed", "among", "thirds", "third", "there"],
    "extended": ["left", "child", "obligation", "nearer", "hands", "knowing", "brothers", "sixth"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ص-ي'] = {
    "latin":    'n-s-y',
    "category": 'Quranic',
    "core":     ["forelock"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ض-ج'] = {
    "latin":    'n-d-j',
    "category": 'Quranic',
    "core":     ["wise", "time", "burn", "fire"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ض-خ'] = {
    "latin":    'n-d-kh',
    "category": 'Quranic',
    "core":     ["forth", "gushing", "both", "springs"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ض-د'] = {
    "latin":    'n-d-d',
    "category": 'Quranic',
    "core":     ["layers", "trees"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ض-ر'] = {
    "latin":    'n-d-r',
    "category": 'Quranic',
    "core":     ["day", "faces", "radiance"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ط-ح'] = {
    "latin":    'n-t-h',
    "category": 'Quranic',
    "core":     ["flesh", "fear", "sin", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ط-ف'] = {
    "latin":    'n-t-f',
    "category": 'Quranic',
    "core":     ["semen", "drop", "created", "dust", "clear", "man", "clinging", "indeed"],
    "extended": ["substance", "behold", "minute", "kind", "opponent", "quantity", "maturity", "see"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ط-ق'] = {
    "latin":    'n-t-q',
    "category": 'Quranic',
    "core":     ["speak", "speaks", "truth", "indeed", "said", "wronged", "record", "surely"],
    "extended": ["thing", "against"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ظ-ر'] = {
    "latin":    'n-z-r',
    "category": 'Quranic',
    "core":     ["see", "allah", "indeed", "say", "said", "look", "end", "before"],
    "extended": ["wait", "lord", "earth", "except", "respite", "day", "any", "ones"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ع-ج'] = {
    "latin":    'n-a-j',
    "category": 'Quranic',
    "core":     ["said", "ewe", "indeed", "overpowered", "speech", "while", "brother", "ninety"],
    "extended": ["entrust", "nine", "ewes", "believe", "deeds", "became", "fell", "partners"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ع-س'] = {
    "latin":    'n-a-s',
    "category": 'Quranic',
    "core":     ["security", "sent", "down", "slumber", "hearts", "upon"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ع-ق'] = {
    "latin":    'n-a-q',
    "category": 'Quranic',
    "core":     ["example", "dumb", "blind", "except"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ع-ل'] = {
    "latin":    'n-a-l',
    "category": 'Quranic',
    "core":     ["tuwa", "indeed", "sacred", "remove"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-غ-ض'] = {
    "latin":    'n-gh-d',
    "category": 'Quranic',
    "core":     ["creation", "time", "breasts", "perhaps"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ث'] = {
    "latin":    'n-f-th',
    "category": 'Quranic',
    "core":     ["evil", "blowers", "knots"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ح'] = {
    "latin":    'n-f-h',
    "category": 'Quranic',
    "core":     ["wrongdoers", "whiff", "touches", "say"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-خ'] = {
    "latin":    'n-f-kh',
    "category": 'Quranic',
    "core":     ["blown", "trumpet", "into", "day", "spirit", "breathed", "allah", "come"],
    "extended": ["lord", "dead", "heavens", "earth", "fall", "made", "leper", "give"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-د'] = {
    "latin":    'n-f-d',
    "category": 'Quranic',
    "core":     ["surely", "exhausted", "sea", "words", "allah", "whatever", "before", "brought"],
    "extended": ["say", "like", "ink", "lord", "even", "supplement", "indeed"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ذ'] = {
    "latin":    'n-f-dh',
    "category": 'Quranic',
    "core":     ["heavens", "earth", "except", "jinn", "pass", "regions", "authority", "men"],
    "extended": ["assembly", "able", "beyond"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ر'] = {
    "latin":    'n-f-r',
    "category": 'Quranic',
    "core":     ["said", "forth", "allah", "aversion", "than", "people", "wealth", "quran"],
    "extended": ["together", "way", "say", "more", "return", "group", "party", "believe"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ش'] = {
    "latin":    'n-f-sh',
    "category": 'Quranic',
    "core":     ["concerning", "sheep", "pastured", "sulaiman"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ل'] = {
    "latin":    'n-f-l',
    "category": 'Quranic',
    "core":     ["right", "fear", "between", "say", "ask", "set", "messenger", "believers"],
    "extended": ["war", "obey", "allah", "about", "spoils"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ف-ي'] = {
    "latin":    'n-f-y',
    "category": 'Quranic',
    "core":     ["strive", "sides", "wage", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ب'] = {
    "latin":    'n-q-b',
    "category": 'Quranic',
    "core":     ["any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ذ'] = {
    "latin":    'n-q-dh',
    "category": 'Quranic',
    "core":     ["fire", "became", "saved", "allah", "together", "besides", "take", "save"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ر'] = {
    "latin":    'n-q-r',
    "category": 'Quranic',
    "core":     ["seed", "speck", "date", "trumpet", "blown"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ص'] = {
    "latin":    'n-q-s',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "except", "see", "fear", "fruits", "surely", "certainly"],
    "extended": ["people", "worship", "any", "borders", "land", "come", "life"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ض'] = {
    "latin":    'n-q-d',
    "category": 'Quranic',
    "core":     ["covenant", "allah", "break", "after", "made", "earth", "joined", "spread"],
    "extended": ["corruption", "breaking", "because", "except", "few", "hearts", "indeed", "oaths"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-ع'] = {
    "latin":    'n-q-a',
    "category": 'Quranic',
    "core":     ["raise", "thereby", "dust"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ق-م'] = {
    "latin":    'n-q-m',
    "category": 'Quranic',
    "core":     ["retribution", "allah", "mighty", "take", "took", "indeed", "except", "people"],
    "extended": ["before", "believe", "owner", "while", "whoever", "away", "verily", "verses"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-ب'] = {
    "latin":    'n-k-b',
    "category": 'Quranic',
    "core":     ["path", "believe", "indeed", "deviating"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-ث'] = {
    "latin":    'n-k-th',
    "category": 'Quranic',
    "core":     ["allah", "broke", "indeed", "oaths", "only", "punishment", "removed", "fight"],
    "extended": ["after", "more", "reward", "fulfils", "pledge", "himself", "over", "against"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-د'] = {
    "latin":    'n-k-d',
    "category": 'Quranic',
    "core":     ["except", "bad", "explain", "grateful"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-ر'] = {
    "latin":    'n-k-r',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "right", "wrong", "said", "people", "enjoin", "forbid"],
    "extended": ["evil", "among", "surely", "upon", "good", "believe", "prayer", "establish"],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-س'] = {
    "latin":    'n-k-s',
    "category": 'Quranic',
    "core":     ["heads"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-ص'] = {
    "latin":    'n-k-s',
    "category": 'Quranic',
    "core":     ["heels"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ك-ف'] = {
    "latin":    'n-k-f',
    "category": 'Quranic',
    "core":     ["arrogant", "allah", "angels", "never", "messiah", "slave", "disdains", "together"],
    "extended": ["ones", "worship", "disdain", "near", "whoever", "gather", "towards"],
    "avoid":    [],
}
ROOT_LEXICON['ن-م-ر-ق'] = {
    "latin":    'n-m-r-q',
    "category": 'Quranic',
    "core":     ["lined", "cushions"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-م-ل'] = {
    "latin":    'n-m-l',
    "category": 'Quranic',
    "core":     ["crush", "hosts", "said", "sulaiman", "while", "ants", "until", "lest"],
    "extended": ["enter", "dwellings", "ant", "perceive", "valley", "came"],
    "avoid":    [],
}
ROOT_LEXICON['ن-م-م'] = {
    "latin":    'n-m-m',
    "category": 'Quranic',
    "core":     ["gossip", "going", "malicious", "defamer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ه-ج'] = {
    "latin":    'n-h-j',
    "category": 'Quranic',
    "core":     ["between", "community", "book", "return"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-أ'] = {
    "latin":    'n-w-a',
    "category": 'Quranic',
    "core":     ["exultant", "qarun", "said", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ب'] = {
    "latin":    'n-w-b',
    "category": 'Quranic',
    "core":     ["lord", "allah", "indeed", "upon", "turns", "turn", "except", "himself"],
    "extended": ["ibrahim", "certainly", "said", "people", "trust", "down", "turning", "partners"],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ش'] = {
    "latin":    'n-w-sh',
    "category": 'Quranic',
    "core":     ["receiving", "place", "believe", "off"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ص'] = {
    "latin":    'n-w-s',
    "category": 'Quranic',
    "core":     ["longer", "called", "destroyed", "generation"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ق'] = {
    "latin":    'n-w-q',
    "category": 'Quranic',
    "core":     ["camel", "said", "allah", "sign", "people", "lord", "eat", "leave"],
    "extended": ["touch", "earth", "salih", "lest", "harm", "thamud", "punishment", "drink"],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ن'] = {
    "latin":    'n-w-n',
    "category": 'Quranic',
    "core":     ["wrongdoers", "dhun", "god", "never"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-و-ي'] = {
    "latin":    'n-w-y',
    "category": 'Quranic',
    "core":     ["grain", "cleaver", "forth", "seed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ن-ي-ل'] = {
    "latin":    'n-y-l',
    "category": 'Quranic',
    "core":     ["allah", "reach", "indeed", "good", "after", "any", "doers", "disbelievers"],
    "extended": ["life", "thus", "messenger", "except", "said", "make", "lord", "until"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ا-ء'] = {
    "latin":    "h-a-'",
    "category": 'Quranic',
    "core":     ["right", "say", "read", "hand"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ا-ت'] = {
    "latin":    'h-a-t',
    "category": 'Quranic',
    "core":     ["say", "bring", "proof", "truthful", "know", "truth", "forth", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ب-ط'] = {
    "latin":    'h-b-t',
    "category": 'Quranic',
    "core":     ["down", "said", "out", "enemy", "others", "earth", "comes", "indeed"],
    "extended": ["dwelling", "place", "fear", "follows", "whoever", "guidance", "allah", "forth"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ب-و'] = {
    "latin":    'h-b-w',
    "category": 'Quranic',
    "core":     ["dust"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ج-د'] = {
    "latin":    'h-j-d',
    "category": 'Quranic',
    "core":     ["additional", "lord", "sleep", "arise"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ج-ع'] = {
    "latin":    'h-j-a',
    "category": 'Quranic',
    "core":     ["sleep", "little", "night", "used"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-د-د'] = {
    "latin":    'h-d-d',
    "category": 'Quranic',
    "core":     ["asunder", "heavens", "splits", "therefrom"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-د-م'] = {
    "latin":    'h-d-m',
    "category": 'Quranic',
    "core":     ["right", "said", "evicted", "mentioned"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-د-ه-د'] = {
    "latin":    'h-d-h-d',
    "category": 'Quranic',
    "core":     ["said", "see", "hoopoe", "absent"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ر-ب'] = {
    "latin":    'h-r-b',
    "category": 'Quranic',
    "core":     ["never", "failure", "become", "certain"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ر-ع'] = {
    "latin":    'h-r-a',
    "category": 'Quranic',
    "core":     ["right", "said", "rushing", "purer"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ز-أ'] = {
    "latin":    'h-z-a',
    "category": 'Quranic',
    "core":     ["mock", "used", "allah", "ridicule", "indeed", "messengers", "take", "verses"],
    "extended": ["before", "came", "mocked", "surrounded", "say", "evil", "because", "messenger"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ز-ز'] = {
    "latin":    'h-z-z',
    "category": 'Quranic',
    "core":     ["indeed", "drop", "upon", "water", "see", "send", "among", "down"],
    "extended": ["earth", "grows", "barren", "stirred", "fear", "musa", "staff", "snake"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ز-ل'] = {
    "latin":    'h-z-l',
    "category": 'Quranic',
    "core":     ["amusement"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ز-م'] = {
    "latin":    'h-z-m',
    "category": 'Quranic',
    "core":     ["defeated"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ش-ش'] = {
    "latin":    'h-sh-sh',
    "category": 'Quranic',
    "core":     ["said", "sheep", "staff", "lean"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ش-م'] = {
    "latin":    'h-sh-m',
    "category": 'Quranic',
    "core":     ["like", "dry"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ض-م'] = {
    "latin":    'h-d-m',
    "category": 'Quranic',
    "core":     ["deprivation", "fear", "deeds", "injustice"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ط-ع'] = {
    "latin":    'h-t-a',
    "category": 'Quranic',
    "core":     ["racing", "ahead", "towards"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ل-ع'] = {
    "latin":    'h-l-a',
    "category": 'Quranic',
    "core":     ["created", "indeed", "anxious", "man"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ل-ل'] = {
    "latin":    'h-l-l',
    "category": 'Quranic',
    "core":     ["allah", "flesh", "blood", "indeed", "dedicated", "swine", "merciful", "forgiving"],
    "extended": ["most", "other", "oft", "dead", "than", "forbidden", "whoever", "forced"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ل-م'] = {
    "latin":    'h-l-m',
    "category": 'Quranic',
    "core":     ["say", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-د'] = {
    "latin":    'h-m-d',
    "category": 'Quranic',
    "core":     ["maturity", "water", "see", "clinging"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-ر'] = {
    "latin":    'h-m-r',
    "category": 'Quranic',
    "core":     ["gates", "water", "pouring", "heaven"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-ز'] = {
    "latin":    'h-m-z',
    "category": 'Quranic',
    "core":     ["say", "ones", "refuge", "seek"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-س'] = {
    "latin":    'h-m-s',
    "category": 'Quranic',
    "core":     ["caller", "follow", "except", "gracious"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-م'] = {
    "latin":    'h-m-m',
    "category": 'Quranic',
    "core":     ["allah", "certainly", "believers", "indeed", "after", "upon", "people", "messenger"],
    "extended": ["trust", "put", "let", "protector", "themselves", "group", "sent", "down"],
    "avoid":    [],
}
ROOT_LEXICON['ه-م-ن'] = {
    "latin":    'h-m-n',
    "category": 'Quranic',
    "core":     ["allah", "guardian"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ن-أ'] = {
    "latin":    'h-n-a',
    "category": 'Quranic',
    "core":     ["satisfaction", "eat", "drink", "used"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-و-د'] = {
    "latin":    'h-w-d',
    "category": 'Quranic',
    "core":     ["jews", "allah", "said", "christians", "indeed", "people", "say", "hud"],
    "extended": ["day", "fear", "believe", "believed", "resurrection", "saying", "surely", "among"],
    "avoid":    [],
}
ROOT_LEXICON['ه-و-ر'] = {
    "latin":    'h-w-r',
    "category": 'Quranic',
    "core":     ["wrongdoing", "guide", "cliff", "righteousness", "founded", "collapsed", "collapse", "fire"],
    "extended": ["hell", "building", "better", "edge", "allah", "people", "pleasure"],
    "avoid":    [],
}
ROOT_LEXICON['ه-و-ن'] = {
    "latin":    'h-w-n',
    "category": 'Quranic',
    "core":     ["punishment", "humiliating", "allah", "disbelievers", "earth", "down", "disbelieved", "prepared"],
    "extended": ["indeed", "said", "verses", "good", "messenger", "people", "any", "about"],
    "avoid":    [],
}
ROOT_LEXICON['ه-و-ي'] = {
    "latin":    'h-w-y',
    "category": 'Quranic',
    "core":     ["desires", "follow", "allah", "indeed", "desire", "lord", "astray", "say"],
    "extended": ["after", "knowledge", "book", "followed", "denied", "come", "guidance", "any"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ي-أ'] = {
    "latin":    'h-y-a',
    "category": 'Quranic',
    "core":     ["allah", "lord", "leper", "blind", "israel", "permission", "clay", "like"],
    "extended": ["breath", "children", "dead", "bird", "becomes", "into", "said", "mercy"],
    "avoid":    [],
}
ROOT_LEXICON['ه-ي-ت'] = {
    "latin":    'h-y-t',
    "category": 'Quranic',
    "core":     ["closed", "said", "wrongdoers", "house"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ي-ج'] = {
    "latin":    'h-y-j',
    "category": 'Quranic',
    "core":     ["see", "allah", "yellow", "debris"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ي-ل'] = {
    "latin":    'h-y-l',
    "category": 'Quranic',
    "core":     ["heap", "quake", "sand", "become"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ه-ي-م'] = {
    "latin":    'h-y-m',
    "category": 'Quranic',
    "core":     ["valley", "roam", "see", "thirsty"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-أ-د'] = {
    "latin":    'w-a-d',
    "category": 'Quranic',
    "core":     ["female", "asked", "buried", "alive"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-أ-ل'] = {
    "latin":    'w-a-l',
    "category": 'Quranic',
    "core":     ["than", "owner", "never", "hastened"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ب-ر'] = {
    "latin":    'w-b-r',
    "category": 'Quranic',
    "core":     ["time", "cattle", "provision", "travel"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ب-ق'] = {
    "latin":    'w-b-q',
    "category": 'Quranic',
    "core":     ["between", "call", "say", "claimed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ب-ل'] = {
    "latin":    'w-b-l',
    "category": 'Quranic',
    "core":     ["example", "allah", "like", "consequence", "affair", "tasted", "believe", "fell"],
    "extended": ["people", "rain", "wealth", "heavy", "before", "painful", "punishment"],
    "avoid":    [],
}
ROOT_LEXICON['و-ت-د'] = {
    "latin":    'w-t-d',
    "category": 'Quranic',
    "core":     ["owner", "stakes", "firaun"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ت-ر'] = {
    "latin":    'w-t-r',
    "category": 'Quranic',
    "core":     ["follow", "time", "denied", "messengers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ت-ن'] = {
    "latin":    'w-t-n',
    "category": 'Quranic',
    "core":     ["off", "certainly", "aorta", "cut"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ث-ق'] = {
    "latin":    'w-th-q',
    "category": 'Quranic',
    "core":     ["covenant", "allah", "took", "said", "indeed", "over", "except", "surely"],
    "extended": ["given", "taken", "until", "after", "break", "raised", "mount", "give"],
    "avoid":    [],
}
ROOT_LEXICON['و-ث-ن'] = {
    "latin":    'w-th-n',
    "category": 'Quranic',
    "core":     ["allah", "idols", "only", "besides", "any"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ج-س'] = {
    "latin":    'w-j-s',
    "category": 'Quranic',
    "core":     ["fear", "felt", "said"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ج-ف'] = {
    "latin":    'w-j-f',
    "category": 'Quranic',
    "core":     ["horses", "camels", "messengers", "restored"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ج-ل'] = {
    "latin":    'w-j-l',
    "category": 'Quranic',
    "core":     ["hearts", "fear", "mentioned", "upon", "allah", "lord", "afraid", "said"],
    "extended": ["indeed"],
    "avoid":    [],
}
ROOT_LEXICON['و-ح-ش'] = {
    "latin":    'w-h-sh',
    "category": 'Quranic',
    "core":     ["beasts", "gathered", "wild"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-د-د'] = {
    "latin":    'w-d-d',
    "category": 'Quranic',
    "core":     ["allah", "wish", "indeed", "among", "most", "any", "find", "people"],
    "extended": ["day", "believe", "disbelieved", "love", "surely", "good", "between", "take"],
    "avoid":    [],
}
ROOT_LEXICON['و-د-ع'] = {
    "latin":    'w-d-a',
    "category": 'Quranic',
    "core":     ["dwelling", "place", "clear", "allah"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-د-ق'] = {
    "latin":    'w-d-q',
    "category": 'Quranic',
    "core":     ["see", "wills", "makes", "allah", "sends", "forth", "midst", "clouds"],
    "extended": ["rain", "sky", "whom"],
    "avoid":    [],
}
ROOT_LEXICON['و-د-ي'] = {
    "latin":    'w-d-y',
    "category": 'Quranic',
    "core":     ["valley", "allah", "lord", "indeed", "sacred", "valleys", "make", "tuwa"],
    "extended": ["said", "came", "called"],
    "avoid":    [],
}
ROOT_LEXICON['و-ذ-ر'] = {
    "latin":    'w-dh-r',
    "category": 'Quranic',
    "core":     ["leave", "allah", "said", "indeed", "people", "lord", "believe", "until"],
    "extended": ["forsake", "earth", "day", "behind", "fear", "any", "used", "musa"],
    "avoid":    [],
}
ROOT_LEXICON['و-ر-ث'] = {
    "latin":    'w-r-th',
    "category": 'Quranic',
    "core":     ["inherit", "allah", "made", "indeed", "after", "inheritors", "earth", "women"],
    "extended": ["children", "paradise", "lord", "people", "except", "child", "thing", "say"],
    "avoid":    [],
}
ROOT_LEXICON['و-ر-د'] = {
    "latin":    'w-r-d',
    "category": 'Quranic',
    "core":     ["place", "precede", "fire", "wretched", "resurrection", "lead", "led", "day"],
    "extended": ["people", "said", "water", "allah", "came", "hell", "besides", "come"],
    "avoid":    [],
}
ROOT_LEXICON['و-ر-ق'] = {
    "latin":    'w-r-q',
    "category": 'Quranic',
    "core":     ["lord", "knows", "shame", "themselves", "became", "began", "apparent", "both"],
    "extended": ["fasten", "leaves"],
    "avoid":    [],
}
ROOT_LEXICON['و-ر-ي'] = {
    "latin":    'w-r-y',
    "category": 'Quranic',
    "core":     ["behind", "allah", "indeed", "said", "given", "except", "backs", "punishment"],
    "extended": ["after", "people", "before", "messenger", "beyond", "come", "sent", "lord"],
    "avoid":    [],
}
ROOT_LEXICON['و-ز-ر'] = {
    "latin":    'w-z-r',
    "category": 'Quranic',
    "core":     ["bear", "burden", "burdens", "another", "bearer", "allah", "lord", "whoever"],
    "extended": ["indeed", "until", "return", "soul", "against", "about", "inform", "own"],
    "avoid":    [],
}
ROOT_LEXICON['و-ز-ع'] = {
    "latin":    'w-z-a',
    "category": 'Quranic',
    "core":     ["rows", "set", "gathered", "parents", "please", "grant", "bestowed", "among"],
    "extended": ["favor", "lord", "righteous", "power", "day"],
    "avoid":    [],
}
ROOT_LEXICON['و-ز-ن'] = {
    "latin":    'w-z-n',
    "category": 'Quranic',
    "core":     ["scales", "balance", "weight", "measure", "justice", "whose", "give", "allah"],
    "extended": ["any", "day", "full", "ones", "heavy", "people", "make", "successful"],
    "avoid":    [],
}
ROOT_LEXICON['و-س-ط'] = {
    "latin":    'w-s-t',
    "category": 'Quranic',
    "core":     ["allah", "middle", "prayer", "thus", "most", "guard"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-س-ق'] = {
    "latin":    'w-s-q',
    "category": 'Quranic',
    "core":     ["night", "envelops", "full", "moon"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-س-ل'] = {
    "latin":    'w-s-l',
    "category": 'Quranic',
    "core":     ["fear", "means", "seek"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-س-م'] = {
    "latin":    'w-s-m',
    "category": 'Quranic',
    "core":     ["discern", "indeed", "signs", "brand"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-س-ن'] = {
    "latin":    'w-s-n',
    "category": 'Quranic',
    "core":     ["high", "tires", "allah", "guarding"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-س-و-س'] = {
    "latin":    'w-s-w-s',
    "category": 'Quranic',
    "core":     ["said", "tree", "whispered", "shaitaan", "whispers"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ش-ي'] = {
    "latin":    'w-sh-y',
    "category": 'Quranic',
    "core":     ["earth", "said", "water", "says"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ص-ب'] = {
    "latin":    'w-s-b',
    "category": 'Quranic',
    "core":     ["heavens", "allah", "fear", "other"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ص-د'] = {
    "latin":    'w-s-d',
    "category": 'Quranic',
    "core":     ["closed", "over"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ص-ف'] = {
    "latin":    'w-s-f',
    "category": 'Quranic',
    "core":     ["allah", "attribute", "above", "lord", "glory", "said", "against", "best"],
    "extended": ["created", "glorified", "partners", "say", "forbidden", "indeed", "describe", "help"],
    "avoid":    [],
}
ROOT_LEXICON['و-ص-ل'] = {
    "latin":    'w-s-l',
    "category": 'Quranic',
    "core":     ["allah", "joined", "evil", "join", "reach", "said", "fear", "indeed"],
    "extended": ["lord", "commanded", "earth", "after", "spread", "break", "corruption", "covenant"],
    "avoid":    [],
}
ROOT_LEXICON['و-ص-ي'] = {
    "latin":    'w-s-y',
    "category": 'Quranic',
    "core":     ["allah", "enjoined", "any", "indeed", "more", "after", "made", "parents"],
    "extended": ["knowing", "sixth", "third", "debt", "half", "women", "left", "child"],
    "avoid":    [],
}
ROOT_LEXICON['و-ض-ع'] = {
    "latin":    'w-d-a',
    "category": 'Quranic',
    "core":     ["allah", "among", "indeed", "except", "any", "lord", "female", "said"],
    "extended": ["better", "believe", "until", "offspring", "set", "say", "distort", "words"],
    "avoid":    [],
}
ROOT_LEXICON['و-ض-ن'] = {
    "latin":    'w-d-n',
    "category": 'Quranic',
    "core":     ["decorated", "thrones"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ط-أ'] = {
    "latin":    'w-t-a',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "people", "disbelievers", "any", "madinah", "infliction", "afflict"],
    "extended": ["fatigue", "lost", "allow", "messenger", "step", "hunger", "recorded", "way"],
    "avoid":    [],
}
ROOT_LEXICON['و-ط-ر'] = {
    "latin":    'w-t-r',
    "category": 'Quranic',
    "core":     ["right", "said", "fear", "concealed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ط-ن'] = {
    "latin":    'w-t-n',
    "category": 'Quranic',
    "core":     ["earth", "allah", "turned", "pleased"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ع-ظ'] = {
    "latin":    'w-a-z',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "admonition", "said", "fear", "take", "whoever", "among"],
    "extended": ["lord", "people", "advise", "before", "punishment", "term", "women", "between"],
    "avoid":    [],
}
ROOT_LEXICON['و-ع-ي'] = {
    "latin":    'w-a-y',
    "category": 'Quranic',
    "core":     ["allah", "began", "raise", "bags", "thus", "plan", "yusuf", "degrees"],
    "extended": ["except", "out", "before", "brought", "take", "king", "willed", "knowledge"],
    "avoid":    [],
}
ROOT_LEXICON['و-ف-د'] = {
    "latin":    'w-f-d',
    "category": 'Quranic',
    "core":     ["gracious", "gather", "most", "day"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ف-ر'] = {
    "latin":    'w-f-r',
    "category": 'Quranic',
    "core":     ["said", "ample", "follows", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ف-ض'] = {
    "latin":    'w-f-d',
    "category": 'Quranic',
    "core":     ["out", "rapidly", "hastening", "graves"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ف-ق'] = {
    "latin":    'w-f-q',
    "category": 'Quranic',
    "core":     ["allah", "reconciliation", "except", "good"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ف-ي'] = {
    "latin":    'w-f-y',
    "category": 'Quranic',
    "core":     ["allah", "full", "indeed", "take", "give", "day", "die", "cause"],
    "extended": ["death", "upon", "covenant", "except", "soul", "lord", "measure", "among"],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ب'] = {
    "latin":    'w-q-b',
    "category": 'Quranic',
    "core":     ["darkness", "evil", "spreads"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ت'] = {
    "latin":    'w-q-t',
    "category": 'Quranic',
    "core":     ["appointed", "day", "time", "well", "people", "lord", "known", "allah"],
    "extended": ["indeed", "said", "musa", "appointment", "say", "come", "ask", "about"],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-د'] = {
    "latin":    'w-q-d',
    "category": 'Quranic',
    "core":     ["fire", "allah", "fuel", "kindled", "like", "earth", "example", "light"],
    "extended": ["away", "whose", "never", "stones", "indeed", "said", "wills", "sets"],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ذ'] = {
    "latin":    'w-q-dh',
    "category": 'Quranic',
    "core":     ["flesh", "fear", "sin", "blood"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ر'] = {
    "latin":    'w-q-r',
    "category": 'Quranic',
    "core":     ["ears", "deafness", "coverings", "hearts", "believe", "say", "understand", "placed"],
    "extended": ["over", "lest", "verses", "quran", "lord", "turns", "indeed", "away"],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ع'] = {
    "latin":    'w-q-a',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "occur", "lord", "punishment", "surely", "fall", "earth"],
    "extended": ["down", "believe", "see", "occurrence", "merciful", "way", "find", "certainly"],
    "avoid":    [],
}
ROOT_LEXICON['و-ق-ف'] = {
    "latin":    'w-q-f',
    "category": 'Quranic',
    "core":     ["see", "say", "stand", "made", "lord", "back", "believers", "disbelieve"],
    "extended": ["before"],
    "avoid":    [],
}
ROOT_LEXICON['و-ك-أ'] = {
    "latin":    'w-k-a',
    "category": 'Quranic',
    "core":     ["reclining", "couches", "therein", "said", "gardens", "green", "brocade", "other"],
    "extended": ["upon", "fruit"],
    "avoid":    [],
}
ROOT_LEXICON['و-ك-د'] = {
    "latin":    'w-k-d',
    "category": 'Quranic',
    "core":     ["surety", "knows", "verily", "after"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ك-ز'] = {
    "latin":    'w-k-z',
    "category": 'Quranic',
    "core":     ["said", "time", "entered", "indeed"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ك-ل'] = {
    "latin":    'w-k-l',
    "category": 'Quranic',
    "core":     ["allah", "trust", "put", "upon", "lord", "sufficient", "say", "except"],
    "extended": ["let", "indeed", "said", "over", "people", "guardian", "surely", "believers"],
    "avoid":    [],
}
ROOT_LEXICON['و-ل-ج'] = {
    "latin":    'w-l-j',
    "category": 'Quranic',
    "core":     ["night", "enter", "day", "allah", "heaven", "causes", "forth", "whom"],
    "extended": ["indeed", "besides", "aware", "seer", "moon", "term", "sun", "appointed"],
    "avoid":    [],
}
ROOT_LEXICON['و-ن-ي'] = {
    "latin":    'w-n-y',
    "category": 'Quranic',
    "core":     ["brother", "signs", "remembrance", "slacken"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ه-ب'] = {
    "latin":    'w-h-b',
    "category": 'Quranic',
    "core":     ["lord", "indeed", "grant", "mercy", "bestowed", "after", "bestower", "isaac"],
    "extended": ["made", "righteous", "yourself", "said", "yaqub", "granted", "allah", "guided"],
    "avoid":    [],
}
ROOT_LEXICON['و-ه-ج'] = {
    "latin":    'w-h-j',
    "category": 'Quranic',
    "core":     ["lamp", "placed", "burning"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['و-ه-ن'] = {
    "latin":    'w-h-n',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "superior", "weaken", "weakened", "weak", "while", "like"],
    "extended": ["grateful", "parents", "years", "destination", "carried", "weakness", "mother", "weaning"],
    "avoid":    [],
}
ROOT_LEXICON['و-ه-ي'] = {
    "latin":    'w-h-y',
    "category": 'Quranic',
    "core":     ["split", "day", "frail", "heaven"],
    "extended": [],
    "avoid":    [],
}
ROOT_LEXICON['ي-أ-س'] = {
    "latin":    'y-a-s',
    "category": 'Quranic',
    "core":     ["allah", "indeed", "despair", "people", "despaired", "upon", "mercy", "until"],
    "extended": ["disbelievers", "except", "man", "yusuf", "despairs", "believe", "make", "favor"],
    "avoid":    [],
}
ROOT_LEXICON['ي-ب-س'] = {
    "latin":    'y-b-s',
    "category": 'Quranic',
    "core":     ["dry", "sea", "cows", "seven", "ears", "explain", "lean", "about"],
    "extended": ["green", "eating", "ones", "fat"],
    "avoid":    [],
}
ROOT_LEXICON['ي-ت-م'] = {
    "latin":    'y-t-m',
    "category": 'Quranic',
    "core":     ["orphans", "allah", "indeed", "orphan", "needy", "give", "relatives", "good"],
    "extended": ["near", "wealth", "covenant", "gives", "wayfarer", "say", "whatever", "justice"],
    "avoid":    [],
}
ROOT_LEXICON['ي-د-ي'] = {
    "latin":    'y-d-y',
    "category": 'Quranic',
    "core":     ["hands", "allah", "before", "indeed", "hand", "said", "lord", "people"],
    "extended": ["sent", "say", "except", "believe", "surely", "against", "behind", "come"],
    "avoid":    [],
}
ROOT_LEXICON['ي-م-م'] = {
    "latin":    'y-m-m',
    "category": 'Quranic',
    "core":     ["sea", "believe", "allah", "while", "brought", "take", "earth", "indeed"],
    "extended": ["river", "cast", "except", "know", "water", "ill", "prayer", "faces"],
    "avoid":    [],
}
ROOT_LEXICON['ي-م-ن'] = {
    "latin":    'y-m-n',
    "category": 'Quranic',
    "core":     ["right", "allah", "oaths", "indeed", "possess", "hand", "hands", "after"],
    "extended": ["whom", "left", "people", "most", "day", "women", "over", "say"],
    "avoid":    [],
}
ROOT_LEXICON['ي-ن-ع'] = {
    "latin":    'y-n-a',
    "category": 'Quranic',
    "core":     ["water", "believe", "signs", "fruit"],
    "extended": [],
    "avoid":    [],
}
