#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// List of words for the game
const char* words[] = {
    "computer",
    "programming",
    "language",
    "algorithm",
    "developer",
    "software",
    "keyboard",
    "monitor",
    "internet",
    "application"
};
const int numWords = sizeof(words) / sizeof(words[0]);

// Function to choose a random word from the list
const char* chooseRandomWord() {
    int index = rand() % numWords;
    return words[index];
}

// Function to scramble the letters of the word
void scrambleWord(char* word) {
    int length = strlen(word);

    for (int i = 0; i < length - 1; i++) {
        int j = rand() % (length - i) + i;
        char temp = word[i];
        word[i] = word[j];
        word[j] = temp;
    }
}

int main() {
    srand(time(NULL));

    printf("Welcome to the Word Scramble Game!\n");
    printf("Unscramble the word to win.\n");

    while (1) {
        const char* originalWord = chooseRandomWord();
        char* scrambledWord = strdup(originalWord);

        scrambleWord(scrambledWord);

        printf("Scrambled word: %s\n", scrambledWord);

        char guess[100];
        printf("Your guess: ");
        scanf("%s", guess);

        if (strcmp(guess, originalWord) == 0) {
            printf("Congratulations! You unscrambled the word correctly.\n");
        } else {
            printf("Incorrect. The correct word is: %s\n", originalWord);
        }

        printf("Play again? (y/n): ");
        char playAgain;
        scanf(" %c", &playAgain);

        free(scrambledWord);

        if (playAgain != 'y' && playAgain != 'Y') {
            break;
        }
    }

    return 0;
}

