def swap(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, st, end) -> int:
    pivot: int = arr[end]
    j = st - 1
    for i in range(st, end):
        if arr[i] <= pivot:
            j += 1
            swap(arr, i, j)

    swap(arr, j + 1, end)
    print(arr)
    return j + 1


def quick_sort(arr, st, end) -> None:
    if st < end:
        pivot = partition(arr, st, end)
        quick_sort(arr, st, pivot - 1)
        quick_sort(arr, pivot + 1, end)


if __name__ == '__main__':
    arr = [4, 8, 7, 1, 9, 2, 3, 6, 5]
    print(arr)
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)