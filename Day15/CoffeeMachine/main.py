# Coffee Machine Project

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def ask_for_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .1
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01


while True:

    user_input = str(input("What would you like? (espresso/latte/cappuccino): "))

    # For maintainers of coffee machine to exit program
    if user_input == "off":
        break

    # TODO: 1. Print report of all coffee machine resources
    print_report()

    if user_input == "espresso":
        if resources["water"] < 50:
            print("Sorry, there isn't enough water to make this drink.")
        elif resources["coffee"] < 18:
            print("Sorry, there isn't enough coffee to make this drink.")
        else:
            ask_for_coins()

            user_money = quarters + dimes + nickles + pennies
            drink_cost = MENU["espresso"]["cost"]
            change = user_money - drink_cost

            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Here is {change} in change.")
                print(f"Here is your {user_input} ☕️ Enjoy!")

            current_money = resources["money"]
            current_money += drink_cost
            print(current_money)

# TODO: 2. Add code for latte