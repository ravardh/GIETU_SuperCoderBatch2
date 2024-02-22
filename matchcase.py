a1=int(input("enter no.1:"))
a2=int(input("enter no.2:"))
op=input("enter operator to perform an operation:")
match op:
    case "+":
        print("sum is: ",a1+a2)
    case "-":
        print("difference is: ",a1-a2)
    case "*":
        print("product is: ",a1*a2)
    case "/":
        print("result is: ",a1/a2)
    case "//":
        print("result of floor division is: ",a1//a2)
    case "%":
        print("remainder is: ",a1%a2)
