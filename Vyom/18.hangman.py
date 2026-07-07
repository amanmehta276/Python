# Hangman game
import random

# Hangman art
HANGMAN_ART = {
    0: (
        "   ",
        "   ",
        "   "
    ),
    1: (
        " o ",
        "   ",
        "   "
    ),
    2: (
        " o ",
        " | ",
        "   "
    ),
    3: (
        " o ",
        "/| ",
        "   "
    ),
    4: (
        " o ",
        "/|\\",
        "   "
    ),
    5: (
        " o ",
        "/|\\",
        "/  "
    ),
    6: (
        " o ",
        "/|\\",
        "/ \\"
    )
}

# Words and hints
words = {
    "python": "A popular programming language",
    "apple": "A famous fruit",
    "computer": "An electronic machine",
    "mango": "The king of fruits",
    "banana": "A yellow fruit"
}


def display_man(wrong_guesses):
    """Display hangman art."""
    print()
    for line in HANGMAN_ART[wrong_guesses]:
        print(line)


def display_hint(word):
    """Display hidden word."""
    print("\nWord:", " ".join(word))


def main():

    secret_word, hint = random.choice(list(words.items()))

    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    display_word = ["_"] * len(secret_word)

    print("🎮 Welcome to Hangman!")
    print(f"💡 Hint: {hint}")

    while wrong_guesses < max_wrong_guesses and "_" in display_word:

        display_man(wrong_guesses)
        display_hint(display_word)

        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("✅ Correct!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess

        else:
            wrong_guesses += 1
            print("❌ Wrong!")

    # Final result
    display_man(wrong_guesses)

    if "_" not in display_word:
        print(f"\n🎉 You guessed the word: {secret_word}")
    else:
        print(f"\n💀 Game Over! The word was '{secret_word}'")


if __name__ == "__main__":
    main()