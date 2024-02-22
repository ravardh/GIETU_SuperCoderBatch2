# calculator
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))
operator = input("enter the operator")
match operator:
    case "+":
        print("The sum is", num1 + num2)
    case "+":
        print("The sum is", num1 + num2)
    case "-":
        print("The sub is", num1 - num2)
    case "*":
        print("The multiplication is", num1 * num2)
    case "/":
        print("The division is", num1 / num2)
    case "":
        print("The power is", num1 ** num2)
    case _:
        print("Enter valid operator(+,-,,/,*)")
