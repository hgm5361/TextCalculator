#Integration Project
#Hailey Merrifield
#Making a textbased calculator program

name = input("Enter your name: ")
print("\nWelcome", name, end='!\n', sep=', ')

#https://realpython.com/python-print/#preventing-line-breaks further helped with sep= and end= arguments

print("\nThese are the types of numerical operations: \n" + "Addition", "Subtraction", "Multiplication", "Division", "Exponentiation", "Floor Division", "Modulation", "Rooting", "Square Rooting", "Cube Rooting", sep=', ')
#Used the + to separate the list of operations from the label without using the , from the sep= argument

operation_type = input("\nType of operation: ")
num1 = float(input("Enter first number: "))

if (operation_type != "Square Rooting") and (operation_type != "Cube Rooting") and (operation_type != "Help"):
    num2 = float(input("Enter second number: "))

#https://realpython.com/lessons/introduction-and-python-if-statement/ taught me if statements

if operation_type == "Addition":
    output = num1 + num2 #Used to add num1 and num2
    print("Adding numbers...")
    print(output)

if operation_type == "Subtraction":
    output = num1 - num2 #Used to subtract num1 and num2
    print("Subtracting numbers...")
    print(output)

if operation_type == "Multiplication":
    output = num1 * num2 #Used to multiply num1 and num2
    print("Multiplying numbers...")
    print(output)

if operation_type == "Division":
    output = num1 / num2 #Used to divide num1 and num2
    print("Dividing numbers...")
    print(output)

if operation_type == "Exponentiation":
    output = num1 ** num2 #Used to exponentiate num1 and num2
    print("Exponentiating numbers...")
    print(output)

if operation_type == "Floor Division":
    output = num1 // num2 #Used to floor divide num1 and num2
    print("Floor dividing numbers...")
    print(output)

if operation_type == "Modulation":
    output = num1 % num2 #Used to modulate num1 and num2
    print("Modulating numbers...")
    print(output)

if operation_type == "Rooting":
    output = num1 ** (1/num2) #Used to root num1 with degree num2
    print("Rooting numbers...")
    print(output)

if operation_type == "Square Rooting":
    output = num1 ** (1/2) #Used to square root num1
    print("Square rooting number...")
    print(output)

if operation_type == "Cube Rooting":
    output = num1 ** 1/3 #Used to cube root num1
    print("Cube rooting number...")
    print(output)

if operation_type == "Help": #secret command for spice
    output = int(num1)* "Help"
    print(output)