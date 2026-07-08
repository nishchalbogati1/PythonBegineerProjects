import random
import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over = False
lives = 6
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        if letter == guess:
                display += letter
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
                display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print("The letter is not in the word")
        print(stages[lives])
        print(f'You have {lives} left.')
        if lives == 0:
            game_over = True
            print("You lose!")
    if "_" not in display:
        game_over = True
        print("You win!")
