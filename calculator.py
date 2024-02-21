a=int(input("enter a number"))
b=int(input("enter a number"))
operator=input("+,-,*,/,")
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid operator")