def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def main():
    calculating = True
    num1 = int(input("What's the first number?: "))
    while calculating:
        num2 = int(input("What's the second number?: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the options above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or "
                       f"type 'n' to exit or "
                       f"type 'c' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            calculating = False
        else:
            calculating = False
            main()


if __name__ == "__main__":
    main()
