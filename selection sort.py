def selection(arr):
    n=len(arr)
    for j in range(0,n):
        min=arr[j]
        for i in range(j,n):
            if(min>=arr[i]):
                min=arr[i]
                arr[j],arr[i]=arr[i],arr[j]
                p=i
        arr[j],arr[p]=arr[p],arr[j]
arr = list(map(int,input().split()))
selection(arr)
print(arr)