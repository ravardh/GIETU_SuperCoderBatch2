def power(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    elif n % 2 == 0:
        return power(x * x, n // 2)
    else:
        return x * power(x, n - 1)

x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
result = power(x, n)
print("Result:", result)
