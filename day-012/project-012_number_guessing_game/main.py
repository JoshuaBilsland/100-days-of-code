#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import art
import random

EASY_GUESSES_REMAINING = 5
HARD_GUESSES_REMAINING = 10


def main():
    print(get_random_number())


def get_random_number():
    return random.randint(1, 100)


if __name__ == "__main__":
    print(art.logo)
    main()
