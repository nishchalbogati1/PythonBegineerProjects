# Hangman Game

A simple command-line Hangman game written in Python. The program randomly selects a word from a predefined list, and the player must guess the word one letter at a time.

## Features

- Randomly selects a word from a list.
- Displays the word as underscores.
- Allows the player to guess letters repeatedly.
- Keeps track of correctly guessed letters.
- Reveals all occurrences of a correctly guessed letter.
- Ends the game when the player successfully guesses the entire word.

## How It Works

1. A random word is selected from the word list.
2. The player is shown blank spaces representing each letter.
3. The player enters one letter per guess.
4. If the guessed letter is correct, it is revealed in the word.
5. Incorrect guesses do not affect the game (no lives system in this version).
6. The game continues until all letters have been guessed.

## Technologies Used

- Python 3
- `random` module

## Project Structure

```
hangman.py
README.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Clone this repository or download the project.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python hangman.py
```

## Example

```
Guess a letter: a
_a___

Guess a letter: e
_a_e_

Guess a letter: m
_ame_

Guess a letter: c
camel
You win!
```
