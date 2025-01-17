from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Invalid Input"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    first_number = float(input("What is the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        if operator not in operations:
            print("Invalid operator. Please choose from +, -, *, /.")
            continue

        second_number = float(input("What is the next number?: "))

        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if should_continue.lower() == 'y':
            first_number = result
        elif should_continue.lower() == 'n':
            should_continue = False
            calculator()
        else:
            print("Invalid Input.")
            should_continue = False

calculator()