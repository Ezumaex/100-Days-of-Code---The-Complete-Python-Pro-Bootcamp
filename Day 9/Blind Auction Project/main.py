# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

bidding_data = {} # Bidding dictionary, contains user's name and price
bidding_active = True

def find_highest_bid(bids):
    highest_bid = 0
    winner = ""

    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


while bidding_active:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))

    bidding_data[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue.lower() == "yes":
        print("\n" * 100)
    elif should_continue.lower() == "no":
        bidding_active = False
        find_highest_bid(bidding_data)



