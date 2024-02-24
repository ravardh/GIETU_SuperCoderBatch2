def myPow(x,n):
    if n==0:
        return 1
    if n<0:
        x = 1/x
        n = -n
    result = myPow(x*x,n//2)
    if n %2== 1:
        result *=x
    return result
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = myPow(base,exponent)
print(f"{base} rasised to the power of {exponent} is: {result}")

