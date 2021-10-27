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


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there isn't enough {item}.")
            return False
        return True


def ask_for_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


is_on = True

while is_on:
    user_input = str(input("What would you like? (espresso/latte/cappuccino): "))
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print_report()
    else:
        drink = MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment = ask_for_coins()
