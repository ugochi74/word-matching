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

        // Work out which achievements this round has earned.
        const total = Number(scoreCard.dataset.total);
        const achievementKey = "wordmatch-achievements";
        let savedAchievements = {};

        try {
            const saved = JSON.parse(window.localStorage.getItem(achievementKey) || "{}");
            if (saved && typeof saved === "object" && !Array.isArray(saved)) {
                savedAchievements = saved;
            }
        } catch (error) {
            savedAchievements = {};
        }

        const earnedAchievements = {
            "first-victory": true,
            "streak-master": currentStreak >= 5,
            "perfect-round": total > 0 && score === total,
        };
        const achievementNames = {
            "first-victory": "First Victory",
            "streak-master": "Streak Master",
            "perfect-round": "Perfect Round",
        };
        const newlyUnlocked = [];

        for (const achievementId in earnedAchievements) {
            if (earnedAchievements[achievementId] && !savedAchievements[achievementId]) {
                newlyUnlocked.push(achievementNames[achievementId]);
            }
        }

        const updatedAchievements = { ...savedAchievements };
        for (const achievementId in earnedAchievements) {
            if (earnedAchievements[achievementId]) {
                updatedAchievements[achievementId] = true;
            }
        }
        window.localStorage.setItem(achievementKey, JSON.stringify(updatedAchievements));

        document.querySelectorAll("[data-achievement]").forEach((card) => {
            const achievementId = card.dataset.achievement;
            const isUnlocked = Boolean(updatedAchievements[achievementId]);
            card.classList.toggle("unlocked", isUnlocked);
            card.classList.toggle("locked", !isUnlocked);

            const status = card.querySelector(".achievement-status");
            if (status) {
                status.textContent = isUnlocked ? "Unlocked ✓" : "Locked";
            }
        });

        const achievementMessage = document.querySelector("#achievement-message");
        if (achievementMessage && newlyUnlocked.length > 0) {
            achievementMessage.textContent = `🎉 New badge unlocked: ${newlyUnlocked.join(", ")}!`;
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


// Click to hear a short sound for each correct or incorrect answer.
const resultSoundButton = document.querySelector("#sound-toggle");

function playResultTone(frequency, delay) {
    window.setTimeout(() => {
        try {
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const volume = audioContext.createGain();
            oscillator.type = "sine";
            oscillator.frequency.value = frequency;
            volume.gain.setValueAtTime(0.08, audioContext.currentTime);
            volume.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.12);
            oscillator.connect(volume);
            volume.connect(audioContext.destination);
            oscillator.start();
            oscillator.stop(audioContext.currentTime + 0.12);
            oscillator.addEventListener("ended", () => audioContext.close());
        } catch (error) {
            // Visual results remain available if audio is unsupported.
        }
    }, delay);
}

if (resultSoundButton) {
    resultSoundButton.textContent = "🔊 Hear result sounds";
    resultSoundButton.addEventListener("click", () => {
        try {
            window.localStorage.setItem("wordmatch-sound", "on");
        } catch (error) {
            // The sound button still works if storage is unavailable.
        }

        resultSoundButton.textContent = "🎵 Playing result sounds…";
        document.querySelectorAll(".review-status").forEach((status, index) => {
            const isCorrect = status.classList.contains("correct");
            playResultTone(isCorrect ? 740 : 260, index * 180);
        });
    });
}
