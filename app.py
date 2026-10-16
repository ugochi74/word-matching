"""Flask web application for the Word Matching Game."""

import os

from flask import Flask, redirect, render_template, request, session, url_for

from game import create_round, score_answers
from questions import WORDS

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY", "local-development-key-change-before-deployment"
)

DIFFICULTIES = {
    "easy": {"label": "Easy", "round_size": 5, "seconds": 60},
    "normal": {"label": "Normal", "round_size": 8, "seconds": 75},
    "challenge": {"label": "Challenge", "round_size": 10, "seconds": 90},
}


@app.route("/")
def home():
    """Show the game welcome page."""
    return render_template("index.html", word_count=len(WORDS))


@app.route("/game", methods=["GET", "POST"])
def game():
    """Start a round or check submitted matches."""
    if request.method == "POST":
        if not session.get("game_active") or session.get("game_completed"):
            return redirect(url_for("home"))

        round_words = session.get("round_words", [])
        words_by_id = {word["id"]: word for word in WORDS}
        selected_words = [
            words_by_id[word_id]
            for word_id in round_words
            if word_id in words_by_id
        ]
        answers = {
            word["id"]: request.form.get(word["id"], "")
            for word in selected_words
        }
        score, results = score_answers(selected_words, answers)

        session["game_completed"] = True
        session["game_active"] = False
        session["score"] = score
        session["results"] = results
        return redirect(url_for("results"))

    difficulty_name = request.args.get(
        "difficulty", session.get("difficulty", "normal")
    )
    if difficulty_name not in DIFFICULTIES:
        difficulty_name = "normal"

    difficulty = DIFFICULTIES[difficulty_name]
    round_size = difficulty["round_size"]
    seen_word_ids = set(session.get("seen_word_ids", []))
    unseen_words = [word for word in WORDS if word["id"] not in seen_word_ids]

    # Start a fresh cycle when there are not enough unseen words for a full round.
    if len(unseen_words) < round_size:
        unseen_words = list(WORDS)
        seen_word_ids = set()

    round_words, definitions = create_round(unseen_words, round_size)
    current_ids = [word["id"] for word in round_words]

    session["seen_word_ids"] = list(seen_word_ids.union(current_ids))
    session["round_words"] = current_ids
    session["difficulty"] = difficulty_name
    session["round_seconds"] = difficulty["seconds"]
    session["game_active"] = True
    session["game_completed"] = False
    session.pop("results", None)
    session.pop("score", None)

    return render_template(
        "game.html",
        words=round_words,
        definitions=definitions,
        difficulty=difficulty,
        difficulty_name=difficulty_name,
    )


@app.route("/results")
def results():
    """Show the score after a completed round."""
    if not session.get("game_completed"):
        return redirect(url_for("home"))

    return render_template(
        "results.html",
        score=session.get("score", 0),
        total=len(session.get("results", [])),
        results=session.get("results", []),
        difficulty_name=session.get("difficulty", "normal"),
    )


if __name__ == "__main__":
    # Enable the debugger only when explicitly requested for local development.
    debug_mode = os.environ.get("FLASK_DEBUG") == "1"
    app.run(debug=debug_mode)
