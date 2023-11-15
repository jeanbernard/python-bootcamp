import os
import platform
import auction_art

print(auction_art.logo)

bids = []
def add_bid(name, bid):
    bid = {
        "name": name,
        "bid": bid,
    }
    bids.append(bid)

def ask_for_bid():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    add_bid(name, bid)

def find_highest_bidder(bids):
    highest_bidder = ''
    high_bid = 0
    for bid in bids:
        if bid["bid"] > high_bid:
            high_bid = bid["bid"]
            highest_bidder = bid["name"]
    print(f"The winner is {highest_bidder} with a bid of ${high_bid}")

def clear_screen():
    os_sys = platform.system()
    if os_sys == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

still_bidding = True
while still_bidding:
    ask_for_bid()
    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bids == 'no':
        still_bidding = False
    else:
        clear_screen()
find_highest_bidder(bids)