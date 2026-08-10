import random
import art
import game_data

score = 0

print(art.logo)

# Generate a random number
choice1 = random.randint(0,len(game_data.data)-1)
choice2 = random.randint(0,len(game_data.data)-1)

# Use that random integer to display the content of the dictionary inside that list and a vs logo
print(f"Compare A:{game_data.data[choice1]["name"]}, a {game_data.data[choice1]['description']}, from {game_data.data[choice1]['country']}")
print(art.vs)
print(f"Compare B:{game_data.data[choice2]["name"]}, a {game_data.data[choice2]['description']}, from {game_data.data[choice2]['country']}")

# Compare the follower count of the two choice and display the result to the user
user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
if game_data.data[choice1]['follower_count'] > game_data.data[choice2]['follower_count']:
    if user_choice == "A":
        print("Correct!")
        score += 1
        print(f"Your score: {score}")

    else:
        print("Wrong!")
elif game_data.data[choice1]['follower_count'] < game_data.data[choice2]['follower_count']:
    if user_choice == "B":
        print("Correct!")
        score += 1
        print(f"Your score: {score}")
    else:
        print("Wrong!")