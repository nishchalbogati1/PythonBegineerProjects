import random

import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)
def calculate_score(card):
    score = sum(card)
    if score == 21 and len(card) == 2:
        return 0
    while score > 21 and 11 in card:
            card.remove(11)
            card.append(1)
            score = sum(card)
    return score
def blackjack():
    user_cards = []
    computer_cards = []
    choice = input("Do you want to start a hand of blackjack? Type 'y' for yes and 'n' for no: ").lower()
    if choice == 'y':
        print(art.logo)

        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        if user_score == 0 and computer_score == 0:
            print("Both have Blackjack! It's a draw.")
            return
        elif user_score == 0:
            print("Blackjack! You win!")
            return
        elif computer_score == 0:
            print("Blackjack! Computer wins!")
            return
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        extra_cards = input("Do you want another card? Type 'y' for yes and 'n' to pass: ").lower()
        while extra_cards == "y":
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)

            if user_score > 21:
                print("You bust! Computer wins!")
                return
            elif user_score == 21:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                break
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                extra_cards = input("Do you want another card? Type 'y' for yes and 'n' to pass: ").lower()
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
        if computer_score > 21:
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
            print("Computer busts! You win!")
        elif user_score > computer_score:
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
            print("You win!")
        elif computer_score > user_score:
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
            print("Computer wins!")
        else:
            print(f"Your final cards: {user_cards}, final score: {user_score}")
            print(f"Computer's final cards: {computer_cards}, current score: {computer_score}")
            print("It's a draw!")


blackjack()
new_game = input("Do you want to start a new hand of blackjack? Type 'y' for yes and 'n' for no: ").lower()
if new_game == 'y':
    blackjack()

else:
    exit()
# print(f"Your cards: {user_cards}, current score: {user_score}")
# print(f"Computer's first card: {computer_cards[0]}")
# choice = input("Do you want to start a hand of blackjack. Type 'y' for yes or 'n' for no: ").lower()