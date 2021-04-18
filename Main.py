# Integration Project

"""A text-based calculator program.

This program does several mathematical operations and prints the results."""

__version__ = '1'
__author__ = 'Hailey Merrifield'


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    return x / y


def exponentiation(x, y):
    return x ** y


def floor_division(x, y):
    return x // y


def modulation(x, y):
    return x % y


def rooting(x, y):
    return x ** (1. / y)


def square_rooting(x):
    return rooting(x, 2)


def cube_rooting(x):
    return rooting(x, 3)


def my_help(x):
    if x == 0 or x == 42.:
        return "Help" + int(x) * "!"
    return int(x) * "Help"


def equality_test(x, y):
    if x > y:
        print(x, "is greater than", y)
    elif x < y:
        print(x, "is less than", y)
    else:
        print(x, "is equal to", y)


def sum_range(x, y):
    """Finds the sum of integers in the range from x to y."""
    output = 0
    for i in range(int(x), int(y + 1)):
        output += i
    return output


def do_operation(x, y, operation_type):
    """Checks which operation to do and does it."""
    output = 0
    if operation_type == "Addition":
        print("Adding numbers...")
        output = addition(x, y)

    elif operation_type == "Subtraction":
        print("Subtracting numbers...")
        output = subtraction(x, y)

    elif operation_type == "Multiplication":
        print("Multiplying numbers...")
        output = multiplication(x, y)

    elif operation_type == "Division":
        print("Dividing numbers...")
        output = division(x, y)

    elif operation_type == "Exponentiation":
        print("Exponentiating numbers...")
        output = exponentiation(x, y)

    elif operation_type == "Floor Division":
        print("Floor dividing numbers...")
        output = floor_division(x, y)

    elif operation_type == "Modulation":
        print("Modulating numbers...")
        output = modulation(x, y)

    elif operation_type == "Rooting":
        print("Rooting numbers...")
        output = rooting(x, y)

    elif operation_type == "Square Rooting":
        print("Square rooting number...")
        output = square_rooting(x)

    elif operation_type == "Cube Rooting":
        print("Cube rooting number...")
        output = cube_rooting(x)

    elif operation_type == "Help":
        """Secret command for spice."""
        print(my_help(x))
        return int(input("Enter a starting number: "))

    elif operation_type == "Clear":
        """Allows the user to enter a new starting number."""
        return input("Enter a starting number: ")

    elif operation_type == "Equality Test":
        print("Testing equality...")
        equality_test(x, y)
        return input("Enter a starting number: ")

    elif operation_type == "Sum Range":
        print("Summing range from", x, "to", y)
        output = sum_range(x, y)

    print(output)
    return output


def main():
    name = input("Enter your name: ")
    print("\nWelcome", name, end='!\n', sep=', ')

    # https://realpython.com/python-print/#preventing-line-breaks further
    # helped with sep= and end= arguments

    print("\nThese are the types of numerical operations: \n" + "Addition",
          "Subtraction", "Multiplication", "Division",
          "Exponentiation", "Floor Division", "Modulation", "Rooting",
          "Square Rooting", "Cube Rooting", "Clear", "Equality Test",
          "Sum Range",
          sep=', ')
    # Used the + to separate the list of operations from the label without
    # using the , from the sep= argument

    operation_type = input("\nType of operation: ")
    num1 = float(input("Enter first number: "))
    num2 = 0

    if (operation_type != "Square Rooting") and (
            operation_type != "Cube Rooting") and (operation_type != "Help"):
        num2 = float(input("Enter second number: "))

    # https://realpython.com/lessons/introduction-and-python-if-statement/
    # taught me if statements

    while True:
        """Allows the user to do operations on the previous result."""
        num1 = do_operation(num1, num2, operation_type)
        operation_type = input("\nType of operation: ")

        if (operation_type != "Square Rooting") and (
                operation_type != "Cube Rooting") and not (
                operation_type == "Help"):
            num2 = float(input("Enter number: "))
