def main():
    print("Enter the first array size")
    m = int(input())
    n = int(input())
    i, j, k = 0, 0, 0
    arr1 = [[0] * n for _ in range(m)]
    print("Enter the first array")
    for i in range(m):
        for j in range(n):
            arr1[i][j] = int(input())
    print("Enter the second array size")
    o = int(input())
    p = int(input())
    arr2 = [[0] * p for _ in range(o)]
    print("Enter the second array")
    for i in range(o):
        for j in range(p):
            arr2[i][j] = int(input())
    if n == o:
        arrnew = [[0] * p for _ in range(m)]
        for i in range(m):
            for j in range(p):
                for k in range(n):
                    arrnew[i][j] += arr1[i][k] * arr2[k][j]
        for i in range(m):
            for j in range(p):
                print(arrnew[i][j], end=" ")
            print()
    else:
        print("Multiplication not possible")


if __name__ == "__main__":
    main()

