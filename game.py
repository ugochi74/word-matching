"""Simple game logic, kept separate from the Flask website."""

import random


def create_round(words):
    """Return words and shuffled definitions for one game round."""
    round_words = list(words)
    definitions = [
        {"id": item["id"], "definition": item["definition"]}
        for item in words
    ]
    random.shuffle(round_words)
    random.shuffle(definitions)
    return round_words, definitions


def score_answers(words, answers):
    """Count correct word-to-definition matches from submitted form data."""
    correct_answers = {item["id"]: item["id"] for item in words}
    results = []

    for item in words:
        selected_definition = answers.get(item["id"], "")
        is_correct = selected_definition == correct_answers[item["id"]]
        results.append({
            "word": item["word"],
            "definition": item["definition"],
            "is_correct": is_correct,
        })

    score = sum(1 for result in results if result["is_correct"])
    return score, results
