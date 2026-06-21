#!/usr/bin/env python3
"""
scripts/trim_lexicon.py
────────────────────────
Removes the auto-generated entries from root_lexicon.py,
keeping only the original 345 hand-curated entries.

Run from project root:
    python scripts/trim_lexicon.py
"""
from pathlib import Path

LEX_PATH = Path(__file__).parent.parent / "src" / "root_lexicon.py"
MARKER   = "# ── Auto-generated entries (expand_lexicon.py)"

with open(LEX_PATH, "r", encoding="utf-8") as f:
    content = f.read()

if MARKER not in content:
    print("[OK] No auto-generated section found — lexicon already clean.")
else:
    clean = content[:content.index(MARKER)].rstrip() + "\n"
    with open(LEX_PATH, "w", encoding="utf-8") as f:
        f.write(clean)

    # Verify
    import sys, importlib
    sys.path.insert(0, str(LEX_PATH.parent))
    import root_lexicon
    importlib.reload(root_lexicon)
    count = len(root_lexicon.ROOT_LEXICON)
    print(f"[OK] Lexicon trimmed to {count} hand-curated entries.")

if __name__ == "__main__":
    pass