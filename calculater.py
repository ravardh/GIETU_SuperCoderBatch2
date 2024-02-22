a=float(input('enter a number:'))
b=float(input('enter another number:'))
print(" 1.addition \n 2.subtration \n 3.multiplication \n 4.division")
operatino=int(input('enter a number between 1 to 4 to do the operation:'))
result=0
match operatino:
    case 1:
        result=a+b
    case 2:
        result=a-b
    case 3:
        result=a*b
    case 4:
        result=a/b
print(result)