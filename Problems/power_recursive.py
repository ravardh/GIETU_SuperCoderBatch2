def myPow(x: int, n: int) -> int:
    if n == 1:
        return x

    return x * myPow(x, n - 1)


if __name__ == '__main__':
    print(myPow(2, 10))
