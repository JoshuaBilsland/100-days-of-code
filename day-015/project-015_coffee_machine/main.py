import menu


def main():
    # 'a' stands for append the symbol, 'p' stands for prepend the symbol
    resources = {
        "water": [300, "ml", "a"],
        "milk": [200, "ml", "a"],
        "coffee": [100, "g", "a"],
        "money": [0, "$", "p"]
    }

    on = True
    while on:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "espresso":
            print(check_resources(resources, user_choice))
            print(get_coin_total([1,2,1,2]))
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
            print(f"{key.capitalize()}: "
                  f"{resources_dict[key][0]}{resources_dict[key][1]}")
        elif resources_dict[key][2] == "p":
            print(f"{key.capitalize()}: "
                  f"{resources_dict[key][1]}{resources_dict[key][0]}")


def check_resources(resources, coffee_wanted):
    for ingredient in menu.MENU[coffee_wanted]["ingredients"]:
        if (resources[ingredient][0]
                < menu.MENU[coffee_wanted]["ingredients"][ingredient]):
            return f"Sorry, there is not enough {ingredient}."
    return None  # No lack of resources


def get_coin_total(coins_inserted):
    coin_total = 0
    for index, amount in enumerate(coins_inserted):
        if index == 0:
            amount *= 0.25
        elif index == 1:
            amount *= 0.10
        elif index == 2:
            amount *= 0.05
        elif index == 3:
            amount *= 0.01
        coin_total += amount
    return coin_total


if __name__ == "__main__":
    main()
