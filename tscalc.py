a=int(input("enter first no."))
b=int(input("enter second no."))
operation=input("+,-,/,*")
match operation:
    case "+":
            print(a+b)
    case "-":
            print(a-b)
    case "/":
            print(a/b)
    case "*":
            print(a*b)
    case _ :
            print("invalid operation")
