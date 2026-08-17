import math
import art
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
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

money = 0

# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def report():
    print(f"Available resources:\n"
        f"Water: {resources['water']}\n"
        f"Milk: {resources['milk']}\n"
        f"Coffee: {resources['coffee']}\n"
        f"Money: ${money}\n")

def menu_price():
    print("MENU ITEMS")
    for key in MENU:
        print(f"{key.title()}: ${MENU[key]["cost"]}")

print(art.logo)

while True:
    menu_price()
    choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if  choice == "off":
        break
    elif choice == "report":
        report()
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        inserted_coins_value = 0
        if choice == "espresso":
            print("Please insert coins.")
            for key in coins:
                coins[key] = int(input(f"How many {key}: "))
            print(coins)
            for coin in coins:
                inserted_coins_value += coins[coin] * values[coin]
            print(f"Inserted coins total: {inserted_coins_value}")
            if inserted_coins_value < MENU["espresso"]["cost"]:
                print("Insufficient funds! Money refunded!")
                continue
            else:
                if (
                        resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                        and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
                ):
                    resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                    money += MENU["espresso"]["cost"]
                    print(f"Here is ${inserted_coins_value - MENU["espresso"]["cost"]} in change!")
                    print("Here is you espresso ☕️ enjoy!")
                else:
                    if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
                        print(f"Sorry, there is not enough Water for espresso.")
                    elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
                        print(f"Sorry, there is not enough Coffee for espresso.")
                    break
        elif choice == "latte":
            print("Please insert coins.")
            for key in coins:
                coins[key] = int(input(f"How many {key}: "))
            print(coins)
            for coin in coins:
                inserted_coins_value += coins[coin] * values[coin]
            print(f"Inserted coins total: {inserted_coins_value}")
            if inserted_coins_value < MENU["latte"]["cost"]:
                print("Insufficient funds! Money refunded!")
                continue
            else:
                if(
                    resources["water"] >= MENU["latte"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]
                    and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]

                ):
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    money += MENU["latte"]["cost"]
                    print(f"Here is ${inserted_coins_value - MENU["latte"]["cost"]} in change!")
                    print("Here is you latte ☕️ enjoy!")
                else:
                    if resources["water"] < MENU["latte"]["ingredients"]["water"]:
                        print(f"Sorry, there is not enough Water for latte.")
                    elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
                        print(f"Sorry, there is not enough Coffee for latte.")
                    elif resources["Milk"] < MENU["latte"]["ingredients"]["milk"]:
                        print(f"Sorry, there is not enough Milk for latte.")
                    break
        elif choice == "cappuccino":
            print("Please insert coins.")
            for key in coins:
                coins[key] = int(input(f"How many {key}: "))
            print(coins)
            for coin in coins:
                inserted_coins_value += coins[coin] * values[coin]
            print(f"Inserted coins total: {inserted_coins_value}")
            if inserted_coins_value < MENU["cappuccino"]["cost"]:
                print("Insufficient funds! Money refunded!")
                continue
            else:
                if (
                        resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]
                        and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]
                        and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]
                ):
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    money += MENU["cappuccino"]["cost"]
                    print(f"Here is ${inserted_coins_value - MENU["cappuccino"]["cost"]} in change!")
                    print("Here is you cappuccino ☕️ enjoy!")
                else:
                    if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
                        print(f"Sorry, there is not enough Water for cappuccino.")
                    elif resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
                        print(f"Sorry, there is not enough Coffee for cappuccino.")
                    elif resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
                        print(f"Sorry, there is not enough Milk for cappuccino.")
                    break
    else:
        print("Sorry, that's not available. Please select the available menu item!")
        continue



