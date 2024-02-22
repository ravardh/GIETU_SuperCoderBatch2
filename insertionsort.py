def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    unsorted_array = [64, 25, 12, 22, 11]
    print("Unsorted Array:", unsorted_array)

    insertion_sort(unsorted_array)

    print("Sorted Array:", unsorted_array)
