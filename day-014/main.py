import art


def main():
    current_score = 0
    winning = True
    while winning:
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


if __name__ == "__main__":
    print(art.logo)
    main()
