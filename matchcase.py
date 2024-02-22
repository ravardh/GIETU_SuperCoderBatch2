def calculator(operator,num1,num2):
    match operator:
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case"*":
            result = num1 * num2
        case "/":
            if num2!=0:
             result = num1 / num2
            else:
             result="error in division by zero"
        case "%":
            result = num1 % num2
        case _:
            result = "invalid operator"
    return result
operator=input("enter the operator(+ ,-, *, / ,%): ")
num1=int(input("enter the first num: "))
num2=int(input("enter the second num: "))
result=calculator(operator,num1,num2)
print(result)


