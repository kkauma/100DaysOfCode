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

# TODO: 1. Print report of all coffee machine resources

user_input = str(input("What would you like? (espresso/latte/cappuccino): "))

if user_input == "report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

elif user_input == "espresso":
    if resources["water"] < 50:
        print("Sorry, there isn't enough water to make this drink.")
    elif resources["coffee"] < 18:
        print("Sorry, there isn't enough coffee to make this drink.")
    else:
        print("Espresso coming right up!")
