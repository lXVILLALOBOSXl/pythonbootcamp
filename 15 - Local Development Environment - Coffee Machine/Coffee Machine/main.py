from data import MENU, resources
from util import get


def report():
    for key, value in resources.items():
        print(f'{key.capitalize()}: {value}')


def get_money():
    total = 0
    total += get("how many quarters?: ", int) * 0.25
    total += get("how many dimes?: ", int) * 0.10
    total += get("how many nickles?: ", int) * 0.05
    total += get("how many pennies?: ", int) * 0.01
    return total


def find_key(coffee, menu):
    if coffee in menu:
        return MENU[coffee]


def enough_money(coffee, money):
    return money >= coffee["cost"]


def enough_resources(coffee):
    if coffee["ingredients"]["water"] > resources["water"]:
        print(f"Sorry, there's is no water enough.")
        return False
    elif coffee["ingredients"]["milk"] > resources["milk"]:
        print(f"Sorry, there's is no milk enough.")
        return False
    elif coffee["ingredients"]["coffee"] > resources["coffee"]:
        print(f"Sorry, there's is no coffer enough.")
        return False
    else:
        return True


def get_change(coffee, money):
    return money - coffee["cost"]


def update_resources(coffee):
    resources["water"] -= coffee["ingredients"]["water"]
    resources["milk"] -= coffee["ingredients"]["milk"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]
    resources["gains"] += coffee["cost"]


def make_coffee(coffee, name):
    update_resources(coffee)
    print(f"Here is your {name} ☕️. Enjoy!")


def __main__():
    on = True
    while on:
        user_input = get(" What would you like? (espresso/latte/cappuccino): ", str)
        if user_input == "report":
            report()
        elif user_input == "off":
            on = False
        else:
            coffee = find_key(user_input, MENU)
            if coffee is not None:
                money = get_money()
                if enough_money(coffee, money):
                    if enough_resources(coffee):
                        change = get_change(coffee, money)
                        if round(change) > 0:
                            print(f"Here is ${change} in change.")
                        make_coffee(coffee, user_input)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"{user_input} not founded, try again.")


__main__()
