def power(x, n):
    if n > 0:
        return x**n
    else:
        return "print a valid +ve number"
    '''elif n < 0:
        return 1 / power(x, -n)
    elif n % 2 == 0:
        return power(x*x, n//2)
    else:
        return x * power(x*x, (n-1)//2)'''

try:
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    result = power(x, n)
    print(f"{x} raised to the power {n} is: {result}")
except ValueError:
    print("Please enter valid numbers.")
