import random

# List of words to choose from
words_list = ["python", "programming", "computer", "science", "keyboard", "mouse", "monitor", "internet"]

def choose_random_word():
    return random.choice(words_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    print("Welcome to Hangman!")
    print("Try to guess the word one letter at a time.")
    print("You have 6 attempts to guess the word correctly.")

    word_to_guess = choose_random_word()
    max_attempts = 6
    guessed_letters = []

    while max_attempts > 0:
        print("\n----------------------------------")
        print("Word:", display_word(word_to_guess, guessed_letters))
        print("Attempts left:", max_attempts)

        if "_" not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You guessed the word correctly.")
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word_to_guess:
            max_attempts -= 1
            print("Incorrect guess. Try again.")

    if "_" in display_word(word_to_guess, guessed_letters):
        print("Sorry, you ran out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    main()

