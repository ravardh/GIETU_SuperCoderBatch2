def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
a=[4,8,7,1,9,2,3,6,5]
print("Original List:", a)

selection_sort(a)

print("Sorted List:", a)
