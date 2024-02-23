def myPow( x, n):
        N = n
        if n == 0 :
            return 1
        if n < 0:
            return 1 / pow(x, -N)
        return pow(x, N)

def pow( x, n):
        if n == 1:
            return x
        if n % 2 == 0:
            return pow(x * x, n // 2)
        else:
            return x * pow(x * x, n // 2)
print(myPow(10,2))