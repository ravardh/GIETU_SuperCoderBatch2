def add(i,j):
    return i+j

def sub(i,j):
    return i-j

def mul(i,j):
    return i*j

def div(i,j):
    return i/j

operator = input("Enter operator (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operator == '+':
    add(a,b)
elif operator == '-':
    sub(a,b)
elif operator == '*':
    mul(a,b)
elif operator == '/':
    div(a,b)