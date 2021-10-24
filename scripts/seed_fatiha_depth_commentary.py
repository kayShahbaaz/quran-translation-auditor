#!/usr/bin/env python3
"""
scripts/seed_fatiha_depth_commentary.py
────────────────────────────────────────
Adds a `depth_commentary` TEXT column to the ayat table and seeds
prose Semantic Depth comparison text for Al-Fatiha 1:1–1:7.

This replaces the bar chart with human-readable per-translator commentary
on how each translation handles the root semantics of the ayah.

Run from project root:
    python scripts/seed_fatiha_depth_commentary.py
"""
import sqlite3, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

DEPTH_COMMENTARY = {
    "1:1": (
        "Sahih & Haleem both use 'worlds' (plural) — fully root-faithful to الْعَالَمِينَ. "
        "Khattab writes 'all worlds' — retains the plural and adds emphasis not in the root but consistent with it. "
        "Soliman uses 'realms' — a valid synonym but shifts away from the cosmological 'worlds' sense of ع-ل-م. "
        "Ala Hazrat uses 'Creation' — theologically rich but loses the plural structure of الْعَالَمِينَ. "
        "All five capture ح-م-د (praise) and أ-ل-ه (Allah) faithfully."
    ),
    "1:2": (
        "All translations score full Semantic Depth because the root ر-ح-م is unambiguous and every translator "
        "renders it with a mercy/compassion word. "
        "The real distinction is morphological: الرَّحْمَٰنِ (Rahman, فَعْلَان pattern) denotes inherent, "
        "all-encompassing mercy; الرَّحِيمِ (Rahim, فَعِيل pattern) denotes recurrent mercy in action. "
        "Khattab's 'Compassionate / Merciful' gestures at this distinction most directly. "
        "Sahih's 'Entirely / Especially' attempts the same with English adverbs. "
        "Haleem's 'Lord of Mercy / Giver of Mercy' shifts toward functional description rather than attribute naming."
    ),
    "1:3": (
        "م-ل-ك (ownership/dominion): Sahih uses 'Sovereign' — leans toward the kingship sense. "
        "Haleem, Khattab, and Soliman all use 'Master' — slightly broader but semantically close. "
        "Ala Hazrat and LearnQuran use 'Owner' — the most root-literal choice, preserving the possessive sense of مَالِكِ. "
        "For الدِّينِ (د-ي-ن): 'Recompense' (Sahih, Soliman, Ala Hazrat, LearnQuran) captures the debt/requital meaning. "
        "'Judgement' (Haleem, Khattab) emphasises the legal-verdict reading. Both are root-faithful."
    ),
    "1:4": (
        "ع-ب-د (worship/devotion): all translators render نَعْبُدُ with 'worship' or 'serve' — full root coverage. "
        "ع-و-ن (help/aid): Sahih and Haleem use 'ask for help' — accurate but loses the Form X seeking nuance. "
        "Soliman's 'call for help' is similar. Khattab's 'ask for help' is equivalent. "
        "LearnQuran's 'ask for help' matches, while Ala Hazrat adds 'seek' explicitly — closest to the Form X استفعال meaning of نَسْتَعِينُ. "
        "The emphatic fronting of إِيَّاكَ ('You alone') is handled differently: most add 'It is You' or bracket '[alone]'; "
        "the Arabic structure makes this emphasis grammatically, not lexically."
    ),
    "1:5": (
        "ه-د-ي (guidance): all translations use 'guide' — full root match. "
        "ص-ر-ط (path/way): all use 'path' or 'way' — full root match. "
        "ق-و-م (upright/straight): الْمُسْتَقِيمَ is rendered 'straight' by all — correct for the Form X participle meaning. "
        "Semantic Depth is 0.67 across the board because the root ق-و-م's primary meanings (stand, establish, uphold) "
        "don't appear — only the derived adjectival sense 'straight' does. This is expected and linguistically correct; "
        "the score reflects that one root's core field isn't directly represented by a single English word."
    ),
    "1:6": (
        "ص-ر-ط (path): all translations use 'path' — full match. "
        "ن-ع-م (blessing/favor): Sahih uses 'bestowed favour' — captures the Form IV causative well. "
        "Haleem, Khattab, and Soliman use 'blessed' — concise and root-faithful. "
        "Ala Hazrat uses 'favoured' — equivalent. "
        "The 0.67 Semantic Depth reflects that عَلَيْهِمْ (ع-ل-و root: upon/above) contributes a third root "
        "whose core field ('high, exalted, above') isn't present in any translation — correctly so, since "
        "عَلَيْهِمْ functions as a preposition here, not as a semantic term."
    ),
    "1:7": (
        "غ-ض-ب (anger/wrath): all translations render الْمَغْضُوبِ with 'anger', 'wrath', or 'displeased' — full root match. "
        "ض-ل-ل (astray/misguidance): all translations use 'astray' or 'gone astray' — full root match. "
        "The passive construction الْمَغْضُوبِ عَلَيْهِمْ ('those upon whom anger has fallen') is handled differently: "
        "Sahih and Ala Hazrat preserve the passive with 'earned anger'; Haleem uses active voice ('incur no anger'); "
        "Soliman's 'incurred wrath' is the most morphologically faithful. "
        "All achieve full Semantic Depth because both roots are clearly represented."
    ),
}


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    cur  = conn.cursor()

    # Add column if missing
    cols = [r[1] for r in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "depth_commentary" not in cols:
        cur.execute("ALTER TABLE ayat ADD COLUMN depth_commentary TEXT")
        print("[OK] Added `depth_commentary` column.")
    else:
        print("[OK] `depth_commentary` column already exists.")

    print(f"\nSeeding depth commentary for {len(DEPTH_COMMENTARY)} ayat...\n")
    updated = 0
    for key, text in DEPTH_COMMENTARY.items():
        cur.execute(
            "UPDATE ayat SET depth_commentary=? WHERE ayah_key=?",
            (text, key)
        )
        if cur.rowcount:
            print(f"  ✓ {key}")
            updated += 1
        else:
            print(f"  ✗ {key} — row not found")

    conn.commit()
    conn.close()
    print(f"\nDone. {updated}/{len(DEPTH_COMMENTARY)} rows seeded.")


if __name__ == "__main__":
    main()