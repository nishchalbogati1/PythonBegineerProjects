import random
import art

number = random.randint(1, 100)

def trys():
    while True:
        difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            print("You have 10 attempts to guess the number.")
            return 10
        elif difficulty == "hard":
            print("You have 5 attempts to guess the number.")
            return 5
        else:
            print("Please choose a valid difficulty.")

def attempts_left(attempts):
    print(f"You have {attempts} attempts left to guess the number.")


print(art.logo)
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

attempts = trys()
while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        break
    elif guess == number:
        print("You guessed the number!")
        break
    elif guess < number:
        print("Too low!")
        attempts -= 1
        attempts_left(attempts)
        continue
    elif guess > number:
        print("Too high!")
        attempts -= 1
        attempts_left(attempts)
        continue
if attempts == 0:
    print("You have run out of guesses!")


