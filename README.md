# Word Matching Game

A beginner-friendly vocabulary game built with Python and Flask. Match words with their definitions, beat the countdown, build answer streaks, and try to beat your personal best.

## Features

- 55 vocabulary words in three themed categories: Everyday English, Science, and Technology.
- Randomly selected words in each round, without repeats until the selected category's cycle is exhausted.
- Three difficulty levels: Easy, Normal, and Challenge.
- Countdown timer that submits the round when time runs out.
- Shuffled word order and definition order.
- Server-side answer checking and scoring.
- Consecutive-correct-answer streak tracking.
- Personal best scores and streak records saved in the current browser using local storage.
- Results review and replay with the same difficulty and topic.
- Automated tests for scoring, streaks, round selection, difficulty settings, and important website routes.
- Responsive home, game, and results pages.
- No account or database required.

## Categories

- **Everyday English:** useful vocabulary for conversations and everyday life.
- **Science:** words about nature, space, energy, and living things.
- **Technology:** words related to computers, the web, and digital tools.

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
- Browser local storage
- Python `unittest`

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

1. Choose a topic and difficulty on the home page.
2. Match each word to its definition before time runs out.
3. Watch your consecutive-correct streak as you work through the round.
4. Review your score, streak, and any missed meanings.
5. Try to beat your personal best or explore another topic.

## Personal records

Scores and streak records are saved in browser local storage. They are specific to the browser and device you use; they are not shared across devices and may be lost if browser data is cleared.

## Configuration and deployment

The app uses a development secret key by default so it can run locally. Before deploying publicly, set a strong `SECRET_KEY` environment variable and configure a production WSGI server. Do not use Flask's development server as the public production server.

## Documentation

- [Product Requirements Document](PRD.md)
- [Implementation Roadmap](ROADMAP.md)

## Project status

The game now supports themed vocabulary rounds, three difficulty levels, a countdown timer, streak tracking, and browser-based personal records. Run the automated test suite and manually check the game in a browser before deployment.

## Learning goals

This project provides practice with Python functions, lists and dictionaries, random selection, server-side validation, Flask routes and sessions, HTML templates, responsive CSS, JavaScript interactions, browser local storage, automated testing, and Git/GitHub.

## License

A license has not been selected yet.
