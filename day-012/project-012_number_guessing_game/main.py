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
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(f"You have {get_guesses_remaining(user_difficulty)} attempts "
          "remaining to guess the number.")

def get_random_number():
    return random.randint(1, 100)


def get_guesses_remaining(difficulty):
    if difficulty == "easy":
        return EASY_GUESSES_REMAINING
    elif difficulty == "hard":
        return HARD_GUESSES_REMAINING


if __name__ == "__main__":
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    main()
