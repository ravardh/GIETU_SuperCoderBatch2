def power(x, n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            half_power = power(x, n // 2)
            return half_power * half_power
        else:
            half_power = power(x, (n - 1) // 2)
            return x * half_power * half_power

# Example usage:
base = 50
exponent = 56
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")