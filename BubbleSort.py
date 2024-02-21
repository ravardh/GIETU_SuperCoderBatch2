def BubbleSort(arr):
    n=len(arr)
    swapped=False
    for i in range(n-1):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
        if not swapped:
            return
arr = [23,11,2,60,22,54,36,77,44]
BubbleSort(arr)
print("The sorted array is:")
print(arr)