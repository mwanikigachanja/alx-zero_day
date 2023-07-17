#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int lowerBound = 1;
    int upperBound = 6;
    int secretNumber, guess, numAttempts = 0;

    // Seed the random number generator
    srand(time(NULL));

    // Generate a random number between the lower and upper bounds (inclusive)
    secretNumber = (rand() % (upperBound - lowerBound + 1)) + lowerBound;

    printf("Welcome to the Guessing Game!\n");
    printf("I'm thinking of a number between %d and %d.\n", lowerBound, upperBound);

    while (1) {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        numAttempts++;

        if (guess < secretNumber) {
            printf("Too low! Try again.\n");
        } else if (guess > secretNumber) {
            printf("Too high! Try again.\n");
        } else {
            printf("Congratulations! You guessed the number %d correctly in %d attempts!\n", secretNumber, numAttempts);
            break;
        }
    }

    return 0;
}

