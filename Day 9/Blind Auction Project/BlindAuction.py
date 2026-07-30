# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
winning_bid = 0
winning_key = ""
auction = {}
while True:
    username = input("What is your name? ")
    bid_price = float(input("What is you bid? $"))
    auction[username]= bid_price
    choice = input("Is there another bidder? (y/n): ").lower()
    if choice == "y":
        print("\n" * 20)
        continue
    else:
        break
# print(auction)
for key in auction:
    if auction[key] > winning_bid:
        winning_bid = auction[key]
        winning_key = key
    else:
        continue
print(f"The winner is {winning_key} with a bid of ${auction[winning_key]}!")


