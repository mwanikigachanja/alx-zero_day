import random

def get_player_input():
    while True:
        try:
            player_input = int(input("Enter a number between 1 and 100: "))
            if 1 <= player_input <= 100:
                return player_input
            else:
                print("Please enter a valid number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def reverse_guessing_game():
    print("Welcome to the Reverse Guessing Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("After each guess, provide me with a hint: 'h' if the number is higher, 'l' if it's lower, and 'c' if I guessed correctly.")

    lower_bound = 1
    upper_bound = 100
    computer_guess = random.randint(lower_bound, upper_bound)

    while True:
        print(f"My guess is {computer_guess}.")
        hint = input("Is my guess higher (h), lower (l), or correct (c)? ").lower()

        if hint == 'h':
            lower_bound = computer_guess + 1
        elif hint == 'l':
            upper_bound = computer_guess - 1
        elif hint == 'c':
            print(f"Yay! I guessed your number {computer_guess} correctly.")
            break
        else:
            print("Invalid hint. Please provide 'h', 'l', or 'c'.")

        if lower_bound > upper_bound:
            print("You are providing conflicting hints. Please play honestly.")
            break

        computer_guess = random.randint(lower_bound, upper_bound)

if __name__ == "__main__":
    reverse_guessing_game()

