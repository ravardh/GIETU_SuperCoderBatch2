def InsertionSort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range (1,n):
        a=arr[i]
        j=i-1
        while j>=0 and a<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=a
arr=[23,11,67,55,31,10]
InsertionSort(arr)
print(arr)