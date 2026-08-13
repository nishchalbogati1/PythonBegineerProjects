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
money = 0
while True:
    choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if choice == "report" or choice == "off":
        if choice == "report":
            # print the ingredients details in this part
            print(f"Available resources:\n"
                  f"Water: {resources['water']}\n"
                  f"Milk: {resources['milk']}\n"
                  f"Coffee: {resources['coffee']}\n"
                  f"Money: ${money}\n")
        elif choice == "off":
            break
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if choice == "espresso":
            if (
                    resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
            ):
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                money += MENU["espresso"]["cost"]
            else:
                print("Sorry, there is not enough resource for espresso.")
        elif choice == "latte":
            if (
                    resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
            ):
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                money += MENU["latte"]["cost"]
            else:
                print("Sorry, there is not enough resource for espresso.")
        elif choice == "cappuccino":
            if (
                    resources["water"] >= MENU["espresso"]["ingredients"]["water"]
                    and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]
            ):
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                money += MENU["cappuccino"]["cost"]
            else:
                print("Sorry, there is not enough resource for espresso.")
        else:
            print("Sorry, that's not available. Please select the available menu item!")
            continue



