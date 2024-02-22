a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
optr = input("Enter the operator: ")
match optr:
    case '+':
        result = a + b
        print(f"{a} + {b} = {result}")
    case '-':
        result = a - b
        print(f"{a} - {b} = {result}")
    case '*':
        result = a * b
        print(f"{a} * {b} = {result}")
    case '/':
        if b != 0:
            result = a / b
            print(f"{a} / {b} = {result}")
        else:
            print("Error! Can not divisible by 0")
    case '%':
        if b != 0:
            result = a % b
            print(f"{a} % {b} = {result}")
        else:
            print("Error! Can not divisible by 0")
    case '//':
        if b != 0:
            result = a // b
            print(f"{a} // {b} = {result}")
        else:
            print("Error! Can not divisible by 0")
    case '**':
        if b != 0:
            result = a ** b
            print(f"{a} ** {b} = {result}")
        else:
            print("Error!")
