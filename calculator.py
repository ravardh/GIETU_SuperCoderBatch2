a=int(input("Enter the 1st number"))
b=int(input("Enter the 2nd number"))
calc=input("Enter the operation required")
match calc:
    case '+':
        print(a+b)
        print("The addition operation is successful")
    case '-':
        print(a-b)
        print("The subtraction operation is successful")

    case '*':
        print(a*b)
        print("The multiplication operation is successful")

    case '/':
        print(a/b)
        print("The divison operation is successful")

    case '//':
        print(a//b)
        print("The floor division operation is successful")

    case '%':
        print(a%b)
        print("The modulous operation is successful")

    case _:
        print("Enter valid operator")
