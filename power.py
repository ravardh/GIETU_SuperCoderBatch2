
def myPow(self, x, n):
        if(n==0):
            return 1
        return x*myPow(n-1)
x=2
n=10
print(myPow(x,n))

        