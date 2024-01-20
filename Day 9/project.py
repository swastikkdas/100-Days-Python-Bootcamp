import clear
from art import logo


print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} and the bid is ${bid_amount}")

while not bidding_finished:
    name = input("Enter Your Name: ")
    price = int(input("Enter Your Bid: $"))
    bids[name] = price
    should_continue= input("Are there any other Bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear.clear()

