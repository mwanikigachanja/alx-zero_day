#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Function to get the computer's choice
int getComputerChoice() {
    // Generate a random number between 0 and 2
    return rand() % 3;
}

// Function to get the player's choice
int getPlayerChoice() {
    char choice[10];
    printf("Enter your choice (rock, paper, or scissors): ");
    scanf("%s", choice);

    if (strcmp(choice, "rock") == 0) {
        return 0;
    } else if (strcmp(choice, "paper") == 0) {
        return 1;
    } else if (strcmp(choice, "scissors") == 0) {
        return 2;
    } else {
        printf("Invalid choice. Please enter rock, paper, or scissors.\n");
        return getPlayerChoice();
    }
}

// Function to determine the winner
void determineWinner(int playerChoice, int computerChoice) {
    if (playerChoice == computerChoice) {
        printf("It's a tie!\n");
    } else if ((playerChoice == 0 && computerChoice == 2) ||
               (playerChoice == 1 && computerChoice == 0) ||
               (playerChoice == 2 && computerChoice == 1)) {
        printf("Congratulations! You win!\n");
    } else {
        printf("Computer wins. Better luck next time!\n");
    }
}

int main() {
    srand(time(NULL));

    printf("Welcome to Rock-Paper-Scissors!\n");

    while (1) {
        int playerChoice, computerChoice;
        playerChoice = getPlayerChoice();
        computerChoice = getComputerChoice();

        printf("You chose: ");
        switch (playerChoice) {
            case 0:
                printf("rock\n");
                break;
            case 1:
                printf("paper\n");
                break;
            case 2:
                printf("scissors\n");
                break;
        }

        printf("Computer chose: ");
        switch (computerChoice) {
            case 0:
                printf("rock\n");
                break;
            case 1:
                printf("paper\n");
                break;
            case 2:
                printf("scissors\n");
                break;
        }

        determineWinner(playerChoice, computerChoice);

        char playAgain;
        printf("Play again? (y/n): ");
        scanf(" %c", &playAgain);

        if (playAgain != 'y' && playAgain != 'Y') {
            break;
        }
    }

    return 0;
}

