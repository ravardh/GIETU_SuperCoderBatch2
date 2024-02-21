num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))

print("Press :")
print("\t1 for +")
print("\t2 for -")
print("\t3 for *")
print("\t4 for /")
print("\t5 for //")
print("\t6 for %")
print("\t7 for **")

operation=int(input("Enter the number to perform operation  :"))
match operation:
  case 1:
    print(num1+num2)
  case 2:
    print(num1-num2)
  case 3:
    print(num1*num2)
  case 4:
    print(num1/num2)
  case 5:
    print(num1//num2)
  case 6:
    print(num1%num2)
  case 7:
    print(num1**num2)
  case _:
    print("You have selected incorrect number")