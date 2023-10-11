from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from util import get


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True
while is_on:
    input_user = get("What would you like? (espresso/latte/cappuccino): ", str).lower()
    is_on = False if input_user == "off" else True
    if input_user == "report":
        coffee_maker.report()
    else:
        coffee = menu.find_drink(input_user)
        if coffee is not None:
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    coffee_maker.make_coffee(coffee)




