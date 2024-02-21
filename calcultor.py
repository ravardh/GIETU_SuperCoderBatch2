a = int(input("Enter the first number: "))
b = int(input("Enter the  second value: "))
op = input("Enter the operator: ")
match op:
    case '+':
        output = a + b
        print(f"{a} + {b} = {output}")
    case '-':
        output = a - b
        print(f"{a} - {b} = {output}")
    case '*':
        output = a * b
        print(f"{a} * {b} = {output}")
    case '/':
        if b != 0:
            output = a / b
            print(f"{a} / {b} = {output}")
        else:
            print("Error! Can not divisible by 0")
    case '%':
        if b != 0:
            output = a % b
            print(f"{a} % {b} = {output}")
        else:
            print("Error! Can not divisible by 0")
    case '//':
        if b != 0:
            output = a // b
            print(f"{a} // {b} = {output}")
        else:
            print("Error! Can not divisible by 0")
    case '**':
        
            output = a**b
            print(f"{a} ** {b} = {output}")
       
    