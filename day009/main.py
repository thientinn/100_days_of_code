from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bidder = {}
end_of_game = False

def highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if highest_bid < bid_amount:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")

while not end_of_game:
  name = input("what is your name?: ")
  bid = int(input("what is your bid?: $"))
  bidder[name] = bid
  output = input("Are there any other bidders? Type 'yes or 'no'.")
  if output == 'no':
    end_of_game = True
    highest_bidder(bidder)
  elif output == 'yes':
    clear()
