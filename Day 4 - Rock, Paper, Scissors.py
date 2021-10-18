import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0, 2)
if (comp_choice == 0):
  if(user_choice == 1):
    print("Computer chose: \n" + rock)
    print("You chose: \n" + paper)
    print("Congratulations, you won!")
  elif (user_choice == 0):
    print("Computer chose: \n" + rock)
    print("You chose: \n" + rock)
    print("It is a draw")
  else:
    print("Computer chose: \n" + rock)
    print("You chose: \n" + scissors)
    print("You lose")
elif (comp_choice == 1):
  if (user_choice == 2):
    print("Computer chose: \n" + paper)
    print("You chose: \n" + scissors)
    print("Congratulations, you won!")
  elif (user_choice == 1):
    print("Computer chose: \n" + paper)
    print("You chose: \n" + paper)
    print("It is a draw")
  else:
    print("Computer chose: \n" + paper)
    print("You chose: \n" + rock)
    print("You lose")
else:
  if (user_choice == 0):
    print("Computer chose: \n" + scissors)
    print("You chose: \n" + rock)
    print("Congratulations, you won!")
  elif (user_choice == 2):
    print("Computer chose: \n" + scissors)
    print("You chose: \n" + scissors)
    print("It is a draw")
  else:
    print("Computer chose: \n" + scissors)
    print("You chose: \n" + paper)
    print("You lost")