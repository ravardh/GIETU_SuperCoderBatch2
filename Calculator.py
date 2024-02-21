num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

operator = input("Enter any operator(+,-,*,/,//,%,**):")

operations = {
    '+': num1 + num2,
    '-': num1 - num2,
    '*': num1 * num2,
    '/': num1 / num2,
    '//': num1 // num2,
    '%': num1 % num2,
    '**': num1 ** num2
}

result = operations.get(operator)

print("Result:", result)