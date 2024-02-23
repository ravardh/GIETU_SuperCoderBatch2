def factorial(n):
    if(n==1):
        return 1;
    else:
        return n*factorial(n-1)
num=int(input("Enter the number"))
print("The factorial is",factorial(num))
