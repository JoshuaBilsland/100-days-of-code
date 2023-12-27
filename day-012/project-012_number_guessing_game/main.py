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

easy_guesses_remaining = 5
hard_guesses_remaining = 10


def main():
    user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    print(f"You have {get_guesses_remaining(user_difficulty)} attempts "
          "remaining to guess the number.")

    guessed_correctly = False
    random_number = get_random_number()
    while get_guesses_remaining(user_difficulty) > 0 and not guessed_correctly:
        user_guess = int(input("Make a guess: "))
        if user_guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            guessed_correctly = True
        else:
            if user_guess > random_number:
                print("Too high.")
                print("Guess again.")
            elif user_guess < random_number:
                print("Too low.")
                print("Guess again.")

            if user_difficulty == "easy":
                global easy_guesses_remaining
                easy_guesses_remaining -= 1
            elif user_difficulty == "hard":
                global hard_guesses_remaining
                hard_guesses_remaining -= 1

    if get_guesses_remaining(user_difficulty) == 0:
        print("You've run out of guesses, you lose.")


def get_random_number():
    return random.randint(1, 100)


def get_guesses_remaining(difficulty):
    if difficulty == "easy":
        return easy_guesses_remaining
    elif difficulty == "hard":
        return hard_guesses_remaining


if __name__ == "__main__":
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    main()
