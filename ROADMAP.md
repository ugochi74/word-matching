# Implementation Roadmap
## Word Matching Game

**Status:** Planning  
**Approach:** Build a small working version first, test each step, then improve the experience.

## Phase 1 — Project setup

**Tasks**
- [ ] Clone the repository and inspect the existing files.
- [ ] Create and activate a Python virtual environment.
- [ ] Add `requirements.txt` with Flask.
- [ ] Add a minimal Flask application in `app.py`.
- [ ] Confirm the home route responds successfully.
- [ ] Add a `.gitignore` for `.venv/`, `__pycache__/`, and local environment files.

**Done when:** Flask runs locally and the home page opens in a browser.

## Phase 2 — Build the matching logic

**Tasks**
- [ ] Create `questions.py` with a small, curated set of word-definition pairs.
- [ ] Create `game.py` for starting a round, checking answers, and calculating progress.
- [ ] Keep game rules independent of Flask routes.
- [ ] Handle invalid and repeated answers.
- [ ] Add unit tests for correct answers, incorrect answers, scoring, round completion, and resetting.

**Done when:** The core game can be tested from Python without opening a browser.

## Phase 3 — Create the website pages

**Tasks**
- [ ] Create the home page with the game title and instructions.
- [ ] Create the game page with words, definitions, score, and progress.
- [ ] Add a results state with a replay action.
- [ ] Add CSS for a clean, friendly, responsive interface.
- [ ] Use JavaScript only where it improves the matching interaction.
- [ ] Add accessible labels, focus states, and clear feedback.

**Done when:** A player can understand the rules and complete a round in the browser.

## Phase 4 — Connect Flask and game state

**Tasks**
- [ ] Add routes to show the home page, start a round, submit a match, and restart.
- [ ] Store per-player round state in a Flask session or another simple server-controlled approach.
- [ ] Calculate score on the server rather than trusting browser-submitted totals.
- [ ] Validate missing, unknown, and repeated submissions.
- [ ] Show useful error or feedback messages.

**Done when:** The complete game journey works from start to finish and invalid actions do not award points.

## Phase 5 — Testing and quality checks

**Tasks**
- [ ] Test core logic with `unittest`.
- [ ] Test the home page and key game routes using Flask's test client.
- [ ] Test correct, incorrect, invalid, and repeated answers.
- [ ] Manually check the layout at desktop and mobile widths.
- [ ] Verify the app can be installed and started using the README instructions.
- [ ] Fix bugs before adding extra features.

**Done when:** Automated tests pass and the main player journey works reliably.

## Phase 6 — Documentation and first release

**Tasks**
- [ ] Update README with the final project structure, installation, run, and test commands.
- [ ] Confirm PRD acceptance criteria.
- [ ] Add screenshots once the interface exists.
- [ ] Review changes with `git diff`.
- [ ] Commit related changes with clear messages.
- [ ] Push the feature branch and open a pull request if using a branch-based workflow.

**Done when:** A new developer can clone the repository, run the game, and understand how it works.

## Phase 7 — Optional improvements

Only start these after the MVP is stable:
- [ ] Easy, medium, and hard difficulty levels.
- [ ] Optional countdown timer.
- [ ] Sound and motion preferences.
- [ ] More vocabulary categories.
- [ ] Local high scores or a leaderboard.
- [ ] Keyboard-friendly matching mode.

## Suggested folder structure

```text
word-matching/
├── app.py
├── game.py
├── questions.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── index.html
│   ├── game.html
│   └── results.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── game.js
├── tests/
│   ├── test_game.py
│   └── test_app.py
├── PRD.md
├── ROADMAP.md
└── README.md
```

This is a proposed structure. Files should be added when their phase begins, rather than creating empty files all at once.

## Beginner-friendly working rules

1. Build one phase at a time.
2. Run the app or tests after each meaningful change.
3. Keep functions small and use clear variable names.
4. Understand the code before adding the next feature.
5. Commit a working step before moving to the next phase.
