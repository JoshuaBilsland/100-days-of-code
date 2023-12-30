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

        print(f"Current score: {current_score}")
        print(f"Compare A: {previous_account["name"]}, "
              f"a {previous_account["description"]}, "
              f"from {previous_account["country"]}")
        print(art.vs)
        print()
        print(f"Compare B: {next_account_to_compare["name"]}, "
              f"a {next_account_to_compare["description"]}, "
              f"from {next_account_to_compare["country"]}")

        choice = get_choice()
        if (previous_account["follower_count"]
            > next_account_to_compare["follower_count"]):
            if choice == "A":
                current_score += 1
            else:
                winning = False
        else:
            if choice == "B":
                current_score += 1
            else:
                winning = False
        previous_account = next_account_to_compare
    print(f"Sorry, that's wrong. Final score: {current_score}")


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
