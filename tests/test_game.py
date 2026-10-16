"""Unit tests for Word Matching Game logic."""

import unittest

from game import create_round, score_answers
from questions import WORDS


class TestCreateRound(unittest.TestCase):
    def test_round_contains_requested_number_of_words(self):
        round_words, definitions = create_round(WORDS, round_size=5)

        self.assertEqual(len(round_words), 5)
        self.assertEqual(len(definitions), 5)

    def test_round_has_no_duplicate_words(self):
        round_words, definitions = create_round(WORDS, round_size=10)

        word_ids = [word["id"] for word in round_words]
        definition_ids = [definition["id"] for definition in definitions]
        self.assertEqual(len(word_ids), len(set(word_ids)))
        self.assertEqual(len(definition_ids), len(set(definition_ids)))

    def test_vocabulary_pool_has_unique_ids(self):
        word_ids = [word["id"] for word in WORDS]

        self.assertEqual(len(word_ids), len(set(word_ids)))


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
