def calculator(operator, num1, num2):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '%':
            return num1 % num2
        case _:
            return "Invalid operator"

operator = input("Enter operator (+, -, *, /, %): ")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

result = calculator(operator, num1, num2)
print("Result:", result)
