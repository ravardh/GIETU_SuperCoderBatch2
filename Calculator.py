n1 = int(input("Enter  first number: "))
n2 = int(input("Enter  second number: "))

print("Press please:")
print("\t1 to get +")
print("\t2 to get -")
print("\t3 to get *")
print("\t4 to get /")
print("\t5 to get //")
print("\t6 to get %")
print("\t7 to get **")

operation = int(input("Enter any number to get operations done: "))
match operation:
    case 1:
        print(n1 + n2)
    case 2:
        print(n1 - n2)
    case 3:
        print(n1 * n2)
    case 4:
        print(n1 / n2)
    case 5:
        print(n1 // n2)
    case 6:
        print(n1 % n2)
    case 7:
        print(n1 ** n2)
    case _:
        print("You have selected an incorrect number")
