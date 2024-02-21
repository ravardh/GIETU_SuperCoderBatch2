a=int(input("Enter value1:"))
b=int(input("Enter value2:"))

opr = int(input("choose opeartion: 1 add \n 2 sustract \n 3 divide \n 4 multiply \n 5 modulous:"))

match opr:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a/b)
    case 4:
        print(a*b)
    case 5:
        print(a%b)