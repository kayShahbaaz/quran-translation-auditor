#!/usr/bin/env python3
"""
scripts/seed_fatiha_reasoning.py
─────────────────────────────────
Seeds the `reasoning` column for Al-Fatiha 1:1–1:7 from the
al-fatiha-draft.md content.

Run from project root:
    python scripts/seed_fatiha_reasoning.py
"""
import sqlite3, sys
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "auditor.db"

# ── Reasoning text for each ayah ────────────────────────────────────────────
# Sourced from data/learnquran/al-fatiha-draft.md
# Plain prose — no markdown. Template will render as-is.

REASONING = {
    "1:1": (
        "الْحَمْدُ carries the definite article (ال), making it 'the praise' — "
        "a complete, all-encompassing praise rather than praise in a generic sense. "
        "لِلَّهِ combines the prefix ل (denoting 'for' or 'belonging to') with الله, "
        "marking the praise as specifically due to Allah. "
        "رَبِّ from ر-ب-ب carries the sense of one who sustains and nurtures — "
        "broader than the English 'lord' alone suggests. "
        "الْعَالَمِينَ is plural (ينَ ending) — 'worlds' in the plural is the most "
        "root-faithful rendering; a singular 'world' or an abstract term like 'creation' "
        "departs from this plurality."
    ),
    "1:2": (
        "Both words share the root ر-ح-م but take different morphological patterns. "
        "الرَّحْمَٰنِ (Ar-Rahman) follows the فَعْلَان pattern, which in Arabic intensifier "
        "morphology denotes an attribute that is all-encompassing and inherent — mercy as "
        "a defining, permanent quality. الرَّحِيمِ (Ar-Rahim) follows the فَعِيل pattern, "
        "which denotes an attribute that is recurrently active — mercy expressed continually "
        "in action. Since English has no equivalent morphological distinction, most translators "
        "render both with 'merciful' variants, differing mainly in intensifier word choice. "
        "A literal rendering preserves the shared root while gesturing at the two patterns."
    ),
    "1:3": (
        "مَالِكِ from م-ل-ك most directly denotes 'owner' or 'possessor' — one who holds "
        "something as property. This is distinct from the related root used for 'king' in some "
        "forms, though both relate to dominion. 'Owner' is the most root-faithful rendering, "
        "preserving the sense of possession over 'Sovereign' (which leans toward the kingship "
        "sense) or 'Master' (which is broader still). "
        "الدِّينِ has a wide semantic range: recompense, judgment, religion, and debt are all "
        "attested meanings of د-ي-ن. 'Recompense' carries the additional sense of "
        "repayment/requital present in the root's 'debt' meaning, making it slightly more "
        "semantically complete than 'Judgment' alone."
    ),
    "1:4": (
        "The grammatical structure here is significant: إِيَّاكَ ('You' — the separate object "
        "pronoun) is placed before the verb نَعْبُدُ ('we worship'), which in Arabic syntax "
        "creates emphasis — 'You [and only You] we worship.' This fronting is a deliberate "
        "rhetorical structure (taqdim) that most translations render with 'It is You we worship' "
        "or preserve through word order. "
        "نَسْتَعِينُ is the Form X (استفعال) verb from ع-و-ن, meaning 'we seek help/assistance' "
        "— the است prefix specifically denotes seeking or requesting, so 'we seek help' is more "
        "root-faithful than a plain 'we ask for help', which loses the reflexive-seeking nuance."
    ),
    "1:5": (
        "اهْدِنَا is an imperative verb from ه-د-ي with the attached object pronoun نَا ('us') "
        "— 'guide us.' الصِّرَاطَ from ص-ر-ط already inherently means 'path/way' — a clear, "
        "traversable road. الْمُسْتَقِيمَ is the Form X active participle from ق-و-م ('to stand, "
        "be upright'), meaning 'the one that stands straight/upright.' Combined, "
        "الصِّرَاطَ الْمُسْتَقِيمَ is literally 'the path, the straight one' — English naturally "
        "renders this as 'the straight path.'"
    ),
    "1:6": (
        "This Ayah continues directly from 1:5, in apposition — صِرَاطَ here restates 'the path "
        "of' without the definite article, as it is in a possessive/genitive construction (إضافة). "
        "الَّذِينَ is the plural relative pronoun 'those who.' "
        "أَنْعَمْتَ is the Form IV verb from ن-ع-م, meaning 'You bestowed favor/blessing' — "
        "the أَ prefix is causative, 'to cause [someone] to have نِعْمَة (blessing).' "
        "The full phrase is literally 'the path of those whom You have favoured.'"
    ),
    "1:7": (
        "This Ayah completes the relative clause begun in 1:6, continuing the description of "
        "'the path.' غَيْرِ from غ-ي-ر means 'not/other than/besides' — functioning as a "
        "negation within the genitive construction. "
        "الْمَغْضُوبِ عَلَيْهِمْ is a passive participle (مَفْعُول) from غ-ض-ب — 'those upon "
        "whom anger has fallen' — the passive construction describes those who have incurred "
        "wrath without specifying the agent, which most translations preserve with "
        "'those who have incurred [Your] wrath.' "
        "الضَّالِّينَ is the active participle plural from ض-ل-ل — 'those who are astray.' "
        "The وَلَا ('and not') sets up the second category in parallel with the first."
    ),
}


def main():
    if not DB_PATH.exists():
        print(f"[ERROR] DB not found: {DB_PATH}")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur  = conn.cursor()

    # Verify column exists
    cols = [r[1] for r in cur.execute("PRAGMA table_info(ayat)").fetchall()]
    if "reasoning" not in cols:
        print("[ERROR] `reasoning` column not found — run migrate_add_reasoning.py first.")
        conn.close()
        sys.exit(1)

    print(f"\nSeeding reasoning for {len(REASONING)} Al-Fatiha ayat...\n")
    updated = 0
    for key, text in REASONING.items():
        cur.execute("UPDATE ayat SET reasoning=? WHERE ayah_key=?", (text, key))
        if cur.rowcount:
            print(f"  ✓ {key} ({len(text)} chars)")
            updated += 1
        else:
            print(f"  ✗ {key} — row not found")

    conn.commit()
    conn.close()
    print(f"\nDone. {updated}/{len(REASONING)} rows seeded.")

if __name__ == "__main__":
    main()