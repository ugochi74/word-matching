"""Tests for the Word Matching Game Flask routes."""

import unittest

from app import app


class TestGameRoutes(unittest.TestCase):
    def setUp(self):
        app.config.update(
            TESTING=True,
            SECRET_KEY="test-secret-key",
        )
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Word", response.data)

    def test_game_page_starts_a_round(self):
        response = self.client.get("/game")

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertTrue(game_session["game_active"])
            self.assertFalse(game_session["game_completed"])
            self.assertTrue(game_session["round_words"])

    def test_results_page_redirects_before_game_is_completed(self):
        response = self.client.get("/results")

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].endswith("/"))

    def test_submitting_correct_answers_shows_results(self):
        self.client.get("/game")

        with self.client.session_transaction() as game_session:
            round_words = list(game_session["round_words"])

        answers = {word_id: word_id for word_id in round_words}
        response = self.client.post("/game", data=answers, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertTrue(game_session["game_completed"])
            self.assertFalse(game_session["game_active"])
            self.assertEqual(game_session["score"], len(round_words))

    def test_submitting_without_starting_a_game_redirects_home(self):
        response = self.client.post("/game", data={})

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].endswith("/"))

    def test_completed_game_cannot_be_submitted_twice(self):
        self.client.get("/game")

        with self.client.session_transaction() as game_session:
            round_words = list(game_session["round_words"])

        answers = {word_id: word_id for word_id in round_words}
        first_response = self.client.post("/game", data=answers)
        second_response = self.client.post("/game", data=answers)

        self.assertEqual(first_response.status_code, 302)
        self.assertEqual(second_response.status_code, 302)
        self.assertTrue(second_response.headers["Location"].endswith("/"))


if __name__ == "__main__":
    unittest.main()
