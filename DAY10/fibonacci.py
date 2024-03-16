dp={}
def fib(n):
    if n in dp:
        return dp[n]
    elif n<=1:
        return n
    else:
        v=fib(n-1)+fib(n-2)
        return v
for i in range(0,8):
    print(fib(i))
