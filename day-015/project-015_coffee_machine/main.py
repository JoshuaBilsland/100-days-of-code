import menu


def main():
    # 'a' stands for append the symbol, 'p' stands for prepend the symbol
    resources = {
        "Water": [300, "ml", "a"],
        "Milk": [200, "ml", "a"],
        "Coffee": [100, "g", "a"],
        "Money": [0, "$", "p"]
    }

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
            report(resources)
        elif user_choice == "off":
            on = False
        else:
            print("ERROR: Invalid choice")


def report(resources_dict):
    for key in resources_dict:
        if resources_dict[key][2] == "a":
            print(f"{key}: {resources_dict[key][0]}{resources_dict[key][1]}")
        elif resources_dict[key][2] == "p":
            print(f"{key}: {resources_dict[key][1]}{resources_dict[key][0]}")


if __name__ == "__main__":
    main()
