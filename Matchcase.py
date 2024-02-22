def calculator(operator,num1,num2):
 match operator:
    case '+':
        result = num1+num2
    case '-':
        result = num1-num2
    case '*':
        result = num1*num2
    case '/':
        if num2 !=0:
            result = num1/num2
        else:
            result = "error:division by zero!"
    case '%':
        result = num1%num2
    case _:
         result = "invalid operator"
 return result
operator=input("Enter the operator(+, _, *, /, %): ")
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
result=calculator(operator,num1,num2)
print(result)