const answerFields = document.querySelectorAll(".matching-form select");
const answerCount = document.querySelector("#answer-count");
const matchingForm = document.querySelector("#matching-form");
const timer = document.querySelector("#timer");
const timerBar = document.querySelector("#timer-bar");
const gameMessage = document.querySelector("#game-message");
const hintButtons = document.querySelectorAll(".hint-button");
const hintsRemaining = document.querySelector("#hints-remaining");

const HINT_LIMIT = 3;
let hintsUsed = 0;

function updateAnswerCount() {
    if (!answerCount) {
        return;
    }

    let answered = 0;
    answerFields.forEach((field) => {
        if (field.value !== "") {
            answered += 1;
        }
    });

    answerCount.textContent = `${answered} of ${answerFields.length} answered`;
    if (answered === answerFields.length && answerFields.length > 0) {
        answerCount.textContent += " — all set!";
    }
}

hintButtons.forEach((button) => {
    button.addEventListener("click", () => {
        if (hintsUsed >= HINT_LIMIT) {
            return;
        }

        const wordId = button.dataset.wordId;
        const correctOption = document.querySelector(
            `#${wordId} option[value="${wordId}"]`
        );
        const hintText = document.querySelector(`#hint-${wordId}`);

        if (!correctOption || !hintText) {
            return;
        }

        const definitionWords = correctOption.textContent.trim().split(/\s+/);
        const clue = definitionWords.slice(0, Math.min(4, definitionWords.length)).join(" ");
        hintText.textContent = `Clue: The meaning begins with “${clue}”`;
        button.disabled = true;
        button.textContent = "Hint used";
        hintsUsed += 1;

        const remaining = HINT_LIMIT - hintsUsed;
        hintsRemaining.textContent = `${remaining} hint${remaining === 1 ? "" : "s"} remaining`;

        if (remaining === 0) {
            hintButtons.forEach((hintButton) => {
                if (!hintButton.disabled) {
                    hintButton.disabled = true;
                }
            });
        }
    });
});

answerFields.forEach((field) => {
    field.addEventListener("change", updateAnswerCount);
});

updateAnswerCount();

if (timer && matchingForm) {
    const totalSeconds = Number(timer.dataset.seconds) || 60;
    let secondsLeft = totalSeconds;
    timerBar.style.width = "100%";

    const countdown = window.setInterval(() => {
        secondsLeft -= 1;
        timer.textContent = `${secondsLeft}s`;
        timerBar.style.width = `${Math.max(0, (secondsLeft / totalSeconds) * 100)}%`;

        if (secondsLeft <= 10) {
            timer.classList.add("timer-warning");
            timerBar.style.background = "#c96d43";
        }

        if (secondsLeft <= 0) {
            window.clearInterval(countdown);
            answerFields.forEach((field) => field.removeAttribute("required"));
            if (gameMessage) {
                gameMessage.textContent = "Time's up! Your answers are being checked.";
            }
            matchingForm.requestSubmit();
        }
    }, 1000);

    matchingForm.addEventListener("submit", () => {
        window.clearInterval(countdown);
    });
}
