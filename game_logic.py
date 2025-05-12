import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """displaying the state of the game to the user"""
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    """the main game loop and functionality of the game"""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1
            if mistakes == 3:
                print(f"Game Over! The secret word was {secret_word}")
                break

    replay = input("Would you like to play again? (y/n): ").lower()
    if replay == "n":
        print("Thank you for playing!")
    elif replay == "y":
        play_game()