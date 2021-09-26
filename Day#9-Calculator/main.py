# Calculator
import art

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# create a dictionary named operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

go_on = True

print(art.logo)

# input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

for symbols in operations:
    print(symbols)

operation_symbol = input("Pick an operation from the line above: ")

result = operations[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
while go_on:
    is_continue = input(f"Type 'y' to continue calculating with {result} , or type 'no' to exit. :")
    if is_continue == 'y':
        next_num = float(input("Enter the next number: "))

        for symbols in operations:
            print(symbols)

        operation_symbol = input("Pick an operation from the line above: ")

        next_result = operations[operation_symbol](result, next_num)

        print(f"{result} {operation_symbol} {next_num} = {next_result}")
        result = next_result

    else:
        go_on = False