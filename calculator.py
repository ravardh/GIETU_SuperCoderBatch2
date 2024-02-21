#calculator using switch case

import switch
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "infinity"

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculate(operator, x, y):
    
    result = switch.Switch(operator)
    with result:
        if '+':
            result = operations['+'](x, y)
        if '-':
            result = operations['-'](x, y)
        if '*':
            result = operations['*'](x, y)
        if '/':
            result = operations['/'](x, y)
        result_ = "no such operator found"
    return result

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    result = calculate(operator, num1, num2)

    print("Result:", result)
