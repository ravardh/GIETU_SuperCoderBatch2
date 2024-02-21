#Caculator
num1 = int(input("Enter the first number: "))
operator = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
match operator:
    case '+':
        print("Sum:-",num1 + num2)
    case '-':
        print("Difference:-",num1 - num2)
    case '*':
        print("Multiplication",num1 * num2)
    case '/':
         if num2 != 0:
             print("division", num1 / num2)
         else:
             print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator. Please enter +, -, *, or /")


