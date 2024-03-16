def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

num= int(input("Enter a number "))
if num < 0:
    print("Invalid input, enter a positive number")
else:
    print("Factorial  is",factorial(num))
