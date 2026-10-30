import random

# Load words from the downloaded file
with open("words.txt", "r", encoding="utf-8") as file:
    words = [word.strip().lower() for word in file if word.strip()]

# Choose a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect attempts allowed
attempts_left = 6
# Hangman drawings for each number of incorrect guesses
hangman_art = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]

print("================================")
print("   WELCOME TO HANGMAN!")
print("================================")

print("\nGuess the hidden word, one letter at a time!")
print("You have 6 incorrect attempts available.")

# Main game loop
while attempts_left > 0:
    print(hangman_art[6 - attempts_left])
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts_left)

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess! 🎉")
    else:
        attempts_left -= 1
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won! 🏆")
        print("The word was:", secret_word)
        break

if attempts_left == 0:
    print("\nGame over! Better luck next time!")
    print("The word was:", secret_word)
