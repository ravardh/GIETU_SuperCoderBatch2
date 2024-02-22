#Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = input("Enter elements of the list separated by space: ").split()
arr = [int(x) for x in arr]

selection_sort(arr)

print("Selection sorted array is:", *arr)
