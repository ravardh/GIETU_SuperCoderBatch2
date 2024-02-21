x = int(input("Enter the first value: "))
y = int(input("Enter the  second value: "))
op = input("Enter the operator: ")
match op:
    case '+':
        result = x + y
        print(f"{x} + {y} = {result}")
    case '-':
        result = x - y
        print(f"{x} - {y} = {result}")
    case '*':
        result = x * y
        print(f"{x} * {y} = {result}")
    case '/':
        if y != 0:
            result = x/ y
            print(f"{x} / {y} = {result}")
        else:
            print("Error! ")
    case '%':
        if y != 0:
            result = x % y
            print(f"{x} % {y} = {result}")
        else:
            print("Error! ")
    case '//':
        if y!= 0:
            result = x // y
            print(f"{x} // {y} = {result}")
        else:
            print("Error! Can not divisible by 0")
    case '**':
        if y != 0:
            result = x ** y
            print(f"{x} ** {y} = {result}")
        else:
            print("Error!")
