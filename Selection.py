def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minId = i
        for j in range(i + 1, n):
            if arr[j] < arr[minId]:
                minId = j
        arr[i], arr[minId] = arr[minId], arr[i]

arr = [2,3,4,2,2,45,6,7]
selectionSort(arr)
print("sorted array is:", arr)

