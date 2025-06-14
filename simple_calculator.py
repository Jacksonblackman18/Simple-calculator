# Jackson Blackman
# May 16th, 2025
# Calculator program

while True:
    operation = input("What is your operation?:")
    numberOne = int(input("What is your first number?:"))
    numberTwo = int(input("What is your second number?:"))
    if operation == "*":
        answer = numberOne * numberTwo
    elif operation == "+":
        answer = numberTwo + numberOne
    elif operation == "-":
        answer = numberOne - numberTwo
    elif operation == "%":
        answer = numberOne / numberTwo
    print(numberOne, operation, numberTwo, " = ", answer )
