# Implementation Roadmap
## Word Matching Game

**Status:** Core gameplay and first engagement upgrades implemented directly on `main`.

## Completed

- [x] Flask home, game, and results pages.
- [x] Vocabulary data separated into `questions.py`.
- [x] Server-side answer checking and scoring.
- [x] Random round selection with no repeated words until the category cycle is exhausted.
- [x] Three difficulty levels and countdown timer.
- [x] Three vocabulary categories: Everyday English, Science, and Technology.
- [x] Consecutive-correct-answer streak tracking.
- [x] Personal best scores and streak records saved in browser local storage.
- [x] Results review, progress counter, and replay.
- [x] Tests for scoring, streaks, random selection, category selection, difficulty, and Flask routes.

## Next improvements

- [ ] Run the expanded automated test suite locally and fix any failures.
- [ ] Test the countdown and automatic submission on desktop and mobile browsers.
- [ ] Add more words to each category over time.
- [x] Add optional sound effects, a sound toggle, answer-selection feedback, and result animations.
- [x] Add a daily challenge with the same eight words for everyone each calendar day.
- [ ] Configure production secret key and deploy the app.

## Difficulty settings

| Level | Words per round | Time limit |
|---|---:|---:|
| Easy | 5 | 60 seconds |
| Normal | 8 | 75 seconds |
| Challenge | 10 | 90 seconds |

## Categories

- Everyday English
- Science
- Technology

## Project structure

```text
word-matching/
├── app.py
├── game.py
├── questions.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── game.html
│   └── results.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── game.js
│       └── results.js
└── tests/
    ├── test_game.py
    └── test_app.py
```

## Beginner-friendly working rules

1. Build one improvement at a time.
2. Run the app or tests after meaningful changes.
3. Keep functions small and variable names clear.
4. Understand the code before adding the next feature.
5. Commit related changes with clear messages.
