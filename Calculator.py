#Calculator using Switch-case
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=input("Enter an operator")
match c :
    case "+": print("addition is ",a+b)
    case "-": print("Substraction is ",a-b)
    case "*": print("Multiplication is ",a*b)
    case "/": print("Division is ",a/b)
    case _: print("Enter a valid operator ['+','-','*','/']")
