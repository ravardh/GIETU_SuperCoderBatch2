def factorial(n: int):
    if n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == '__main__':
    fact: int = 1
    for i in range(1, 6):
        fact = fact * i

    print(factorial(5))
