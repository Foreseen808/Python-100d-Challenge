from higher_lower_data import logo
from higher_lower_data import vs
from higher_lower_data import data
import random


def ChoiceOutput(choice):
  """
  Gets name, follower_count, description and country from the list and returns the follower_count
  """
  name = data[choice].get('name')
  follower_count = data[choice].get('follower_count')
  description = data[choice].get('description')
  country = data[choice].get('country')
  
  print(f"{name}, a {description}, from {country}")
  return follower_count  

def Compare(choice1, choice2):
  """
  Compares the 2 choices between each other and returns 1 if true or 0 if false
  """
  if choice1 >= choice2:
    return 1
  else:
    return 0


def playgame():
  print(logo)
  score = 0
  game_over = False
  while not game_over:
    ch1 = random.randint(0,len(data)-1)
    ch2 = random.randint(0,len(data)-1)
    a = ChoiceOutput(ch1)
    print(vs)
    b = ChoiceOutput(ch2)
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if answer == 'A':
      answer = a
      if Compare(a, b):
        score += 1
        print(f"You're right! Current score:{score}")
      else:
        print(f"Sorry, that's wrong. Final score:{score}")
        game_over = True
    elif answer == 'B':
      answer = b
      if Compare(b, a):
        score += 1
        print(f"You're right! Current score:{score}")
      else:
        print(f"Sorry, that's wrong. Final score:{score}")
        game_over = True
    
  
  
  

playgame()

