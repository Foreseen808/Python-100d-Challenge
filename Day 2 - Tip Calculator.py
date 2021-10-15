print("Welcome to the tip calculator")
# Takes the bill input from user and converts it into a float with 2 decimals precision
bill = "{:.2f}".format(float(input("What was the total bill?\n")))
# Concatenates 1. with input from user for the total amount formula
tip = ("1." + input("What percentage tip would you like to give? 10, 12, or 15?\n"))
# Takes user input and converts it from string to int
split = int(input("How many people to split the bill\n"))
# Calculates the total amount needed to be paid and concatenates it with the amount that each person needs to pay
print("Each person should pay: $" + "{0:.2f}".format(((float(bill) / int(split) * float(tip)))))

