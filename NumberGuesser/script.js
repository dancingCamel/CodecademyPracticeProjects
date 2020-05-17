let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:

const generateTarget = () => {
	return Math.floor(Math.random() * 10);
};

const compareGuesses = (human, comp, target) => {
	let human_diff = Math.abs(target - human);
	let comp_diff = Math.abs(target - comp);

	if (human_diff < comp_diff || human_diff === comp_diff) {
		return true;
	}

	return false;
};

const updateScore = (winner) => {
	if (winner === 'human') {
		humanScore++;
	}
	else {
		computerScore++;
	}
};

const advanceRound = () => {
	currentRoundNumber++;
};
