#!/usr/bin/env python3
"""
scripts/seed_fatiha_intro_summary.py
──────────────────────────────────────
Adds surah_intro and surah_summary columns to the ayat table and seeds
Al-Fatiha's introduction and summary.

The intro is stored on the FIRST ayah of the surah (1:1).
The summary is stored on the LAST ayah of the surah (1:7).
The template checks for these and renders them as panels above/below the card set.

Run from project root:
    python scripts/seed_fatiha_intro_summary.py
"""
import sqlite3, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

FATIHA_INTRO = (
    "Al-Fatiha (الفاتحة) — The Opening — is the first Surah of the Qur'ān and the most "
    "recited text in Prayer, repeated in each rak'ah of the five daily prayers. "
    "Its seven Ayaat encompass the entire Qur'ān in miniature: opening with praise of Allah, "
    "affirming His attributes of mercy and sovereignty, establishing the exclusive "
    "relationship of worship between the believer and the Divine, and concluding with a "
    "supplication for guidance on the path of those whom Allah has blessed. "
    "The Surah was revealed in Makkah and is known by many names — among them Umm al-Qur'ān "
    "(Mother of the Qur'ān), Umm al-Kitab (Mother of the Book), As-Sab' al-Mathani "
    "(The Seven Oft-Repeated Ayaat), and Al-Kafiya (The Sufficient). "
    "Linguistically, it is among the most densely rooted texts in Arabic — every word "
    "carries a precise root meaning that the five translations audited here render with "
    "varying degrees of fidelity."
)

FATIHA_SUMMARY = (
    "Across the seven ayat of Al-Fatiha, the five translations show consistently high "
    "Semantic Depth scores, reflecting that the surah's roots — ح-م-د (praise), أ-ل-ه (deity), "
    "ر-ب-ب (lordship/nurturing), ع-ل-م (worlds/knowledge), ر-ح-م (mercy), م-ل-ك (ownership), "
    "د-ي-ن (recompense), ه-د-ي (guidance), ص-ر-ط (path), and ق-و-م (uprightness) — are "
    "all semantically rich and well-represented in the translators' vocabulary choices. "
    "Key translation divergences: الْعَالَمِينَ is rendered as 'worlds' (Sahih, Khattab, Soliman), "
    "'Worlds' (Haleem), and 'Creation' (Ala Hazrat) — the plural structure is lost in the last. "
    "مَالِكِ is rendered as 'Sovereign' (Sahih), 'Master' (Haleem, Khattab), 'Master' (Soliman), "
    "and 'Owner' (Ala Hazrat) — 'Owner' is the most root-faithful. "
    "الصِّرَاطَ الْمُسْتَقِيمَ is consistently rendered as 'the straight path' or 'the straight way' "
    "across all five — a rare point of full consensus. "
    "Literal Accuracy scores are highest for ayat 1:3–1:5 and lowest for 1:7, where the "
    "passive construction الْمَغْضُوبِ عَلَيْهِمْ presents the greatest translation challenge."
)


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    cols = [r[1] for r in cur.execute("PRAGMA table_info(ayat)").fetchall()]

    # Add columns if missing
    for col in ["surah_intro", "surah_summary"]:
        if col not in cols:
            cur.execute(f"ALTER TABLE ayat ADD COLUMN {col} TEXT")
            print(f"[OK] Added column: {col}")
        else:
            print(f"[OK] Column already exists: {col}")

    # Seed intro on 1:1
    cur.execute("UPDATE ayat SET surah_intro=? WHERE ayah_key='1:1'", (FATIHA_INTRO,))
    print(f"[OK] Intro seeded on 1:1 ({len(FATIHA_INTRO)} chars)")

    # Seed summary on 1:7
    cur.execute("UPDATE ayat SET surah_summary=? WHERE ayah_key='1:7'", (FATIHA_SUMMARY,))
    print(f"[OK] Summary seeded on 1:7 ({len(FATIHA_SUMMARY)} chars)")

    conn.commit()
    conn.close()
    print("\nDone.")


if __name__ == "__main__":
    main()