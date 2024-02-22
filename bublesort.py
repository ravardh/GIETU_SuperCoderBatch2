def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
if __name__ == "__main__":
    unsorted_array = [64, 25, 12, 22, 11]
    print("Unsorted Array:", unsorted_array)

    bubble_sort(unsorted_array)

    print("Sorted Array:", unsorted_array)
