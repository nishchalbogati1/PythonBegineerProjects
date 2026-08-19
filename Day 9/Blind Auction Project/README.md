# Blind Auction

A simple Python **Blind Auction** program where multiple bidders can enter their names and bids. The program keeps all bids hidden from previous bidders and determines the winner based on the highest bid.

## How It Works

1. The program displays an auction logo.
2. Each bidder enters:

   * Their name
   * Their bid amount
3. The program asks whether there is another bidder.
4. If there is another bidder, the screen is cleared before the next bidder enters their bid.
5. Once all bidders have entered their bids, the program compares all bids.
6. The bidder with the highest bid is declared the winner.

## Example

```text
What is your name? John
What is you bid? $150
Is there another bidder? (y/n): y

What is your name? Sarah
What is you bid? $200
Is there another bidder? (y/n): y

What is your name? Mike
What is you bid? $175
Is there another bidder? (y/n): n

The winner is Sarah with a bid of $200.0!
```

## Concepts Used

This project demonstrates several Python concepts:

* Dictionaries
* `while` loops
* `for` loops
* `if/else` statements
* User input with `input()`
* Type conversion using `float()`
* Dictionary key-value pairs
* Comparing values to find the maximum
* `continue` and `break`
* Importing and using a module

## Code Structure

Bids are stored in a dictionary:

```python
auction = {}
```

Each bidder's name is used as the key and their bid as the value:

```python
auction[username] = bid_price
```

For example:

```python
{
    "John": 150.0,
    "Sarah": 200.0,
    "Mike": 175.0
}
```

The program then loops through the dictionary and keeps track of the highest bid:

```python
for key in auction:
    if auction[key] > winning_bid:
        winning_bid = auction[key]
        winning_key = key
```

## Requirements

* Python 3.x
* The `art` module

Install the required module if necessary:

```bash
pip install art
```

## Running the Program

Run the Python file from your terminal:

```bash
python main.py
```

## Learning Objective

This project is designed to practice using **dictionaries, loops, conditions, user input, and finding the highest value in a collection** in Python.
