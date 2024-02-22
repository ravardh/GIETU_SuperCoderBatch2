def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):

        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j


        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_array = [64, 25, 12, 22, 11]
print("Original Array:", my_array)

selection_sort(my_array)

print("Sorted Array:", my_array)


