a = int(input("Enter the first number: "))
b = int(input("Enter the  second value: "))
op = input("Enter the operator: ")
match op:
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
            print("Error! Can not divisible by 0")

