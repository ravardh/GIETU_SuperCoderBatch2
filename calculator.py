a=int(input("enter a no."))
b=int(input("enter a 2no."))
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