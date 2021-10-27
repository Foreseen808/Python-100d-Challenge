from calculator_art import logo

def addition(a, b):
  return a+b

def substraction(a, b):
  return a-b

def multiplication(a, b):
  return a*b

def division(a, b):
  return a/b

operations = {
  "+": addition,
  "-": substraction,
  "*": multiplication,
  "/": division,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?\n"))
  for symbol in operations:
      print(symbol)
  keep_calculating = True
  
  while keep_calculating:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?\n"))
    calculation_function = operations[operation_symbol]
    ans = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {ans}")

    if input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit.: ") == "y":
      num1 = ans
    else:
      keep_calculating = False
      calculator()

calculator()
