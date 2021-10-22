#HINT: You can call clear() to clear the output in the console.
from replit import clear
import blindauction_art as art

print(art.logo)
auction = {}
auction_end = False
while not auction_end:

  name = input("What is your name?\n")
  bid = input("What is your bid price?\n")
  auction[name] = bid

  
  choice = input("Are there any other uses who want to bid? type 'yes' or  'no'\n")
  if choice.lower() == 'yes':
      clear()
  elif (choice.lower() == 'no'):
    auction_end = True
    maximum = max(auction, key=auction.get)
    print("The winner is " + maximum + " with a bid of $" + auction[maximum])

