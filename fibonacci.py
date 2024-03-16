def fibo(n,l1):
    if n<=1:
        return n
    if l1[n]==-1:
        l1[n]=fibo(n-1,l1)+fibo(n-2,l1)
    return l1[n]
n = int(input("Enter the range: "))
for i in range(1,n+1):
    l1=[-1]*(n + 1)
for i in range(n):
    print(fibo(i,l1),end=" ")
