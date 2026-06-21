# src/mock_data.py
# ─────────────────────────────────────────────────────────────────────────────
# Quranic Cross-Lingual Translation Auditor
# Seed dataset — 10 Ayat across 5 Surahs
#
# Conventions:
#   · Ayah 1:1  →  "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ"  (NOT Bismillah)
#   · All translations use "Allah" (never "God")
#   · Unit label: Ayah (pl. Ayat)
# ─────────────────────────────────────────────────────────────────────────────

AYAT_DATA = [
    # ── Surah Al-Fatiha (1) ──────────────────────────────────────────────────
    {
        "ayah_key": "1:1",
        "surah_name": "Al-Fatiha",
        "arabic": "الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ",
        "roots": {
            "الْحَمْدُ": "ح-م-د",
            "لِلَّهِ":   "أ-ل-ه",
            "رَبِّ":     "ر-ب-ب",
            "الْعَالَمِينَ": "ع-ل-م"
        },
        "trans_sahih":   "All praise is due to Allah, Lord of the worlds.",
        "trans_haleem":  "Praise belongs to Allah, Lord of the Worlds.",
        "trans_khattab": "All praise is for Allah—Lord of all worlds.",
        "trans_soliman": "Praised be Allah, the Lord of the universe."
    },
    {
        "ayah_key": "1:2",
        "surah_name": "Al-Fatiha",
        "arabic": "الرَّحْمَٰنِ الرَّحِيمِ",
        "roots": {
            "الرَّحْمَٰنِ": "ر-ح-م",
            "الرَّحِيمِ":  "ر-ح-م"
        },
        "trans_sahih":   "The Entirely Merciful, the Especially Merciful.",
        "trans_haleem":  "The Lord of Mercy, the Giver of Mercy.",
        "trans_khattab": "The Most Compassionate, Most Merciful.",
        "trans_soliman": "The Almighty Merciful, the Especially Merciful."
    },
    {
        "ayah_key": "1:3",
        "surah_name": "Al-Fatiha",
        "arabic": "مَالِكِ يَوْمِ الدِّينِ",
        "roots": {
            "مَالِكِ": "م-ل-ك",
            "يَوْمِ":  "ي-و-م",
            "الدِّينِ": "د-ي-ن"
        },
        "trans_sahih":   "Sovereign of the Day of Recompense.",
        "trans_haleem":  "Master of the Day of Judgement.",
        "trans_khattab": "Master of the Day of Judgment.",
        "trans_soliman": "Owner of the Day of Retribution."
    },

    # ── Surah Al-Baqarah (2) ─────────────────────────────────────────────────
    {
        "ayah_key": "2:255",
        "surah_name": "Al-Baqarah",
        "arabic": "اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ",
        "roots": {
            "اللَّهُ":    "أ-ل-ه",
            "إِلَٰهَ":   "أ-ل-ه",
            "الْحَيُّ":  "ح-ي-ي",
            "الْقَيُّومُ": "ق-و-م"
        },
        "trans_sahih":   "Allah - there is no deity except Him, the Ever-Living, the Sustainer of existence.",
        "trans_haleem":  "Allah: there is no god but Him, the Ever Living, the Ever Watchful.",
        "trans_khattab": "Allah! There is no god worthy of worship except Him, the Ever-Living, All-Sustaining.",
        "trans_soliman": "Allah, there is no deity but He, the Ever-Living, the Self-Subsisting."
    },
    {
        "ayah_key": "2:256",
        "surah_name": "Al-Baqarah",
        "arabic": "لَا إِكْرَاهَ فِي الدِّينِ قَد تَّبَيَّنَ الرُّشْدُ مِنَ الْغَيِّ",
        "roots": {
            "إِكْرَاهَ": "ك-ر-ه",
            "الدِّينِ":  "د-ي-ن",
            "الرُّشْدُ": "ر-ش-د",
            "الْغَيِّ":  "غ-و-ي"
        },
        "trans_sahih":   "There shall be no compulsion in religion. The right course has become clear from the wrong.",
        "trans_haleem":  "There is no compulsion in religion: true guidance has become distinct from error.",
        "trans_khattab": "There is no compulsion in religion, for the truth stands out clearly from falsehood.",
        "trans_soliman": "There is no coercion in religion. Righteousness has been made distinct from misguidance."
    },

    # ── Surah Al-Imran (3) ───────────────────────────────────────────────────
    {
        "ayah_key": "3:185",
        "surah_name": "Al-Imran",
        "arabic": "كُلُّ نَفْسٍ ذَائِقَةُ الْمَوْتِ",
        "roots": {
            "نَفْسٍ":    "ن-ف-س",
            "ذَائِقَةُ": "ذ-و-ق",
            "الْمَوْتِ": "م-و-ت"
        },
        "trans_sahih":   "Every soul will taste death.",
        "trans_haleem":  "Every soul will taste death.",
        "trans_khattab": "Every soul will taste death.",
        "trans_soliman": "Each soul shall have the experience of death."
    },

    # ── Surah Ar-Rahman (55) ─────────────────────────────────────────────────
    {
        "ayah_key": "55:1",
        "surah_name": "Ar-Rahman",
        "arabic": "الرَّحْمَٰنُ",
        "roots": {
            "الرَّحْمَٰنُ": "ر-ح-م"
        },
        "trans_sahih":   "The Most Merciful.",
        "trans_haleem":  "The Lord of Mercy.",
        "trans_khattab": "The Most Compassionate Allah.",
        "trans_soliman": "The Almighty Merciful."
    },
    {
        "ayah_key": "55:2",
        "surah_name": "Ar-Rahman",
        "arabic": "عَلَّمَ الْقُرْآنَ",
        "roots": {
            "عَلَّمَ":    "ع-ل-م",
            "الْقُرْآنَ": "ق-ر-أ"
        },
        "trans_sahih":   "Taught the Quran.",
        "trans_haleem":  "He taught the Quran.",
        "trans_khattab": "taught the Quran,",
        "trans_soliman": "He taught the Quran."
    },

    # ── Surah Al-Ikhlas (112) ────────────────────────────────────────────────
    {
        "ayah_key": "112:1",
        "surah_name": "Al-Ikhlas",
        "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ",
        "roots": {
            "قُلْ":    "ق-و-ل",
            "اللَّهُ": "أ-ل-ه",
            "أَحَدٌ":  "أ-ح-د"
        },
        "trans_sahih":   "Say, He is Allah, the One.",
        "trans_haleem":  "Say, He is Allah the One.",
        "trans_khattab": "Say, He is Allah—One.",
        "trans_soliman": "Proclaim: He is Allah, Unique."
    },
    {
        "ayah_key": "112:2",
        "surah_name": "Al-Ikhlas",
        "arabic": "اللَّهُ الصَّمَدُ",
        "roots": {
            "اللَّهُ":    "أ-ل-ه",
            "الصَّمَدُ": "ص-م-د"
        },
        "trans_sahih":   "Allah, the Eternal Refuge.",
        "trans_haleem":  "Allah the Eternal, Besought by all.",
        "trans_khattab": "Allah—the Sustainer needed by all.",
        "trans_soliman": "Allah, the Eternally Self-Sufficient."
    },
]
