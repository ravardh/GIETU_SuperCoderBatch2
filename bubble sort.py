def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n):
            if(arr[i]<=arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
arr = list(map(int,input().split()))
bubble(arr)
print(arr)