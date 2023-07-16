import random

def generate_secret_combination():
    return [random.randint(1, 6) for _ in range(6)]

def get_user_guess():
    try:
        user_input = input("Enter your guess (6 numbers from 1 to 6, separated by spaces): ")
        user_guess = [int(num) for num in user_input.split()]
        return user_guess
    except ValueError:
        print("Invalid input. Please enter 6 numbers from 1 to 6, separated by spaces.")
        return get_user_guess()

def compare_combinations(secret_combination, user_guess):
    correct_positions = 0
    correct_numbers = 0

    for i in range(6):
        if user_guess[i] == secret_combination[i]:
            correct_positions += 1
        elif user_guess[i] in secret_combination:
            correct_numbers += 1

    return correct_positions, correct_numbers

def main():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret combination of 6 numbers from 1 to 6.")

    secret_combination = generate_secret_combination()
    max_attempts = 10

    while max_attempts > 0:
        print("\n----------------------------------")
        user_guess = get_user_guess()
        
        if len(user_guess) != 6 or any(num < 1 or num > 6 for num in user_guess):
            print("Invalid guess. Please enter 6 numbers from 1 to 6.")
            continue

        max_attempts -= 1

        correct_positions, correct_numbers = compare_combinations(secret_combination, user_guess)

        print(f"Correct positions: {correct_positions}")
        print(f"Correct numbers but wrong positions: {correct_numbers}")

        if correct_positions == 6:
            print("Congratulations! You guessed the correct combination.")
            break

        print(f"Attempts left: {max_attempts}")

    if correct_positions != 6:
        print("Sorry, you ran out of attempts. The secret combination was:", secret_combination)

if __name__ == "__main__":
    main()

