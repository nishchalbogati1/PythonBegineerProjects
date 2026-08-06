# Number Guessing Game

A simple Python number guessing game.

## Description

The program chooses a random number between **1 and 100**. The player selects a difficulty level and tries to guess the number within the given number of attempts.

- **Easy:** 10 attempts
- **Hard:** 5 attempts

After each guess, the program tells the player whether the guess is **too high** or **too low**.

## Requirements

- Python 3

## How to Run

Run the program using:

```bash
python main.py
```

## Example

```text
Welcome to the Guessing Game!
I am thinking of a number between 1 and 100.

Choose a difficulty: 'easy' or 'hard': easy
You have 10 attempts to guess the number.

Make a guess: 50
Too low!

Make a guess: 75
Too high!
```

## Features

- Random number generation
- Difficulty selection
- Input validation for difficulty
- High/low hints after each guess
