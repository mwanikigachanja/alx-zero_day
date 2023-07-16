#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to calculate the total value of a hand
int calculateHandValue(int hand[], int numCards) {
    int value = 0;
    int numAces = 0;

    for (int i = 0; i < numCards; i++) {
        if (hand[i] == 1) { // Ace
            numAces++;
        }
        value += hand[i];
    }

    while (numAces > 0 && value + 10 <= 21) {
        value += 10;
        numAces--;
    }

    return value;
}

// Function to display a hand
void displayHand(int hand[], int numCards) {
    for (int i = 0; i < numCards; i++) {
        printf("%d ", hand[i]);
    }
    printf("\n");
}

int main() {
    int deck[52] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,  // Cards 2 to 10 and face cards (J, Q, K) have value 10
                    10, 10, 10, 11,                       // Ace can be 1 or 11
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                    10, 10, 10, 11,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
                    10, 10, 10, 11};

    int playerHand[10];
    int dealerHand[10];
    int numPlayerCards = 0;
    int numDealerCards = 0;

    srand(time(NULL));

    // Initial deal: Player gets two cards, Dealer gets one card face-up
    playerHand[numPlayerCards++] = deck[rand() % 52];
    playerHand[numPlayerCards++] = deck[rand() % 52];
    dealerHand[numDealerCards++] = deck[rand() % 52];

    printf("Welcome to Blackjack!\n\n");
    printf("Your hand: ");
    displayHand(playerHand, numPlayerCards);
    printf("Dealer's hand: %d\n\n", dealerHand[0]);

    // Player's turn
    while (1) {
        int choice;
        printf("Enter 1 to hit or 2 to stand: ");
        scanf("%d", &choice);

        if (choice == 1) {
            playerHand[numPlayerCards++] = deck[rand() % 52];
            printf("Your hand: ");
            displayHand(playerHand, numPlayerCards);

            int playerValue = calculateHandValue(playerHand, numPlayerCards);
            if (playerValue > 21) {
                printf("Bust! You lose.\n");
                return 0;
            }
        } else if (choice == 2) {
            break;
        } else {
            printf("Invalid choice. Please enter 1 to hit or 2 to stand.\n");
        }
    }

    // Dealer's turn
    printf("\nDealer's hand: ");
    displayHand(dealerHand, numDealerCards);
    while (1) {
        int dealerValue = calculateHandValue(dealerHand, numDealerCards);
        if (dealerValue >= 17) {
            break;
        }

        dealerHand[numDealerCards++] = deck[rand() % 52];
        printf("Dealer's hand: ");
        displayHand(dealerHand, numDealerCards);
    }

    // Determine the winner
    int playerValue = calculateHandValue(playerHand, numPlayerCards);
    int dealerValue = calculateHandValue(dealerHand, numDealerCards);

    printf("\nYour hand value: %d\n", playerValue);
    printf("Dealer's hand value: %d\n\n", dealerValue);

    if (playerValue > dealerValue && playerValue <= 21) {
        printf("Congratulations! You win!\n");
    } else if (dealerValue > 21 && playerValue <= 21) {
        printf("Dealer busts! You win!\n");
    } else {
        printf("Dealer wins. Better luck next time!\n");
    }

    return 0;
}

