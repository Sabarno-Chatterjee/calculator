from art import logo

#Add
def add(n1, n2):
    """This function is used for addition."""
    return n1 + n2


#Subtract
def subtract(n1, n2):
    """This function is used for subtraction."""
    return n1 - n2


#Multiplication
def multiply(n1, n2):
    """This function is used for multiplication."""
    return n1 * n2


#Division
def division(n1, n2):
    """This function is used for division."""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division,
}

def calculator():
    """This function is used for the purpose of calculations."""
    print(logo)
    num1 = float(input("What's the first number?\n"))

    for symbol in operations:
        print(symbol, end='  ')
    print()



    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above.\n")
        num2 = float(input("What's the next number?\n"))
        print()

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Do you want to continue? Press 'y' or 'n'.") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()