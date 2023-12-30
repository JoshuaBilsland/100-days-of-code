import art
import random
import game_data


def main():
    current_score = 0
    previous_account = get_account()
    winning = True
    while winning:
        # Pick a new account to compare against
        next_account_to_compare = get_account()
        while next_account_to_compare == previous_account:
            next_account_to_compare = get_account()
        print(previous_account)
        print(next_account_to_compare)
        choice = get_choice()


def get_choice():
    valid_input = False
    while not valid_input:
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        if user_input.upper() in ["A", "B"]:
            valid_input = True
        else:
            print("ERROR: Only enter 'A' or 'B'")
    return user_input


def get_account():
    return random.choice(game_data.data)


if __name__ == "__main__":
    print(art.logo)
    main()
