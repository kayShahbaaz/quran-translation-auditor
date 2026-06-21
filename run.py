# run.py
import sys, os, json, sqlite3, re, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from flask import Flask, render_template, request
from database import init_db, seed_db
from fidelity_engine import score_all_translators, TRANSLATOR_KEYS, TRANSLATOR_LABELS, SCORE_LABELS

app       = Flask(__name__, template_folder="app/templates", static_folder="app/static")
PAGE_SIZE = 50
DB_PATH   = os.path.join(os.path.dirname(__file__), "data", "auditor.db")

# Surahs with full Root Breakdown + Reasoning + Semantic Depth support
# Others will show only Literal Accuracy scores (no expand panel)
FULL_ANALYSIS_SURAHS = {1}  # Only Al-Fatiha for now; 112-114 planned for next version

# ── Arabic surah names ────────────────────────────────────────────────────────
SURAH_ARABIC = {
    "Al-Fatiha":"الفاتحة","Al-Baqarah":"البقرة","Al-Imran":"آل عمران",
    "An-Nisa":"النساء","Al-Maidah":"المائدة","Al-Anam":"الأنعام",
    "Al-Araf":"الأعراف","Al-Anfal":"الأنفال","At-Tawbah":"التوبة",
    "Yunus":"يونس","Hud":"هود","Yusuf":"يوسف","Ar-Rad":"الرعد",
    "Ibrahim":"إبراهيم","Al-Hijr":"الحجر","An-Nahl":"النحل",
    "Al-Isra":"الإسراء","Al-Kahf":"الكهف","Maryam":"مريم","Ta-Ha":"طه",
    "Al-Anbiya":"الأنبياء","Al-Hajj":"الحج","Al-Muminun":"المؤمنون",
    "An-Nur":"النور","Al-Furqan":"الفرقان","Ash-Shuara":"الشعراء",
    "An-Naml":"النمل","Al-Qasas":"القصص","Al-Ankabut":"العنكبوت",
    "Ar-Rum":"الروم","Luqman":"لقمان","As-Sajdah":"السجدة",
    "Al-Ahzab":"الأحزاب","Saba":"سبأ","Fatir":"فاطر","Ya-Sin":"يس",
    "As-Saffat":"الصافات","Sad":"ص","Az-Zumar":"الزمر","Ghafir":"غافر",
    "Fussilat":"فصلت","Ash-Shura":"الشورى","Az-Zukhruf":"الزخرف",
    "Ad-Dukhan":"الدخان","Al-Jathiyah":"الجاثية","Al-Ahqaf":"الأحقاف",
    "Muhammad":"محمد","Al-Fath":"الفتح","Al-Hujurat":"الحجرات","Qaf":"ق",
    "Adh-Dhariyat":"الذاريات","At-Tur":"الطور","An-Najm":"النجم",
    "Al-Qamar":"القمر","Ar-Rahman":"الرحمن","Al-Waqiah":"الواقعة",
    "Al-Hadid":"الحديد","Al-Mujadila":"المجادلة","Al-Hashr":"الحشر",
    "Al-Mumtahanah":"الممتحنة","As-Saf":"الصف","Al-Jumuah":"الجمعة",
    "Al-Munafiqun":"المنافقون","At-Taghabun":"التغابن","At-Talaq":"الطلاق",
    "At-Tahrim":"التحريم","Al-Mulk":"الملك","Al-Qalam":"القلم",
    "Al-Haqqah":"الحاقة","Al-Maarij":"المعارج","Nuh":"نوح",
    "Al-Jinn":"الجن","Al-Muzzammil":"المزمل","Al-Muddaththir":"المدثر",
    "Al-Qiyamah":"القيامة","Al-Insan":"الإنسان","Al-Mursalat":"المرسلات",
    "An-Naba":"النبأ","An-Naziat":"النازعات","Abasa":"عبس",
    "At-Takwir":"التكوير","Al-Infitar":"الانفطار","Al-Mutaffifin":"المطففين",
    "Al-Inshiqaq":"الانشقاق","Al-Buruj":"البروج","At-Tariq":"الطارق",
    "Al-Ala":"الأعلى","Al-Ghashiyah":"الغاشية","Al-Fajr":"الفجر",
    "Al-Balad":"البلد","Ash-Shams":"الشمس","Al-Layl":"الليل",
    "Ad-Duha":"الضحى","Ash-Sharh":"الشرح","At-Tin":"التين",
    "Al-Alaq":"العلق","Al-Qadr":"القدر","Al-Bayyinah":"البينة",
    "Az-Zalzalah":"الزلزلة","Al-Adiyat":"العاديات","Al-Qariah":"القارعة",
    "At-Takathur":"التكاثر","Al-Asr":"العصر","Al-Humazah":"الهمزة",
    "Al-Fil":"الفيل","Quraysh":"قريش","Al-Maun":"الماعون",
    "Al-Kawthar":"الكوثر","Al-Kafirun":"الكافرون","An-Nasr":"النصر",
    "Al-Masad":"المسد","Al-Ikhlas":"الإخلاص","Al-Falaq":"الفلق","An-Nas":"الناس",
}


# ── Arabic normalisation helpers ──────────────────────────────────────────────

# Prefixes the morphology file strips from words
_AL_PREFIXES = ("ٱلْ", "ٱل", "الْ", "ال", "وَٱلْ", "وَال", "فَٱلْ", "فَال",
                "بِٱلْ", "بِال", "كَٱلْ", "كَال", "لِٱلْ", "لِل",
                "وَ", "فَ", "بِ", "لِ", "كَ")

def _strip_prefix(word: str) -> str:
    """Strip common Arabic prefixes to get the stem for matching."""
    for prefix in _AL_PREFIXES:
        if word.startswith(prefix) and len(word) > len(prefix) + 1:
            return word[len(prefix):]
    return word

def _normalise_ar(text: str) -> str:
    """Strip diacritics, normalise alef variants, and remove ال prefix for matching."""
    # Remove diacritics (harakat) and other combining marks
    text = ''.join(c for c in text if not unicodedata.category(c).startswith('M')
                   and unicodedata.category(c) not in ('Cf',))
    # Normalise alef variants → plain alef
    for ch in "أإآٱ":
        text = text.replace(ch, "ا")
    # Remove tatweel
    text = text.replace("ـ", "")
    return text


_NORM_PREFIXES = ("ال", "وال", "فال", "بال", "كال", "لل", "لال")

def _strip_ar_prefix(word: str) -> str:
    """Strip common Arabic prefixes after normalisation."""
    for prefix in _NORM_PREFIXES:
        if word.startswith(prefix) and len(word) > len(prefix) + 1:
            return word[len(prefix):]
    return word


def _match_root_to_db_word(morph_word: str, db_words: list) -> str | None:
    """
    Find the DB word that best matches a root dict key.
    Uses normalised Arabic (diacritics stripped, alef variants unified)
    with multi-level fallback matching.
    """
    morph_norm  = _normalise_ar(morph_word)
    morph_strip = _strip_ar_prefix(morph_norm)

    for db_word in db_words:
        db_norm  = _normalise_ar(db_word)
        db_strip = _strip_ar_prefix(db_norm)

        # Level 1: exact normalised match
        if db_norm == morph_norm:
            return db_word
        # Level 2: both stripped of ال prefix match
        if db_strip == morph_strip and len(morph_strip) > 2:
            return db_word
        # Level 3: root key is the stem of the DB word (prefix kept in DB)
        if morph_norm and db_strip == morph_norm and len(morph_norm) > 2:
            return db_word
        # Level 4: DB word stem matches root key stripped
        if morph_strip and db_norm == morph_strip and len(morph_strip) > 2:
            return db_word
        # Level 5: containment (root key contained in DB word after normalisation)
        if morph_strip and len(morph_strip) > 3 and morph_strip in db_norm:
            return db_word

    return None


def _to_hyphenated(root: str) -> str:
    """Convert plain Arabic root 'حمد' to hyphenated 'ح-م-د' for lexicon lookup."""
    root = root.strip()
    # Already hyphenated
    if '-' in root:
        return root
    # Insert hyphens between each character (skip diacritics)
    import unicodedata
    chars = [c for c in root if not unicodedata.category(c).startswith('M')]
    return '-'.join(chars) if len(chars) >= 2 else root


def build_root_map(db_arabic: str, roots_dict: dict) -> dict:
    """
    Map DB arabic words → roots, using fuzzy matching to bridge the
    prefix-stripping difference between the morphology file and our DB.

    roots_dict: {morph_segment_word: root}  from the roots column
    db_arabic:  full ayah text from the arabic column

    Returns {db_word: root} — only words that matched get a root.
    """
    if not roots_dict or not db_arabic:
        return {}

    # Split DB arabic into words, filtering out ayah markers (٪ ۚ ۖ ۗ ۘ ۙ ۛ ۜ ۝ etc)
    db_words = [w for w in db_arabic.split()
                if w and not all(unicodedata.category(c) in ('Po', 'Mn', 'Cf', 'So', 'No')
                                  for c in w)]

    result = {}
    for morph_word, root in roots_dict.items():
        db_word = _match_root_to_db_word(morph_word, db_words)
        if db_word and db_word not in result:
            result[db_word] = root

    return result


def get_audited_ayat(rows):
    audited   = []
    col_names = None

    for row in rows:
        key = row["ayah_key"]
        if col_names is None:
            col_names = set(row.keys())

        # Parse stored roots dict {morph_word: root}
        raw_roots = json.loads(row["roots"]) if row["roots"] else {}
        gloss     = json.loads(row["gloss"])  if row["gloss"]  else []
        db_arabic = row["arabic"] or ""

        # Re-map morphology words → DB words using fuzzy matching
        # Also convert root values to hyphenated format for lexicon/engine compatibility
        raw_mapped = build_root_map(db_arabic, raw_roots)
        roots = {word: _to_hyphenated(root) for word, root in raw_mapped.items()}

        translations = {
            "sahih":      row["trans_sahih"],
            "haleem":     row["trans_haleem"],
            "khattab":    row["trans_khattab"],
            "soliman":    row["trans_soliman"],
            "kanzuliman": row["trans_kanzuliman"],
        }

        scores = score_all_translators(translations, roots, gloss)

        # Per-translator display rows
        translator_rows = []
        for tkey in TRANSLATOR_KEYS:
            col    = f"trans_{tkey}"
            text   = row[col] if col in col_names else ""
            sdata  = scores.get(tkey) or {}
            gloss_score = sdata.get("gloss", {}).get("score") if sdata.get("gloss") else None
            root_score  = sdata.get("root",  {}).get("score") if sdata.get("root")  else None
            translator_rows.append({
                "key":         tkey,
                "label":       TRANSLATOR_LABELS[tkey],
                "text":        text,
                "gloss_score": gloss_score,
                "root_score":  root_score,
                "root_detail": sdata.get("root"),
            })

        # Root breakdown panel — deduplicated, in order of first appearance
        root_breakdown = []
        seen_roots = set()
        from root_lexicon import get_root_data
        for db_word, root in roots.items():
            if root in seen_roots:
                continue
            seen_roots.add(root)
            # Morphology file uses plain root (حمد); lexicon uses hyphenated (ح-م-د)
            hyphenated = _to_hyphenated(root)
            rdata = get_root_data(hyphenated)
            if rdata:
                root_breakdown.append({
                    "arabic_word": db_word,
                    "root":        hyphenated,
                    "latin":       rdata["latin"],
                    "category":    rdata["category"],
                    "core":        rdata["core"],
                    "extended":    rdata["extended"],
                })
            else:
                # Root not in lexicon yet — show with Arabic root as label
                root_breakdown.append({
                    "arabic_word": db_word,
                    "root":        hyphenated,
                    "latin":       hyphenated,
                    "category":    "Uncovered",
                    "core":        [],
                    "extended":    [],
                })

        surah_en  = row["surah_name"]
        surah_num = int(key.split(":")[0])
        ayah_num  = int(key.split(":")[1])

        # Only show Root Breakdown / Reasoning / Semantic Depth for supported surahs
        in_full_analysis = surah_num in FULL_ANALYSIS_SURAHS

        reasoning        = (row["reasoning"]        if "reasoning"        in col_names else "") or ""
        depth_commentary = (row["depth_commentary"] if "depth_commentary" in col_names else "") or ""
        surah_intro      = (row["surah_intro"]      if "surah_intro"      in col_names else "") or ""

        audited.append({
            "id":               row["id"],
            "ayah_key":         key,
            "surah_name":       surah_en,
            "surah_arabic":     SURAH_ARABIC.get(surah_en, ""),
            "arabic":           db_arabic,
            "translators":      translator_rows,
            "root_breakdown":   root_breakdown   if in_full_analysis else [],
            "reasoning":        reasoning        if in_full_analysis else "",
            "depth_commentary": depth_commentary if in_full_analysis else "",
            "has_roots":        bool(raw_roots) and in_full_analysis,
            "surah_intro":      surah_intro,
        })

    return audited


@app.route("/")
def index():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    total_ayat = cur.execute("SELECT COUNT(*) FROM ayat").fetchone()[0]
    surah_rows = cur.execute(
        "SELECT DISTINCT surah_name FROM ayat ORDER BY id"
    ).fetchall()
    surahs = [{"en": r[0], "ar": SURAH_ARABIC.get(r[0], "")} for r in surah_rows]

    surah_filter = request.args.get("surah", "").strip()
    page         = max(1, int(request.args.get("page", 1)))
    offset       = (page - 1) * PAGE_SIZE

    if surah_filter:
        total_filtered = cur.execute(
            "SELECT COUNT(*) FROM ayat WHERE surah_name=?", (surah_filter,)
        ).fetchone()[0]
        rows = cur.execute(
            "SELECT * FROM ayat WHERE surah_name=? ORDER BY id LIMIT ? OFFSET ?",
            (surah_filter, PAGE_SIZE, offset)
        ).fetchall()
    else:
        total_filtered = total_ayat
        rows = cur.execute(
            "SELECT * FROM ayat ORDER BY id LIMIT ? OFFSET ?",
            (PAGE_SIZE, offset)
        ).fetchall()

    conn.close()

    total_pages     = max(1, (total_filtered + PAGE_SIZE - 1) // PAGE_SIZE)
    surah_filter_ar = SURAH_ARABIC.get(surah_filter, "") if surah_filter else ""
    audited         = get_audited_ayat(rows)

    return render_template("index.html",
        ayat            = audited,
        total_ayat      = total_ayat,
        display_count   = total_filtered,
        surahs          = surahs,
        surah_filter    = surah_filter,
        surah_filter_ar = surah_filter_ar,
        page            = page,
        total_pages     = total_pages,
        page_size       = PAGE_SIZE,
        total_filtered  = total_filtered,
        score_labels    = SCORE_LABELS,
    )


@app.route("/surahs")
def surahs():
    """Surah summary page — reads from pre-computed surah_scores table."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    # Check if precomputed table exists
    has_table = cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='surah_scores'"
    ).fetchone()

    if not has_table:
        conn.close()
        return """<html><body style='font-family:sans-serif;padding:40px'>
            <h2>Surah scores not yet computed.</h2>
            <p>Run: <code>python scripts/precompute_summary.py</code></p>
            <a href='/'>← Back</a>
        </body></html>"""

    rows = cur.execute("""
        SELECT s.surah_name, s.ayah_count,
               s.avg_sahih, s.avg_haleem, s.avg_khattab,
               s.avg_soliman, s.avg_kanzuliman, s.avg_overall
        FROM surah_scores s
        JOIN (SELECT surah_name, MIN(id) as first_id FROM ayat GROUP BY surah_name) a
          ON s.surah_name = a.surah_name
        ORDER BY a.first_id
    """).fetchall()
    conn.close()

    surahs_data = []
    for i, row in enumerate(rows, 1):
        surahs_data.append({
            "num":     i,
            "en":      row["surah_name"],
            "ar":      SURAH_ARABIC.get(row["surah_name"], ""),
            "count":   row["ayah_count"],
            "overall": row["avg_overall"],
            "avgs": {
                "sahih":      row["avg_sahih"],
                "haleem":     row["avg_haleem"],
                "khattab":    row["avg_khattab"],
                "soliman":    row["avg_soliman"],
                "kanzuliman": row["avg_kanzuliman"],
            }
        })

    return render_template("surahs.html",
        surahs       = surahs_data,
        trans_keys   = TRANSLATOR_KEYS,
        trans_labels = TRANSLATOR_LABELS,
    )


if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        print("[APP] No database — running setup...")
        init_db(); seed_db()
    else:
        count = sqlite3.connect(DB_PATH).execute(
            "SELECT COUNT(*) FROM ayat"
        ).fetchone()[0]
        print(f"[APP] Database found — {count} Ayat loaded.")
    print("[APP] Launching → http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))