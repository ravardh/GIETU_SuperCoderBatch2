def numPow(data,n):
    if(n==0):
        return 1
    elif n<0:
        return 1 / numPow(data, -n)
    else:
        return data*numPow(data,n-1)
print(numPow(2,10))
