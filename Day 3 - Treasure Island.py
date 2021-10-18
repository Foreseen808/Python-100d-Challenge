print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_choice = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if (first_choice == 'left'):
  second_choice = input("You come across a lake. Do you want to wait for a boat, or swim across? Type 'wait' or 'swim'").lower()
  if (second_choice == 'wait'):
    third_choice = input("The boat takes you to shore, where you find 3 doors, a yellow one, a blue one and a red one. Which one do you open? Please type 'red','blue' or 'yellow'\n").lower()
    if (third_choice == 'yellow'):
      print("Congratulations! You win!")
    elif (third_choice == 'red'):
      print("You fall into a pit of lava.\n Game over.")
    elif (third_choice == 'blue'):
      print ("You come across a pack of hungry beats.\n Game over.")
  else:
    print("You are attacked by trout.\n Game over.")
else:
  print("You fall into a hole\n Game over.")

