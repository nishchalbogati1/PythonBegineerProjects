import math

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
}
coins = {
    "quarters": 0,
    "dimes": 0,
    "nickels": 0,
    "pennies": 0,
}
values = {
    "v_quarters": 0.25,
    "v_dimes": 0.10,
    "v_nickels": 0.05,
    "v_pennies": 0.01,
}

money = 0
inserted_coins_value = 0

# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def report_off(choice):
    if choice == "report" or choice == "off":
        if choice == "report":
            print(f"Available resources:\n"
                  f"Water: {resources['water']}\n"
                  f"Milk: {resources['milk']}\n"
                  f"Coffee: {resources['coffee']}\n"
                  f"Money: ${money}\n")
        elif choice == "off":
            return

def menu_price():
    print("MENU ITEMS")
    for key in MENU:
        print(f"{key.title()}: ${MENU[key]["cost"]}")

while True:
    menu_price()
    choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    report_off(choice)
    print("Please insert coins.")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        for key in coins:
            coins[key] = int(input(f"How many {key}: "))
        print(coins)
        for coin in coins:
            for value in values:
                inserted_coins_value += round((coins[coin] * values[value]),2)
        print(f"Inserted coins total: {inserted_coins_value:.2f}")
        if choice == "espresso":
            if (
                    resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
            ):
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                money += MENU["espresso"]["cost"]
            else:
                if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                    print(f"Sorry, there is not enough Water for espresso.")
                elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                    print(f"Sorry, there is not enough Coffee for espresso.")
                break
        elif choice == "latte":
            if (
                    resources["water"] >= MENU["latte"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]
                    and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]

            ):
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                money += MENU["latte"]["cost"]
            else:
                if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                    print(f"Sorry, there is not enough Water for latte.")
                elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                    print(f"Sorry, there is not enough Coffee for latte.")
                elif resources["Milk"] < MENU["latte"]["ingredients"]["milk"]:
                    print(f"Sorry, there is not enough Milk for latte.")
                break
        elif choice == "cappuccino":
            if (
                    resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
                    and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]
            ):
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                money += MENU["cappuccino"]["cost"]
            else:
                if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                    print(f"Sorry, there is not enough Water for cappuccino.")
                elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                    print(f"Sorry, there is not enough Coffee for cappuccino.")
                elif resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                    print(f"Sorry, there is not enough Milk for cappuccino.")
                break
        else:
            print("Sorry, that's not available. Please select the available menu item!")
            continue



