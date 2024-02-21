def calculator():
    print("Welcome to the calculator!")
    while True:
        print("Choose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        choice = input("Enter choice (1/2/3/4/5): ")
        match choice:
            case "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 + num2)
            case "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 - num2)
            case "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print("Result:", num1 * num2)
            case "4":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    print("Result:", num1 / num2)
            case "5":
                print("Exiting calculator. Goodbye!")
                return
            case _:
                print("Invalid input! Please enter a valid choice.")

calculator()
