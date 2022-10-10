const gamesEl = document.querySelector(".games-list");
const gamesList = Array.from(gamesEl.children);

const selectEl = document.getElementById("game-select");


selectEl.addEventListener("change", (e) => {
  const selectedValue = e.target.value;

  if (selectedValue === "all") {
    gamesList.forEach((game) => {
      game.style.display = "block";
    });
  } else {
    const foundGame = gamesList.find((game) => game.dataset.name === selectedValue);
    foundGame.style.display = "block"
    const remainingGames = gamesList.filter(
      (game) => game.dataset.name !== selectedValue
    );
    remainingGames.forEach((game) => {
      game.style.display = "none";
    });
  }
});
