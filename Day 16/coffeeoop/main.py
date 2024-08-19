from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_mahchine = MoneyMachine()
menu = Menu()
is_on = True

money_mahchine.report()
coffee_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_mahchine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money_mahchine.make_payment(
            drink.cost
        ):
            coffee_machine.make_coffee(drink)
