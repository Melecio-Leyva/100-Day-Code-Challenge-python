#clearing art.
import os 
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the silent auction")

bid = {}
def find_highest_bid(bidding_list):
    highest_bid=0
    winner=""
    for bidder in bid:
        bid_amount = bid[bidder]
        if highest_bid <bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
nxt_person = True
while nxt_person:
    name = input("What is your name.")
    price= int(input("What is your bid? $"))
    bid[name] = price
    person= input("Is the someone else in the room? type yes or no.\n").lower()
    if person == 'no':
        nxt_person = False
        find_highest_bid(bid)
    elif person == 'yes':
        cls()

