while True:
    # Take two numbers as input and print their sum.
    operator = input("Chose operator (+,-,*,/?) > ")
    first_no = int(input("Enter first digit> "))
    second_no = int(input("Enter second digit> "))
    try:
        if operator == "+":
            print(str(first_no + second_no))
        elif operator == "-":
            print(str(first_no-second_no))
        elif operator == "*":
            print(str(first_no*second_no))
        elif operator == "/":
            print(str(first_no/second_no))
        else:
            print("Please chose a valid operator")
    except ZeroDivisionError:
        print("Zero Division Error")