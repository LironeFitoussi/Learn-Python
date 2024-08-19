MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def ask_user():
    while True:
        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): "
        ).lower()
        if user_choice in MENU or user_choice in ["off", "report"]:
            return user_choice
        print("Invalid input. Please try again.")


def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in coins:
        while True:
            try:
                count = int(input(f"How many {coin}?: "))
                if count < 0:
                    raise ValueError
                total += count * coins[coin]
                break
            except ValueError:
                print("Please enter a valid non-negative integer.")
    return total


def check_resources(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def make_coffee(drink):
    for ingredient, amount in MENU[drink]["ingredients"].items():
        resources[ingredient] -= amount
    print(f"Here is your {drink}. Enjoy!")


def get_coffee():
    global another_coffee
    while True:
        user_choice = ask_user()
        if user_choice == "report":
            print_resources()
        elif user_choice == "off":
            another_coffee = False
            print("Goodbye!")
            return
        elif user_choice in MENU:
            if check_resources(user_choice):
                drink = MENU[user_choice]
                print(f"You have chosen {user_choice}. It costs ${drink['cost']:.2f}")
                user_money = process_coins()
                if user_money < drink["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    resources["money"] += drink["cost"]
                    change = user_money - drink["cost"]
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    make_coffee(user_choice)

            user_decision = input("Do you want another coffee? (yes/no): ").lower()
            if user_decision != "yes":
                another_coffee = False
                print("Goodbye!")
                return
        else:
            print("Invalid choice. Please try again.")


another_coffee = True

while another_coffee:
    get_coffee()
