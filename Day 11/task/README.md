# 🃏 Blackjack Game

A simple command-line Blackjack game built with Python. This project simulates a game of Blackjack between the player and the computer, following the core rules of the game.

## Features

* Deal two random cards to both the player and the computer.
* Detect a **natural Blackjack** (Ace + 10-value card).
* Allow the player to draw additional cards (Hit) or end their turn (Stand).
* Automatically convert an Ace from **11** to **1** when necessary to prevent a bust.
* Dealer follows standard Blackjack rules by drawing cards until reaching a score of at least **17**.
* Detect player and dealer busts.
* Compare final scores to determine the winner.
* Option to start a new game after the current game ends.

## Technologies Used

* Python 3
* `random` module
* Custom ASCII art module (`art.py`)

## Project Structure

```text
.
├── blackjack.py      # Main game logic
├── art.py            # ASCII art logo
└── README.md
```

## How to Run

1. Clone this repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd <repository-folder>
```

3. Run the program.

```bash
python blackjack.py
```

## Game Rules

* Both the player and the dealer receive two cards at the beginning of the game.
* Number cards are worth their face value.
* Face cards (Jack, Queen, King) are worth **10**.
* An Ace is worth **11**, but it is automatically changed to **1** if it would cause the hand to bust.
* A natural Blackjack is an Ace and a 10-value card dealt as the initial two cards.
* The player may continue drawing cards until they choose to stand or their score exceeds 21.
* The dealer must continue drawing cards until their score is **17 or higher**.
* If either player exceeds 21, they bust and lose the hand.
* If neither player busts, the higher score wins. Equal scores result in a draw.

## Learning Outcomes

This project helped practice:

* Writing and calling functions
* Using loops (`while` and `for`)
* Conditional statements (`if`, `elif`, `else`)
* Working with lists and list methods
* Returning values from functions
* Implementing game logic
* Refactoring repeated code into reusable functions
* Organizing a Python program into smaller, manageable components

## Future Improvements

Some possible enhancements include:

* Improve input validation.
* Display cards using ASCII art.
* Keep track of wins, losses, and draws.
* Refactor the code into additional helper functions for improved readability.

