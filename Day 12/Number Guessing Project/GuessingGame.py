import random
import art

number = random.randint(1, 100)

def trys():
    difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        print("You have 10 attempts to guess the number.")
        return 10
    elif difficulty == "hard":
        print("You have 5 attempts to guess the number.")
        return 5
    else:
        print("Please choose a valid difficulty.")
        return trys()

print(art.logo)
print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100.")

no_of_trys = trys()
while no_of_trys > 0:
    guess = int(input("Make a guess: "))
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        break
    elif guess == number:
        print("You guessed the number!")
        break
    elif guess < number:
        print("Too low!")
        no_of_trys -= 1
        continue
    elif guess > number:
        print("Too high!")
        no_of_trys -= 1
        continue
if no_of_trys == 0:
    print("You have run out of guesses!")


