# ✅ TODO 01 - Print the logo.
# ✅ TODO 02 - Ask the name which will be the 'key' and then the bid which will be the 'value'. Insert it into the dictionary.
# ✅ TODO 03 - while loop will use to check wether we enter "yes or no". If yes then clear the console and again loop otherwise False the loop.
# ✅ TODO 04 - Loop the dictionary and will see who bid the high value and print it out.

from art import logo
import os

def cls():             #clear funcion
    os.system('cls')

def checker(d_of_bidders):
    highest_bid = 0
    winner = ""
    for bidder in d_of_bidders:
        bid_amount = d_of_bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner candidate who bid the highest is {winner} with bidded cost of ${highest_bid}!")

print(logo)

dict_of_biders = {}
bidder_left = True

while bidder_left:
    name = input("Enter the name: ")
    bid = int(input("Enter the bid: $"))
    dict_of_biders[name] = bid
    b_left = input("Does any more bidder left? Type 'yes' if left otherwise 'no': ").lower()
    if b_left == "yes":
        cls()
    else:
        bidder_left = False
        cls()

checker(dict_of_biders)
