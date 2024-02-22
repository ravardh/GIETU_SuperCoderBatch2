num = int(input("Enter a number to calculate its factorial: "))

factorial_result = 1
for i in range(1, num + 1):
    factorial_result *= i
print(factorial_result)