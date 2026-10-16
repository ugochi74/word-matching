# Product Requirements Document (PRD)
## Word Matching Game

**Status:** Draft — MVP planning  
**Project type:** Python-powered web game  
**Repository:** https://github.com/ugochi74/word-matching

## 1. Product overview

Word Matching Game is a simple, responsive website where players match words to their correct definitions. The game should feel clear and enjoyable for first-time players while providing a practical project for learning Python and web development.

The first release focuses on a complete, reliable single-player game. It will not include accounts, multiplayer, payments, or a database.

## 2. Problem and opportunity

People need a simple way to practise vocabulary and remember word meanings. A small game with immediate feedback and a score makes this practice more engaging than reading a plain list of definitions.

This project also gives its developer a manageable way to practise Python functions, data structures, validation, testing, and Flask.

## 3. Goals

- Let a player start and finish a round without confusion.
- Test word-to-definition matching.
- Provide immediate, understandable feedback.
- Track score and progress during a round.
- Work on common desktop and mobile screen sizes.
- Keep the code simple, readable, and testable.

## 4. Target users

- Students and learners practising vocabulary.
- Casual players who enjoy short word puzzles.
- Beginners learning Python and web development.

## 5. MVP user journey

1. The player opens the home page.
2. The player selects a difficulty or accepts the default.
3. The game displays a word and a set of possible definitions (or two matching columns if that interaction is selected during implementation).
4. The player chooses a match.
5. The game checks the answer and shows feedback.
6. The score and progress update.
7. The player continues until the round is complete.
8. The results screen shows the final score and offers a replay option.

## 6. Functional requirements

### FR-1: Start a game
The website must let the player start a new round and clearly explain how to play.

### FR-2: Display matching choices
Each round must display a set of words and definitions. Each word must have one correct definition in that round.

### FR-3: Check answers
The game must compare the player's choice with the correct answer using Python game logic. The server must not trust a score submitted by the browser.

### FR-4: Give feedback
The interface must clearly indicate whether a match is correct or incorrect and let the player continue.

### FR-5: Track progress
The game must show progress through the round, number of correct matches, and score.

### FR-6: Complete and replay
When all required matches are answered, show a results summary and allow the player to start again.

### FR-7: Difficulty
Provide at least an easy level for the MVP. Medium and hard levels may use more words or less familiar vocabulary once the basic game is stable.

### FR-8: Responsive interface
Controls and text must remain readable and usable on mobile and desktop.

### FR-9: Handle invalid input
Unknown question IDs, invalid choices, repeated submissions, and missing form values must be handled safely with a helpful message or a rejected request.

## 7. Non-functional requirements

- Use readable, beginner-friendly Python.
- Separate core game rules from Flask routes and HTML templates.
- Validate game actions on the server.
- Use semantic HTML and accessible labels.
- Provide visible focus states and sufficient text contrast.
- Avoid collecting personal information in the MVP.
- Include automated tests for core rules and important routes.
- Keep installation steps documented in the README.

## 8. Proposed technology

- **Python 3** — game rules and server-side logic.
- **Flask** — routes and HTTP request handling.
- **HTML templates** — page structure.
- **CSS** — visual design and responsive layout.
- **JavaScript** — optional interaction enhancements.
- **unittest** (built into Python) — first choice for tests, avoiding unnecessary dependencies.

## 9. Proposed game rules

- A round contains a fixed number of word-definition pairs.
- Each word has exactly one correct definition in the round.
- A correct answer increases the score.
- An incorrect answer does not increase the score.
- Each word should only be scored once.
- The round ends when all required matches have been answered.
- Starting a new game resets round progress and score.
- Exact scoring values and round size will be confirmed during implementation and documented in the interface.

## 10. MVP acceptance criteria

The MVP is ready when:

- [ ] The app starts locally using documented instructions.
- [ ] A player can start a new game.
- [ ] Words and definitions are displayed clearly.
- [ ] Correct and incorrect answers are handled correctly.
- [ ] Score and progress update consistently.
- [ ] Repeated or invalid submissions cannot award extra points.
- [ ] The player sees a results screen and can replay.
- [ ] The main layout works on mobile and desktop.
- [ ] Automated tests cover core matching rules and key routes.
- [ ] README setup and usage instructions match the implemented app.

## 11. Out of scope for the first release

- User accounts and profiles.
- Online leaderboards.
- Multiplayer or live competitions.
- Database-backed long-term score history.
- AI-generated definitions.
- Payments, advertisements, or analytics tracking.

These can be considered only after the MVP works reliably.

## 12. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Score can be manipulated in the browser | Validate answers and calculate scores in Python on the server |
| The first version becomes too complex | Deliver one complete single-player mode before adding extras |
| Duplicate answers cause incorrect scoring | Track answered question IDs in the game state |
| Vocabulary data contains mistakes | Keep a small curated question bank and test its structure |
| Mobile controls are hard to use | Use responsive layouts, readable text, and touch-friendly controls |
