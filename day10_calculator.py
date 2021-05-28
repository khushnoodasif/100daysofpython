print("Welcome to PyCalc! \n")
from day10_calculator_files import logo

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    num1 = float(input("what is your first number? \n".title()))
    for symbol in operation:
        print(symbol)
    calc_continue = True
    while calc_continue:
        operation_symbol = input("pick a operation from the line above. \n".title())
        num2 = float(input("what is your next number? \n".title()))
        calc_function = operation[operation_symbol]
        answer = calc_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'yes' to continue calculating with {answer}? or 'no' to start again. \n".title()) == "yes":
            num1 = answer
        else:
            calc_continue = False
            calculator()
calculator()
