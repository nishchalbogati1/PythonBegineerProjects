import random
import art
import game_data

def random_int():
    return random.randint(0,len(game_data.data)-1)

def display_account(label,account):
    print(
        f"Compare {label}: {game_data.data[account]['name']}, "
        f"a {game_data.data[account]['description']}, "
        f"from {game_data.data[account]['country']}, "
    )

def game_over():
    print("Wrong!")
    print(f"Game Over! Your final score is: {score}")

score = 0
choice1 = random_int()
choice2 = random_int()

while choice1 == choice2:
    choice2 = random_int()

print(art.logo)
while True:
    display_account("A",choice1)
    print(art.vs)
    display_account("B",choice2)
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_follower = game_data.data[choice1]['follower_count']
    b_follower = game_data.data[choice2]['follower_count']
    if user_choice == "A":
        if a_follower > b_follower:
            score += 1
            print(f"Correct! Current score: {score}")
            choice2 = random_int()
            while choice1 == choice2:
                choice2 = random_int()
        else:
            game_over()
            break
    elif user_choice == "B":
        if a_follower < b_follower:
            score += 1
            print(f"Correct! Current score: {score}")
            choice1 = choice2
            choice2 = random_int()
            while choice1 == choice2:
                choice2 = random_int()
        else:
            game_over()
            break
    else:
        print("Please enter either 'A' or 'B': ")
        continue

