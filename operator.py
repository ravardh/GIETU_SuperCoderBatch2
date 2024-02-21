a=int(input("enter a number"))
b=int(input("enter a number"))
operator = input("+,-,*,/,")
match operator :
    case "+":
      print(a+b)
    case"-":
      print(a-b)
    case"*":
      print("*")
    case"/":
      print("/")   
    case _:
        print("invalid operator")