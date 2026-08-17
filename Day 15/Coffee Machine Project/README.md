# ☕ Coffee Machine

A simple Python coffee machine program that allows users to order espresso, latte, or cappuccino.

## Features

- Displays available coffee menu items and their prices.
- Accepts coins:
  - Quarters
  - Dimes
  - Nickels
  - Pennies
- Calculates the total amount inserted.
- Checks whether the user has inserted enough money.
- Calculates and returns change.
- Checks whether enough ingredients are available.
- Deducts ingredients after a successful purchase.
- Tracks the total money earned.
- Provides a `report` command to display available resources and money earned.
- Provides an `off` command to turn off the machine.
- Handles invalid menu selections.

## Menu

| Drink | Price |
|---|---:|
| Espresso | $1.50 |
| Latte | $2.50 |
| Cappuccino | $3.00 |

## Resources

The machine starts with:

- Water: 300 ml
- Milk: 200 ml
- Coffee: 100 g

## How to Run

Make sure Python is installed, then run:

```bash
python main.py