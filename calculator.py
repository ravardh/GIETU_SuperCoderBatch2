def add(num1,num2):
    print(num1/num2)
def sub(num1,num2):
     print(num1-num2)
def multiplication(num1,num2):
    print(num1*num2)
def division(num1,num2):
    print(num1/num2)

print("Performing Operation")
n=input("Enter a operation to perform")
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
match n:
    case '+':
        add(a,b)
    case '-':
        sub(a,b)
    case '*':
        add(a,b)
    case '/':
        add(a,b)
    case _ :
        print("Enter a valid operation")
