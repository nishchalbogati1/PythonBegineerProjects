import random
import art
import game_data

def random_int():
    return random.randint(0,len(game_data.data)-1)

def game_over():
    print("Wrong!")
    print(f"Game Over! Your final score is: {score}")

score = 0
choice_a = random_int()
choice_b = random_int()

while choice_a == choice_b:
    choice_b = random_int()

print(art.logo)
while True:
    print(
        f"Compare A: {game_data.data[choice_a]['name']}, "
        f"a {game_data.data[choice_a]['description']}, "
        f"from {game_data.data[choice_a]['country']}"
    )
    print(art.vs)
    print(
        f"Against B: {game_data.data[choice_b]['name']}, "
        f"a {game_data.data[choice_b]['description']}, "
        f"from {game_data.data[choice_b]['country']}"
    )
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    a_follower = game_data.data[choice_a]['follower_count']
    b_follower = game_data.data[choice_b]['follower_count']
    if user_choice == "A":
        if a_follower > b_follower:
            score += 1
            print(f"Correct! Current score: {score}")
            choice_b = random_int()
            while choice_a == choice_b:
                choice_b = random_int()
        else:
            game_over()
            break
    elif user_choice == "B":
        if a_follower < b_follower:
            score += 1
            print(f"Correct! Current score: {score}")
            choice_a = choice_b
            choice_b = random_int()
            while choice_a == choice_b:
                choice_b = random_int()
        else:
            game_over()
            break
    else:
        print("Please enter either 'A' or 'B': ")
        continue

