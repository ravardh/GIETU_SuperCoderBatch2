def fibo(n, list1):
    if n <= 1:
        return n
    if list1[n] == -1:
        list1[n] = fibo(n-1, list1) + fibo(n-2, list1)
    return list1[n]
n = int(input("Enter the range: "))
for i in range(1,n+1):
    list1 = [-1] * (n + 1)
for i in range(n):
    print(fibo(i,list1),end=" ")
