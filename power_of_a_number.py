def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
base = float(input("Enter the base (x): "))
exponent = int(input("Enter the exponent (n): "))
result = power(base, exponent)
print(f"{base}^{exponent} is: {result}")
