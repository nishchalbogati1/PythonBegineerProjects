import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose?Type 0 for 'Rock', 1 for 'Scissors', 2 for 'Paper'.\n"))
if user_choice not in [0, 1, 2]:
    print("Please choose between 0, 1 and 2.")
    exit()
computer_choice = random.randint(0,2)
options = [rock, scissors, paper]
print("Your choice:")
print(options[user_choice])
print("Computer choice:")
print(options[computer_choice])
if options[user_choice] == options[computer_choice]:
    print("It's a tie!")
    exit()
elif options[user_choice] == paper:
    if options[computer_choice] == rock:
        print("You won!")
        exit()
    else:
        print("You lost!")
        exit()
elif options[user_choice] == scissors:
    if options[computer_choice] == paper:
        print("You won!")
        exit()
    else:
        print("You lost!")
        exit()
elif options[user_choice] == rock:
    if options[computer_choice] == scissors:
        print("You won!")
        exit()
    else:
        print("You lost!")
        exit()
# if user_choice != 0 and user_choice != 1 and user_choice != 2:
else:
    print("Please choose between rock, paper and scissors.")
