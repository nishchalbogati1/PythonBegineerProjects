import random

import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Deals a random card from the deck."""
    return random.choice(cards)

def calculate_score(card):
    """Calculates the score of the players by adding the value of the cards."""
    score = sum(card)
    if score == 21 and len(card) == 2:
        return 0
    while score > 21 and 11 in card:
            card.remove(11)
            card.append(1)
            score = sum(card)
    return score

def final_score(user_cards, computer_cards,user_score,computer_score):
    """Displays the final score of the players."""
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")

def blackjack():
    """Contains the main working logic for Blackjack"""
    user_cards = []
    computer_cards = []
    choice = input("Do you want to start a hand of blackjack? Type 'y' for yes and 'n' for no: ").lower()
    if choice == 'y':
        print(art.logo)

        for _ in range(2):
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
                final_score(user_cards,computer_cards,user_score,computer_score)
                print("You bust! Computer wins!")
                return
            elif user_score == 21:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                break
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                extra_cards = input("\n Do you want another card? Type 'y' for yes and 'n' to pass: ").lower()
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        final_score(user_cards, computer_cards, user_score, computer_score)
        if computer_score > 21:
            print("Computer busts! You win!")
        elif user_score > computer_score:
            print("You win!")
        elif computer_score > user_score:
            print("Computer wins!")
        else:
            print("It's a draw!")
    elif choice == 'n':
        exit()
    else:
        print("Please enter either 'y' or 'n'.")
        print("\n" * 2)
        blackjack()

while True:
    blackjack()
    again = input("Do you want to play again? Type 'y' for yes and 'n' for no: ")
    if again != 'y':
        break
    print("\n" * 20)