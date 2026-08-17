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

profit= 0

def report():
    print(f"Available resources:\n"
        f"Water: {resources['water']}\n"
        f"Milk: {resources['milk']}\n"
        f"Coffee: {resources['coffee']}\n"
        f"Money: ${profit}\n")

def menu_price():
    print("MENU ITEMS")
    for item in MENU:
        print(f"{item.title()}: ${MENU[item]["cost"]}")

def insert_coins():
    print("Please insert coins.")
    inserted_coins_value = int(input(f"How many quarters: ")) * 0.25
    inserted_coins_value += int(input(f"How many dimes: ")) * 0.10
    inserted_coins_value += int(input(f"How many nickels: ")) * 0.05
    inserted_coins_value += int(input(f"How many pennies: ")) * 0.01
    return inserted_coins_value

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}!")
            return False
    return True

def is_transaction_successful(coins_value, drink_cost):
    if coins_value >= drink_cost:
        change = round((coins_value - drink_cost),2)
        print(f"Here is ${change} in change!")
        global profit
        profit += drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def make_drink(choice, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {choice} ☕️ enjoy!")

print(art.logo)
is_on = True
while is_on:
    menu_price()
    choice = input("What would you like? (Espresso, Latte, Cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino" or choice == "off" or choice == "report":
        if  choice == "off":
            is_on = False
        elif choice == "report":
            report()
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                coins_value = insert_coins()
                if is_transaction_successful(coins_value, drink["cost"]):
                    make_drink(choice, drink["ingredients"])
    else:
        print("Sorry, that's not available. Please select the available menu item!")



