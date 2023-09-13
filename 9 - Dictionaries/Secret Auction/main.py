from art import logo

print(logo + "\nWelcome to the secret auction program.")

import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


are_remaining_bidders = True
bidders = {}

while are_remaining_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    bidders[name] = bid
    
    if input("Are there any other bidders? Type 'yes' or 'no' ").lower() == "yes":
        are_remaining_bidders = True
        clear_console()
    else:
        are_remaining_bidders = False

clear_console()

highest_bidder = ""
highest_bidd = 0

for bidder in bidders:
    if bidders[bidder] > highest_bidd:
        highest_bidd = bidders[bidder]
        highest_bidder = bidder

print(f"The winner is {highest_bidder} with a bid of ${highest_bidd}.")