def factorial(num):
    if(num==1):
        return 1
    return num*factorial(num-1)

number=int(input("Enter the value"))
print(factorial(number)," is the factorial of ",number )