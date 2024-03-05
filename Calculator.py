x=int(input('Enter first number'))
y=int(input('Enter second number'))
symbol=input('Enter a symbol')
def add(x,y):
    print(x+y)
def subt(x,y):
    print(x-y)
def multi(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
def modulus(x,y):
    print(x%y)


match symbol:
    case'+':
        add(x,y)
    case'-':
        subt(x,y)
    case'*':
        multi(x,y)
    case'/':
        div(x,y)
    case '%':
        modulus(x%y)
    case _:
        print("No operation")
