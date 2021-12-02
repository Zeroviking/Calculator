import Operations


def Do_math():
    print("Select plan of action.")
    print("Enter 1 to add")
    print("Enter 2 to subtract")
    print("Enter 3 to multiply")
    print("Enter 4 to divide")

    while True:
        # take input from the user
        choice = input("Enter choice here: ")

        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            # use float so you can use decimals.
            if choice == '1':
                print(num1, "+", num2, "=", Operations.add(num1, num2))

            if choice == '2':
                print(num1, "-", num2, "=", Operations.subtract(num1, num2))

            if choice == '3':
                print(num1, "*", num2, "=", Operations.multiply(num1, num2))

            if choice == '4':
                print(num1, "/", num2, "=", Operations.divide(num1, num2))

            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Wanna do nudder dwon (Enter Yes, or No): ")
            if next_calculation == "No":
                break
            if next_calculation == "Yes":
                Do_math()

        else:
            print("Invalid Input")
Do_math()