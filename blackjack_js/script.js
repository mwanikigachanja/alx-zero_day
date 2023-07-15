// GAME LOGIC
// Global Variables
let deck = [];
let playerHand = [];
let dealerHand = [];
let currentPlayer = 'player';
let gameOver = false;

// Card Values
const cardValues = {
  '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
  'JACK': 10, 'QUEEN': 10, 'KING': 10, 'ACE': 11
};

// Initialize the game
function startGame() {
  // Shuffle the deck
  deck = createDeck();
  shuffleDeck(deck);

  // Deal the initial hands
  playerHand = [getNextCard(), getNextCard()];
  dealerHand = [getNextCard()];

  // Render the game view
  renderGameView();
}

// Hit - Draw a new card for the player
function hit() {
  if (!gameOver) {
    playerHand.push(getNextCard());
    renderGameView();
    checkPlayerBust();
  }
}

// Stand - Player chooses to stop receiving cards
function stand() {
  if (!gameOver) {
    currentPlayer = 'dealer';
    while (getHandValue(dealerHand) < 17) {
      dealerHand.push(getNextCard());
    }
    checkWinner();
  }
}

// Restart the game
function restartGame() {
  playerHand = [];
  dealerHand = [];
  currentPlayer = 'player';
  gameOver = false;
  document.getElementById('result').textContent = '';
  startGame();
}

// Create a new deck of cards
function createDeck() {
  const suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES'];
  const values = Object.keys(cardValues);
  const deck = [];
  for (const suit of suits) {
    for (const value of values) {
      deck.push({ suit, value });
    }
  }
  return deck;
}

// Shuffle the deck using Fisher-Yates algorithm
function shuffleDeck(deck) {
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }
}

// Get the next card from the deck
function getNextCard() {
  return deck.pop();
}

// Calculate the value of a hand
function getHandValue(hand) {
  let value = 0;
  let aceCount = 0;
  for (const card of hand) {
    if (card.value === 'ACE') {
      aceCount++;
    }
    value += cardValues[card.value];
  }
  while (value > 21 && aceCount > 0) {
    value -= 10;
    aceCount--;
  }
  return value;
}

// Check if the player's hand value exceeds 21 (bust)
function checkPlayerBust() {
  if (getHandValue(playerHand) > 21) {
    currentPlayer = 'dealer';
    gameOver = true;
    checkWinner();
  }
}

// Check who wins the game
function checkWinner() {
  const playerValue = getHandValue(playerHand);
  const dealerValue = getHandValue(dealerHand);
  let result = '';

  if (playerValue > 21) {
    result = 'Player Busts! You lose.';
  } else if (dealerValue > 21) {
    result = 'Dealer Busts! You win.';
  } else if (playerValue === dealerValue) {
    result = 'It\'s a tie!';
  } else if (playerValue > dealerValue) {
    result = 'You win!';
  } else {
    result = 'You lose.';
  }

  document.getElementById('result').textContent = result;
  renderGameView();
  gameOver = true;
}

// Render the game view
function renderGameView() {
  const playerHandElement = document.getElementById('player-hand');
  const dealerHandElement = document.getElementById('dealer-hand');
  playerHandElement.innerHTML = '';
  dealerHandElement.innerHTML = '';

  for (const card of playerHand) {
    const img = document.createElement('img');
    img.src = `cards/${card.suit}/${card.value}.png`;
    playerHandElement.appendChild(img);
  }

  for (const card of dealerHand) {
    const img = document.createElement('img');
    img.src = `cards/${card.suit}/${card.value}.png`;
    dealerHandElement.appendChild(img);
  }

  if (currentPlayer === 'dealer' && !gameOver) {
    const cardBack = document.createElement('img');
    cardBack.src = 'cards/card-back.png';
    dealerHandElement.appendChild(cardBack);
  }

  const message = document.getElementById('message');
  if (!gameOver) {
    if (currentPlayer === 'player') {
      message.textContent = 'Your turn!';
    } else {
      message.textContent = 'Dealer\'s turn...';
    }
  } else {
    message.textContent = '';
  }
}

