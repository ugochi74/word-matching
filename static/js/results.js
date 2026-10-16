const scoreCard = document.querySelector("#score-card");
const personalBest = document.querySelector("#personal-best");
const newRecord = document.querySelector("#new-record");
const bestStreakRecord = document.querySelector("#best-streak-record");

if (scoreCard && personalBest) {
    const score = Number(scoreCard.dataset.score);
    const difficulty = scoreCard.dataset.difficulty;
    const category = scoreCard.dataset.category;
    const storageKey = `wordmatch-best-${category}-${difficulty}`;
    const streakKey = `wordmatch-streak-${category}-${difficulty}`;
    const currentStreak = Number(document.querySelector("#current-best-streak")?.dataset.streak || 0);

    try {
        const savedScore = Number(window.localStorage.getItem(storageKey) || 0);
        const savedStreak = Number(window.localStorage.getItem(streakKey) || 0);
        const isNewRecord = score > savedScore;

        if (isNewRecord) {
            window.localStorage.setItem(storageKey, String(score));
        }
        if (currentStreak > savedStreak) {
            window.localStorage.setItem(streakKey, String(currentStreak));
        }

        const bestScore = Math.max(score, savedScore);
        const bestStreak = Math.max(currentStreak, savedStreak);
        personalBest.textContent = `${bestScore} points`;

        if (bestStreakRecord) {
            bestStreakRecord.textContent = `${bestStreak} in a row`;
        }
        if (isNewRecord && newRecord) {
            newRecord.textContent = "🏆 New personal best! You beat your previous score.";
        }
    } catch (error) {
        personalBest.textContent = "Unavailable";
        if (bestStreakRecord) {
            bestStreakRecord.textContent = "Unavailable";
        }
        if (newRecord) {
            newRecord.textContent = "Your browser blocked local storage, so records could not be saved.";
        }
    }
}
