n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
operator=input("enter the operator")
match operator:
  case "+":
    print("The sum is",n1+n2)
  case "+":
    print("The sum is",n1+n2)
  case "-":
    print("The sub is",n1-n2)
  case "*":
    print("The multiplication is",n1*n2)
  case "/":
    print("The division is",n1/n2)
  case "*":
    print("The power is",n1*n2)
  case _:
    print("Enter operator(+,-,*,/,*)")
