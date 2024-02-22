def selection(arr):
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i+1,len(arr)):
            if min > arr[j]:
                min = arr[j]
                arr[j],arr[i] = arr[i],arr[j] 

arr = list(map(int,input().split()))
selection(arr)
print(arr)