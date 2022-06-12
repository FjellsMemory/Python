"""Play the game of hangman."""

import random


def input_choice(question: str, answers: list) -> str:
    """Ask question repeatedly until answer from list is entered."""
    print(question + " [" + ' | '.join(answers) + "]")
    answer = input("> ")
    while answer not in answers:
        print("Invalid answer. Try again.")
        answer = input("> ")
    return answer


def shape(word: str, guesses: str) -> str:
    """Return string with letters from 'guesses' in 'word' printed, else "_"."""
    newstr = ""
    for i in word:
        if i in guesses:
            newstr = newstr + f"{i}"
        else:
            newstr = newstr + "_"
    return newstr


def hangman(word: str, chances: int):
    """Play a round of hangman using 'word' and 'chances'."""
    so_far = shape(word, "")
    left = chances
    right = ""
    won = False
    while left > 0:
        guess = input(f"{so_far}; " + f"{left} " + "mistakes left; make a \
guess: ")
        if len(guess) != 1:
            continue
        if guess in word:
            right = right + f"{guess}"
            so_far = shape(word, right)
            if "_" not in so_far:
                won = True
                break
            else:
                continue
        else:
            left = left - 1
    if won is True:
        print(f"You won! The word was '{word}'! You're the best! Everyone \
loves you!")
    else:
        print(f"You lost. You suck. The word was '{word}'.")


if __name__ == "__main__":
    words = ['apple', 'tree', 'python', 'bench', 'float']

    max_fails = int(input("Number of allowed mistakes: "))

    while input_choice("Wanna play a game?", ['yes', 'no']) == 'yes':
        word = random.choice(words)  # Wähle ein zufälliges Wort aus.
        hangman(word, max_fails)