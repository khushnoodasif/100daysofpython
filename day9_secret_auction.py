from day9_secret_auction_files import logo
print(logo)

import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
bids = {}

def highest_bidder(bidding_list):
	highest_bid = 0
	winner = ""
	for bidder in bidding_list:
		bid_amount = bidding_list[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")

bids_finished = False
while not bids_finished:
	name = input("What is your name? \n")
	bid = int(input("What is your bid price? ($) \n"))
	bids[name] = bid
	other_bid = input("Are there other bidders? (yes/no)\n")
	if other_bid == "no":
		bids_finished = True
		highest_bidder(bids)
	elif other_bid == "yes":
		clear_screen()
