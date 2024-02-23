def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
if __name__ == "__main__":
    unsorted_array = [4,8,7,1,9,2,3,6,5]
    print("Unsorted Array:", unsorted_array)

    selection_sort(unsorted_array)

    print("Sorted Array:", unsorted_array)
