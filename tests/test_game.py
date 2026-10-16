"""Unit tests for Word Matching Game scoring."""

import unittest

from game import score_answers


class TestScoreAnswers(unittest.TestCase):
    def setUp(self):
        self.words = [
            {"id": "one", "word": "One", "definition": "The first number."},
            {"id": "two", "word": "Two", "definition": "The number after one."},
        ]

    def test_all_correct_answers_get_full_score(self):
        score, results = score_answers(self.words, {"one": "one", "two": "two"})

        self.assertEqual(score, 2)
        self.assertTrue(all(result["is_correct"] for result in results))

    def test_incorrect_answer_does_not_get_a_point(self):
        score, results = score_answers(self.words, {"one": "two", "two": "two"})

        self.assertEqual(score, 1)
        self.assertFalse(results[0]["is_correct"])
        self.assertTrue(results[1]["is_correct"])

    def test_missing_answer_is_incorrect(self):
        score, results = score_answers(self.words, {"one": "one"})

        self.assertEqual(score, 1)
        self.assertFalse(results[1]["is_correct"])

    def test_unknown_definition_id_is_incorrect(self):
        score, results = score_answers(
            self.words,
            {"one": "not-a-real-definition", "two": "two"},
        )

        self.assertEqual(score, 1)
        self.assertFalse(results[0]["is_correct"])
        self.assertTrue(results[1]["is_correct"])

    def test_empty_answers_get_zero_score(self):
        score, results = score_answers(self.words, {})

        self.assertEqual(score, 0)
        self.assertEqual(len(results), len(self.words))
        self.assertTrue(all(not result["is_correct"] for result in results))


if __name__ == "__main__":
    unittest.main()
