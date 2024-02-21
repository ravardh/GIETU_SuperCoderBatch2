a=int(input("Enter operand 1:"))
b=int(input("Enter operand 2:"))
char=input("Enter any symbol [+,-,/,*,%]:")
match char:
  case "+":
    print(a+b)
  case "-":
    print(a-b)
  case "*":
    print(a*b)
  case "/":
    print(a/b)
  case "%":
    print(a%b)
  case _:
    print("Somthing Went wrong:(!")