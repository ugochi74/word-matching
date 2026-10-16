const answerFields = document.querySelectorAll(".matching-form select");
const answerCount = document.querySelector("#answer-count");
const matchingForm = document.querySelector("#matching-form");
const timer = document.querySelector("#timer");
const timerBar = document.querySelector("#timer-bar");
const gameMessage = document.querySelector("#game-message");

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
