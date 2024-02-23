def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

def calculator(operator, x, y):
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    operation = operations.get(operator)
    if operation:
        return operation(x, y)
    else:
        return "Invalid operator"

operator = input("Enter the operator (add, subtract, multiply, divide): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculator(operator, num1, num2)
print("Result:", result)
