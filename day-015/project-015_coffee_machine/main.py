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
            resource_check = check_resources(resources, "espresso")
            if resource_check is None:
                print("Please insert coins.")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                coin_total = get_coin_total(
                    [quarters, dimes, nickles, pennies])
                coin_check = check_amount(menu.MENU["espresso"]["cost"],
                                          coin_total)
                resources["money"][0] += coin_check[0]
                print(coin_check[1])
                if coin_check[0] != 0:
                    for ingredient in menu.MENU["espresso"]["ingredients"]:
                        resources[ingredient][0] -= menu.MENU["espresso"][
                            "ingredients"][ingredient]
            else:
                print(resource_check)

        elif user_choice == "latte":
            resource_check = check_resources(resources, "latte")
            if resource_check is None:
                print("Please insert coins.")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                coin_total = get_coin_total(
                    [quarters, dimes, nickles, pennies])
                coin_check = check_amount(menu.MENU["latte"]["cost"],
                                          coin_total)
                resources["money"][0] += coin_check[0]
                print(coin_check[1])
                if coin_check[0] != 0:
                    for ingredient in menu.MENU["latte"]["ingredients"]:
                        resources[ingredient][0] -= menu.MENU["latte"][
                            "ingredients"][ingredient]
            else:
                print(resource_check)

        elif user_choice == "cappuccino":
            resource_check = check_resources(resources, "cappuccino")
            if resource_check is None:
                print("Please insert coins.")
                quarters = float(input("How many quarters?: "))
                dimes = float(input("How many dimes?: "))
                nickles = float(input("How many nickles?: "))
                pennies = float(input("How many pennies?: "))
                coin_total = get_coin_total(
                    [quarters, dimes, nickles, pennies])
                coin_check = check_amount(menu.MENU["cappuccino"]["cost"],
                                          coin_total)
                resources["money"][0] += coin_check[0]
                print(coin_check[1])
                if coin_check[0] != 0:
                    for ingredient in menu.MENU["cappuccino"]["ingredients"]:
                        resources[ingredient][0] -= menu.MENU["cappuccino"][
                            "ingredients"][ingredient]
            else:
                print(resource_check)

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


def check_amount(desired_amount, coin_total):
    if coin_total > desired_amount:
        change = round(coin_total - desired_amount, 2)
        string = f"Here is ${change} in change."
        return coin_total, string
    elif coin_total < desired_amount:
        string = "Sorry that's not enough money. Money refunded."
        return 0, string
    else:
        string = "That is enough money."
        return coin_total, string


if __name__ == "__main__":
    main()
