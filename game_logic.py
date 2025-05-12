import random
from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
            if mistakes == 3:
                print(f"Game Over! The secret word was {secret_word}")
                break