import menu


def main():
    on = True
    while on:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "espresso":
            print()
        elif user_choice == "latte":
            print()
        elif user_choice == "cappuccino":
            print()
        elif user_choice == "report":
            print()
        elif user_choice == "off":
            print()
        else:
            print("ERROR: Invalid choice")


if __name__ == "__main__":
    main()
