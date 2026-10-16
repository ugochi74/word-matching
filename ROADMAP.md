# Implementation Roadmap
## Word Matching Game

**Status:** First playable version implemented; gameplay improvements added directly on `main`.

## Completed

- [x] Flask home, game, and results pages.
- [x] Vocabulary data separated into `questions.py`.
- [x] Server-side answer checking and scoring.
- [x] Shuffled words and definitions.
- [x] A larger vocabulary pool with unique word IDs.
- [x] Random round selection with no repeated words until the current pool cycle is exhausted.
- [x] Easy, Normal, and Challenge difficulty levels.
- [x] Countdown timer with automatic submission when time expires.
- [x] Progress counter, results review, and replay.
- [x] Unit tests for scoring, round selection, difficulty, and Flask routes.

## Next improvements

- [ ] Run the expanded automated test suite locally and fix any failures.
- [ ] Test timer behaviour in desktop and mobile browsers.
- [ ] Add categories such as science, everyday words, and technology.
- [ ] Consider a best-score or streak tracker.
- [ ] Configure production secret key and deploy the app.

## Difficulty settings

| Level | Words per round | Time limit |
|---|---:|---:|
| Easy | 5 | 60 seconds |
| Normal | 8 | 75 seconds |
| Challenge | 10 | 90 seconds |

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
│       └── game.js
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
