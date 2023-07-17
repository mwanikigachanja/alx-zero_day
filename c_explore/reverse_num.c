#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int lowerBound = 1;
    int upperBound = 100;
    int secretNumber, guess;
    char hint;

    // Seed the random number generator
    srand(time(NULL));

    printf("Welcome to the Reverse Number Guessing Game!\n");
    printf("Think of a number between %d and %d.\n", lowerBound, upperBound);

    while (1) {
        // Generate a random guess between the lower and upper bounds (inclusive)
        guess = (rand() % (upperBound - lowerBound + 1)) + lowerBound;

        printf("Is your number %d? (h/l/c): ", guess);
        scanf(" %c", &hint);

        if (hint == 'c' || hint == 'C') {
            printf("Great! I guessed your number %d.\n", guess);
            break;
        } else if (hint == 'h' || hint == 'H') {
            // If the guess is too high, adjust the upper bound
            upperBound = guess - 1;
        } else if (hint == 'l' || hint == 'L') {
            // If the guess is too low, adjust the lower bound
            lowerBound = guess + 1;
        } else {
            printf("Invalid input. Please enter 'h' for higher, 'l' for lower, or 'c' for correct.\n");
        }
    }

    return 0;
}

