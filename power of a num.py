def numPower(data,n):
    if(n==0):
        return 1
    elif n<0:
        return 1 / numPower(data, -n)
    else:
        return data*numPower(data,n-1)
print(numPower(2,-10))
