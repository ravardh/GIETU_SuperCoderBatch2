def factorial(n):
    if(n==1):
        return 1
    else:
        return factorial(n-1)*n
n=int(input("enetr a number:"))
print("fact of {0} is {1}".format(n , factorial(n)))