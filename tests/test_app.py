"""Tests for the Word Matching Game Flask routes."""

import unittest

from app import app
from questions import WORDS


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
        self.assertIn(b"Challenge", response.data)

    def test_home_page_shows_player_progress_dashboard(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your learning progress", response.data)
        self.assertIn(b"progress-games-played", response.data)
        self.assertIn(b"progress-recent-games", response.data)

    def test_game_page_starts_a_round(self):
        response = self.client.get("/game")

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertTrue(game_session["game_active"])
            self.assertFalse(game_session["game_completed"])
            self.assertEqual(len(game_session["round_words"]), 8)
            self.assertEqual(game_session["difficulty"], "normal")

    def test_daily_challenge_uses_eight_words_and_same_words_for_the_day(self):
        first_response = self.client.get("/daily-challenge", follow_redirects=True)

        self.assertEqual(first_response.status_code, 200)
        self.assertIn(b"DAILY CHALLENGE", first_response.data)
        with self.client.session_transaction() as game_session:
            first_round = list(game_session["round_words"])
            self.assertEqual(game_session["category"], "Daily Challenge")
            self.assertTrue(game_session["is_daily_challenge"])
            self.assertEqual(len(first_round), 8)

        second_response = self.client.get("/daily-challenge", follow_redirects=True)

        self.assertEqual(second_response.status_code, 200)
        with self.client.session_transaction() as game_session:
            second_round = list(game_session["round_words"])

        self.assertEqual(first_round, second_round)

    def test_daily_challenge_results_keep_daily_challenge_label(self):
        self.client.get("/daily-challenge", follow_redirects=True)
        with self.client.session_transaction() as game_session:
            round_words = list(game_session["round_words"])

        answers = {word_id: word_id for word_id in round_words}
        response = self.client.post("/game", data=answers, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"DAILY CHALLENGE COMPLETE", response.data)
        self.assertIn(b"Try today's challenge again", response.data)

    def test_easy_difficulty_starts_five_word_round(self):
        response = self.client.get("/game?difficulty=easy")

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertEqual(len(game_session["round_words"]), 5)
            self.assertEqual(game_session["difficulty"], "easy")

    def test_challenge_difficulty_starts_ten_word_round(self):
        response = self.client.get("/game?difficulty=challenge")

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertEqual(len(game_session["round_words"]), 10)
            self.assertEqual(game_session["difficulty"], "challenge")

    def test_next_round_uses_different_words_until_pool_cycle(self):
        self.client.get("/game")

        with self.client.session_transaction() as game_session:
            first_round = set(game_session["round_words"])

        self.client.get("/game")

        with self.client.session_transaction() as game_session:
            second_round = set(game_session["round_words"])

        self.assertEqual(len(first_round), 8)
        self.assertEqual(len(second_round), 8)
        self.assertTrue(first_round.isdisjoint(second_round))

    def test_results_page_redirects_before_game_is_completed(self):
        response = self.client.get("/results")

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.headers["Location"].endswith("/"))

    def test_results_include_round_id_for_progress_tracking(self):
        self.client.get("/game")
        with self.client.session_transaction() as game_session:
            round_words = list(game_session["round_words"])

        answers = {word_id: word_id for word_id in round_words}
        response = self.client.post("/game", data=answers, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'data-round-id=', response.data)

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

    def test_category_filter_starts_a_round_from_selected_topic(self):
        response = self.client.get("/game?category=Technology&difficulty=easy")

        self.assertEqual(response.status_code, 200)
        with self.client.session_transaction() as game_session:
            self.assertEqual(game_session["category"], "Technology")
            self.assertEqual(len(game_session["round_words"]), 5)

        self.assertIn(b"Technology", response.data)

    def test_invalid_category_falls_back_to_everyday_english(self):
        self.client.get("/game?category=MadeUpTopic")

        with self.client.session_transaction() as game_session:
            self.assertEqual(game_session["category"], "Everyday English")


if __name__ == "__main__":
    unittest.main()
