from art import logo
import math

print(logo)

def sum(number_1, number_2):
    return number_1 + number_2

def sub(number_1, number_2):
    return number_1 - number_2

def div(number_1, number_2):
    try:
        return number_1 / number_2
    except ZeroDivisionError:
        return None

def mul(number_1, number_2):
    return number_1 * number_2

new_calculation = True
result = 0
operate = True

while operate:
    if new_calculation:
        number_1 = float(input("What's the first number?: "))
    else:
        number_1 = result
    operation = input("+\n-\n*\n/\nPick an operation: ")
    number_2 = float(input("What's the next number?: "))

    if operation == '+':
        result = sum(number_1,number_2)
        print(f"{number_1} + {number_2} = {result}")
    elif operation == '-':
        result = sub(number_1,number_2)
        print(f"{number_1} - {number_2} = {result}")
    elif operation == '/':
        result = div(number_1,number_2)
        print(f"{number_1} / {number_2} = {result}")
    elif operation == '*':
        result = mul(number_1,number_2)
        print(f"{number_1} * {number_2} = {result}")
    else:
        result = None
        print("Invalid operation, try again.")

    if result != None:
        option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'q' to quit: ").lower()
        if option == 'y':
            new_calculation = False
        elif option == 'n': 
            new_calculation = True
        else:
            operate = False
    else:
        new_calculation = True
