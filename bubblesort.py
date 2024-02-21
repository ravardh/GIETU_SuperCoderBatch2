def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [4, 8, 7, 1, 9, 2, 3, 6, 5]
bubble_sort(arr)
print("Sorted array is:", arr)
