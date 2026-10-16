# Word Matching Game

A beginner-friendly word matching game built with Python and Flask. Players match words with their correct meanings, earn points for correct answers, and try to complete each round with as few mistakes as possible.

The goal is to build a small, polished web game while practising Python fundamentals, web development, input validation, testing, and Git/GitHub workflow.

## Planned features

- Match each word with the correct definition.
- Choose a difficulty level.
- Track score, correct answers, and attempts.
- Start a new round or restart the game.
- Give clear feedback after each answer.
- Responsive layout for desktop and mobile.
- A small question bank that can be expanded over time.

## Planned technology

- **Python** for game rules and scoring.
- **Flask** for the web server and routes.
- **HTML** for page structure.
- **CSS** for styling and responsive layout.
- **JavaScript** for interactive matching controls where useful.
- **unittest** or **pytest** for testing core game logic.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/ugochi74/word-matching.git
cd word-matching
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

Once `requirements.txt` has been added:

```bash
python -m pip install -r requirements.txt
```

The planned web framework is Flask.

### 4. Run the application

The run command will be added when the Flask application is implemented. The planned entry point is `app.py`.

## Planned project structure

```text
word-matching/
├── app.py
├── game.py
├── questions.py
├── requirements.txt
├── templates/
│   ├── index.html
│   └── game.html
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

This structure is the initial plan and may change as the project develops.

## Documentation

- [Product Requirements Document](PRD.md)
- [Implementation Roadmap](ROADMAP.md)

## Current status

**Planning stage.** The product requirements and implementation plan are being documented before the game is built.

## Learning goals

By completing this project, you will practise:

- Variables, lists, dictionaries, conditions, loops, and functions.
- Separating game logic from web routes and page presentation.
- Validating player choices on the server.
- Writing tests for correct and incorrect matches.
- Building a responsive interface and using Git branches and commits.

## Scope and privacy

The first version is a learning project. It will not require accounts, collect personal information, or process payments. Scores can remain temporary for a single game session until persistent storage is intentionally added.

## License

A license has not been selected yet.
