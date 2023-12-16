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
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the options above: ")
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")


if __name__ == "__main__":
    main()
