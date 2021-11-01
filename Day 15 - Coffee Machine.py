coffee_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_resources_enough(order):
    """
    Checks if there are enough resources to make the drink
    """
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_payment():
    """
    Takes coins input from user and converts it
    """
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order):
    """
    Makes the drink
    """
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {drink_name}. Enjoy!")


def payment_successful(money_received, drink_cost):
    """
    Checks to see if the money received is enough to cover the cost of the drink
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee_machine():
    is_on = True
    while is_on:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_choice == 'off':
            break
        if coffee_choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = coffee_menu[coffee_choice]
            if is_resources_enough(drink['ingredients']):
                payment = process_payment()
                if payment_successful(payment, drink["cost"]):
                    make_coffee(coffee_choice, drink['ingredients'])


coffee_machine()