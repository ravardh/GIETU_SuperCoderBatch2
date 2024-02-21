def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr =  [4, 8, 7, 1, 9, 2, 3, 6, 5]
insertion_sort(arr)
print("Sorted array is:", arr)
