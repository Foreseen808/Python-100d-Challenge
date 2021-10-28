from GuessTheNumber_art import logo
import random
print(logo)
easy_game = 10
hard_game = 5

def PlayerLives():
  """
  Sets the player lives based on difficulty
  """
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return easy_game
  elif difficulty == 'hard':
    return hard_game

def CompareNumber(player_guess, computer_guess, lives_remaining):
  """
  Compares the input number against the random generated one
  """
  if player_guess > computer_guess:
    print("Too high")
    return lives_remaining - 1
  elif player_guess < computer_guess:
    print("Too low")
    return lives_remaining - 1
  else:
    print(f"You got it! The answer was {computer_guess}.")



def playgame():
  computer_guess = random.randrange(1,100)
  print("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100.")
  
  
  lives_remaining = PlayerLives()
  player_guess = 0

  while player_guess != computer_guess:
    print(f"You have {lives_remaining} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    lives_remaining = CompareNumber(player_guess, computer_guess, lives_remaining)
    if lives_remaining == 0:
      print("You've run out of guesses, you lose.")
      return
    elif player_guess != computer_guess:
      print("Guess again")

playgame()


