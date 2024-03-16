def fun(arr):
    maxl=0
    for i in range(len(arr)):
        cur=0
        for j in range(i,len(arr)):
            cur+=arr[j]
            if cur==0:
                maxl=max(maxl,j-i+1)
    return maxl
arr=[9,-3,3,-1,6,-5]
res=fun(arr)
print(res)