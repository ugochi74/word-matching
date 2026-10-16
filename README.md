# Word Matching Game

A beginner-friendly vocabulary game built with Python and Flask. Match words with their definitions, beat the countdown, try different difficulty levels, and learn new words as you play.

## Features

- A growing pool of 40+ vocabulary words.
- Randomly selected words in each round.
- No repeated words between rounds until the vocabulary pool cycle is exhausted.
- Three difficulty levels: Easy, Normal, and Challenge.
- Countdown timer that submits the round when time runs out.
- Shuffled word order and definition order.
- Server-side answer checking and scoring.
- Progress counter while choosing answers.
- Results review and replay at the same difficulty.
- Automated tests for scoring, round selection, difficulty settings, and important website routes.
- Responsive home, game, and results pages.
- No account or database required.

## Difficulty levels

| Level | Words per round | Time limit |
|---|---:|---:|
| Easy | 5 | 60 seconds |
| Normal | 8 | 75 seconds |
| Challenge | 10 | 90 seconds |

## Technology

- Python 3
- Flask
- HTML and Jinja templates
- CSS
- JavaScript
- Python `unittest`

## Project structure

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
└── tests/
    ├── test_game.py
    └── test_app.py
```

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/ugochi74/word-matching.git
cd word-matching
```

If you already have the project:

```bash
cd ~/word-matching
git pull origin main
```

### 2. Create and activate a virtual environment

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the website

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Stop the server with `Ctrl+C`.

### 5. Run the tests

```bash
python -m unittest discover -s tests -v
```

## How to play

1. Choose Easy, Normal, or Challenge.
2. Match each word to the correct definition before the timer reaches zero.
3. Submit early if you're ready, or let the timer submit your current answers.
4. Review your score and any missed meanings.
5. Play another round to get a fresh selection of words.

## Configuration and deployment

The app uses a development secret key by default so it can run locally. Before deploying publicly, set a strong `SECRET_KEY` environment variable and configure a production WSGI server. Do not use Flask's development server as the public production server.

## Documentation

- [Product Requirements Document](PRD.md)
- [Implementation Roadmap](ROADMAP.md)

## Project status

The core game and the first round of gameplay improvements are implemented. The expanded test suite should be run locally, and the timer should be manually checked in a browser before deployment.

## Learning goals

This project provides practice with Python functions, lists and dictionaries, random selection, server-side validation, Flask routes and sessions, HTML templates, responsive CSS, JavaScript interactions, automated testing, and Git/GitHub.

## License

A license has not been selected yet.
