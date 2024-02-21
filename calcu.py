def add(n1,n2):
    print(n1+n2)
def sub(n1,n2):
    print(n1-n2)
def mul(n1,n2):
    print(n1*n2)
def div(n1,n2):
    print(n1/n2)

n1=int(input("enter a number"))
n2=int(input("enter a number"))
sym=input("input a operation")
match sym:
    case '+':
        add(n1,n2)
    case '-':
        sub(n1,n2)
    case '*':
        mul(n1,n2)
    case '/':
        div(n1,n2)

    case _:
        print("no operation")

        