def myPow(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return myPow(x * x, n // 2)
    else:
        return x * myPow(x * x, n // 2)

print(myPow(5, 3))
