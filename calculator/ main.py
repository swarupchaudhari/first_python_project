try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print(
        "What kind of operation do you want to perform?\n"
        "Press + for addition\n"
        "Press - for subtraction\n"
        "Press * for multiplication\n"
        "Press / for division"
    )

    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Division by zero is not allowed")
        case _:
            print("Invalid operation")

except ValueError:
    print("Enter valid integer values for a and b")