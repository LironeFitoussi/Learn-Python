from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(calculator["*"](4, 8))

print(logo)
print("Welcome to the calculator")

def calculator_function():
    num1 = float(input("What's the first number?: "))
    for symbol in calculator:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        if operation_symbol not in calculator:
            print("Invalid operation")
            should_continue = False
            calculator_function()
        num2 = float(input("What's the next number?: "))
        calculation_function = calculator[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        next_action = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation click 'enter' to exit: ")
        if next_action == "y":
            num1 = answer
        elif next_action == "n":
            should_continue = False
            calculator_function()
        else:
            print("See you later")
            return

calculator_function()