# Word Matching Game

A beginner-friendly vocabulary game built with Python and Flask. Players match words with their definitions, submit their answers, receive a score, and review the correct meanings.

## Features

- Responsive home, game, and results pages.
- Six vocabulary words in each round.
- Shuffled words and definitions.
- Server-side answer checking and scoring.
- Progress counter while choosing answers.
- Results review and replay.
- Automated tests for scoring and important website routes.
- No account or database required.

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

If you already have the project, enter its folder and get the latest changes:

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

Open a second terminal, enter the project directory, activate the virtual environment, and run:

```bash
python -m unittest discover -s tests -v
```

## How to play

1. Select **Start playing** on the home page.
2. Choose a definition for each word.
3. Submit your answers to see your score.
4. Review the correct meanings and start another round.

## Configuration and deployment

The app uses a development secret key by default so it can run locally without extra setup. Before deploying publicly, set a strong `SECRET_KEY` environment variable and configure a production WSGI server. Do not use Flask's development server as the public production server.

## Documentation

- [Product Requirements Document](PRD.md)
- [Implementation Roadmap](ROADMAP.md)

## Project status

The first playable web version is implemented. Further work includes verifying the automated tests in a local environment, improving validation and deployment configuration, and publishing the app to a hosting platform.

## Learning goals

This project provides practice with Python functions, lists and dictionaries, server-side validation, Flask routes and sessions, HTML templates, responsive CSS, JavaScript interactions, automated testing, and Git/GitHub.

## License

A license has not been selected yet.
