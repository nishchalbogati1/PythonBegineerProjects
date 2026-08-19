# Caesar Cipher

A simple Python program that **encrypts and decrypts messages** using the Caesar Cipher.

## How It Works

The program shifts each letter in the message by a number chosen by the user.

For example, with a shift of `3`:

```text
a → d
b → e
c → f
```

So:

```text
hello
```

becomes:

```text
khoor
```

The program can also decode the message by shifting the letters back.

## Features

* Encode a message
* Decode a message
* Choose your own shift number
* Keeps spaces and special characters unchanged
* Allows you to run the program again

## Example

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello
Type the shift number:
3

Here is the encoded result: khoor
```

## Concepts Used

* Functions
* Lists
* `for` and `while` loops
* `if` statements
* User input
* String manipulation
* `break` and `continue`
* Modulo operator

## Requirements

* Python 3.x
* `art` module

Install the module with:

```bash
pip install art
```

## Running the Program

```bash
python main.py
```

## Learning Objective

This project was created to practice **Python functions, loops, lists, strings, and basic encryption logic**.
