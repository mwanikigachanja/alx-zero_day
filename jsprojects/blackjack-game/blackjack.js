// blackjack.js
const readline = require('readline-sync');

// Function to generate a deck of cards
function generateDeck() {
  const suits = ['♠', '♣', '♦', '♥'];
  const values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'];

  const deck = [];
  for (const suit of suits) {
    for (const value of values) {
      deck.push({ suit, value });
    }
  }

  return deck;
}

// Function to shuffle the deck
function shuffle(deck) {
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [deck[i], deck[j]] = [deck[j], deck[i]];
  }
}

// Function to calculate the total value of a hand
function getHandValue(hand) {
  let total = 0;
  let hasAce = false;

  for (const card of hand) {
    if (card.value === 'A') {
      hasAce = true;
      total += 11;
    } else if (['K', 'Q', 'J'].includes(card.value)) {
      total += 10;
    } else {
      total += parseInt(card.value, 10);
    }
  }

  if (hasAce && total > 21) {
    total -= 10;
  }

  return total;
}

// Function to display a hand
function displayHand(hand) {
  return hand.map((card) => card.suit + card.value).join(', ');
}

// Main game function
function playBlackjack() {
  const deck = generateDeck();
  shuffle(deck);

  const playerHand = [];
  const dealerHand = [];

  // Deal two cards to the player and dealer
  playerHand.push(deck.pop());
  dealerHand.push(deck.pop());
  playerHand.push(deck.pop());
  dealerHand.push(deck.pop());

  console.log('Your hand:', displayHand(playerHand));
  console.log('Dealer\'s hand:', displayHand([dealerHand[0], { suit: '??', value: '??' }]));

  while (true) {
    const playerValue = getHandValue(playerHand);
    if (playerValue === 21) {
      console.log('Blackjack! You win!');
      break;
    } else if (playerValue > 21) {
      console.log('Busted! You lose.');
      break;
    }

    const action = readline.question('Do you want to "hit" or "stand"? ');
    if (action.toLowerCase() === 'hit') {
      playerHand.push(deck.pop());
      console.log('Your hand:', displayHand(playerHand));
    } else if (action.toLowerCase() === 'stand') {
      // Dealer's turn
      const dealerValue = getHandValue(dealerHand);

      while (dealerValue < 17) {
        dealerHand.push(deck.pop());
        dealerValue = getHandValue(dealerHand);
      }

      console.log('Your hand:', displayHand(playerHand));
      console.log('Dealer\'s hand:', displayHand(dealerHand));

      if (dealerValue > 21 || dealerValue < playerValue) {
        console.log('You win!');
      } else if (dealerValue === playerValue) {
        console.log('Push! It\'s a tie.');
      } else {
        console.log('You lose.');
      }

      break;
    } else {
      console.log('Invalid input. Please enter "hit" or "stand".');
    }
  }
}

playBlackjack();

