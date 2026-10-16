const answerFields = document.querySelectorAll(".matching-form select");
const answerCount = document.querySelector("#answer-count");

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
}

answerFields.forEach((field) => {
    field.addEventListener("change", updateAnswerCount);
});

updateAnswerCount();
