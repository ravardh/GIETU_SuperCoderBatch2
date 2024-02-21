def linear_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for _ in range(n - 1):
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        pos = i
        min_val = arr[i]
        for j in range(i, n):
            if min_val > arr[j]:
                min_val = arr[j]
                pos = j
        arr[pos], arr[i] = arr[i], arr[pos]

if __name__ == "__main__":
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    # linear_sort(arr)
    # bubble_sort(arr)
    insertion_sort(arr)

    print(*arr)
