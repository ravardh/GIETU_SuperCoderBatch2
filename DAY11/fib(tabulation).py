def fib(num):
    f = [-1 for _ in range(7)]
    f[0]=0
    f[1]=1
    for i in range(2,7):
        f[i]=f[i-1]+f[i-2]
    return f[i]
print(fib(5))
