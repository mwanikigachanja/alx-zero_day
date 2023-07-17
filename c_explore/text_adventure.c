#include <stdio.h>
#include <stdlib.h>

void waitForKeyPress() {
    printf("\nPress Enter to continue...\n");
    while (getchar() != '\n');
}

int main() {
    printf("Welcome to the Text Adventure Game!\n");
    printf("You find yourself in front of a dark cave.\n");

    waitForKeyPress();

    printf("Do you want to enter the cave? (y/n): ");
    char choice;
    scanf(" %c", &choice);

    if (choice == 'y' || choice == 'Y') {
        printf("\nYou cautiously enter the cave.\n");
        printf("In the darkness, you see two passages.\n");

        waitForKeyPress();

        printf("\nWhich passage will you take? (1/2): ");
        int passage;
        scanf("%d", &passage);

        if (passage == 1) {
            printf("\nYou chose passage 1.\n");
            printf("As you walk deeper, you discover a treasure chest!\n");
            printf("Congratulations, you found the treasure! You win!\n");
        } else if (passage == 2) {
            printf("\nYou chose passage 2.\n");
            printf("The passage leads to a dead-end, and you are trapped!\n");
            printf("Game Over!\n");
        } else {
            printf("\nInvalid choice. You hesitate too long and get stuck in indecision.\n");
            printf("Game Over!\n");
        }
    } else {
        printf("\nYou decide not to enter the cave. The adventure ends here.\n");
    }

    return 0;
}

