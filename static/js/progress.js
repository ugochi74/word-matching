const progressPanel = document.querySelector("#player-progress");

if (progressPanel) {
    const gamesPlayed = document.querySelector("#progress-games-played");
    const averageScore = document.querySelector("#progress-average-score");
    const bestScore = document.querySelector("#progress-best-score");
    const recentGames = document.querySelector("#progress-recent-games");
    const emptyMessage = document.querySelector("#progress-empty");

    try {
        const saved = JSON.parse(window.localStorage.getItem("wordmatch-progress") || "null");

        if (!saved || !saved.gamesPlayed) {
            emptyMessage.hidden = false;
        } else {
            gamesPlayed.textContent = String(saved.gamesPlayed);

            const average = saved.totalQuestions > 0
                ? Math.round((saved.totalCorrect / saved.totalQuestions) * 100)
                : 0;
            averageScore.textContent = `${average}%`;

            if (saved.bestScore) {
                bestScore.textContent = `${saved.bestScore.score}/${saved.bestScore.total} (${saved.bestScore.percentage}%)`;
            }

            const history = Array.isArray(saved.history) ? saved.history : [];
            if (history.length > 0) {
                recentGames.innerHTML = "";
                history.slice(0, 5).forEach((game) => {
                    const item = document.createElement("li");
                    const date = new Date(game.date);
                    const dateLabel = Number.isNaN(date.getTime())
                        ? "Recent game"
                        : date.toLocaleDateString();
                    item.textContent = `${dateLabel} — ${game.score}/${game.total} (${game.percentage}%) · ${game.category}`;
                    recentGames.appendChild(item);
                });
            }
        }
    } catch (error) {
        emptyMessage.textContent =
            "Progress is unavailable because browser storage could not be read.";
        emptyMessage.hidden = false;
    }
}
