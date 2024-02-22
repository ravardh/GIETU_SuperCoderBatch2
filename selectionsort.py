def selection(arr):
    n = len(arr)
    for i in range (n):
        min = i
        for j in range (i + 1,n):
            if(arr[min] > arr[j]):
                min = j
        arr[min],arr[i] = arr[i], arr[min]


arr = [2,4,5,2,8,9,4,7]
selection(arr)
print("Sorted array is:", arr)