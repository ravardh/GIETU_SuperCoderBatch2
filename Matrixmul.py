r = int(input("enter the rows: "))
c = int(input("enter the columns: "))

print("enter matrix A: ")
a = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        a[i][j] = int(input())

print("enter matrix B: ")
b = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        b[i][j] = int(input())

print("multiplication matrix: ")
d = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        d[i][j] = 0
        for k in range(c):
            d[i][j] += a[i][k] * b[k][j]
        print(d[i][j], end=" ")
    print()