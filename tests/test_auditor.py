# tests/test_auditor.py
# ─────────────────────────────────────────────────────────────────────────────
# Unit tests for the divergence auditing engine.
# Uses Python's built-in unittest — no extra dependencies.
#
# Usage:
#   python -m pytest tests/              # with pytest
#   python tests/test_auditor.py         # standalone
# ─────────────────────────────────────────────────────────────────────────────

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from auditor import clean_text, jaccard_similarity, compute_divergence


class TestCleanText(unittest.TestCase):

    def test_lowercase_and_strip_punctuation(self):
        result = clean_text("The Most Merciful!")
        self.assertIn("merciful", result)
        self.assertNotIn("The", result)
        self.assertNotIn("!", result)

    def test_stop_words_removed(self):
        result = clean_text("He is the Lord of the worlds.")
        self.assertNotIn("he", result)
        self.assertNotIn("is", result)
        self.assertNotIn("the", result)
        self.assertNotIn("of", result)
        self.assertIn("lord", result)
        self.assertIn("worlds", result)

    def test_returns_set(self):
        result = clean_text("mercy mercy mercy")
        self.assertIsInstance(result, set)
        self.assertEqual(len(result), 1)

    def test_empty_string(self):
        result = clean_text("")
        self.assertEqual(result, set())


class TestJaccardSimilarity(unittest.TestCase):

    def test_identical_sets(self):
        s = {"lord", "mercy", "worlds"}
        self.assertEqual(jaccard_similarity(s, s), 1.0)

    def test_disjoint_sets(self):
        a = {"sovereign", "recompense"}
        b = {"master", "judgement"}
        self.assertEqual(jaccard_similarity(a, b), 0.0)

    def test_partial_overlap(self):
        a = {"lord", "worlds", "praise"}
        b = {"lord", "worlds", "belongs"}
        result = jaccard_similarity(a, b)
        # intersection=2, union=4  →  0.5
        self.assertAlmostEqual(result, 0.5, places=4)

    def test_both_empty(self):
        self.assertEqual(jaccard_similarity(set(), set()), 1.0)

    def test_one_empty(self):
        self.assertEqual(jaccard_similarity({"word"}, set()), 0.0)


class TestComputeDivergence(unittest.TestCase):

    def test_returns_required_keys(self):
        result = compute_divergence(
            "Every soul will taste death.",
            "Every soul will taste death.",
            "Every soul will taste death.",
            "Each soul shall have the experience of death."
        )
        for key in ("friction_score", "band", "band_label", "word_sets", "pairs_log"):
            self.assertIn(key, result)

    def test_identical_translations_low_score(self):
        t = "Every soul will taste death."
        result = compute_divergence(t, t, t, t)
        self.assertEqual(result["friction_score"], 0.0)
        self.assertEqual(result["band"], "low")

    def test_score_in_valid_range(self):
        result = compute_divergence(
            "All praise is due to Allah, Lord of the worlds.",
            "Praise belongs to Allah, Lord of the Worlds.",
            "All praise is for Allah—Lord of all worlds.",
            "Praised be Allah, the Lord of the universe."
        )
        self.assertGreaterEqual(result["friction_score"], 0.0)
        self.assertLessEqual(result["friction_score"], 1.0)

    def test_six_pairs_in_log(self):
        result = compute_divergence(
            "Say He is Allah the One.",
            "Say He is Allah the One.",
            "Say He is Allah One.",
            "Proclaim He is Allah Unique."
        )
        self.assertEqual(len(result["pairs_log"]), 6)

    def test_band_labels(self):
        t = "Every soul will taste death."
        result = compute_divergence(t, t, t, t)
        self.assertEqual(result["band_label"], "Tight Consensus")


if __name__ == "__main__":
    unittest.main(verbosity=2)
