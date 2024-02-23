def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


n= int(input("Enter a number "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial  is", factorial(n))
