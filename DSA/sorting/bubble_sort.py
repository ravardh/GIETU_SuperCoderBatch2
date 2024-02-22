def swap(arr: list, i: int, j: int) -> None:
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr: list) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
        print(arr)


if __name__ == '__main__':
    arr = [4, 8, 7, 1, 9, 2, 3, 6, 5]
    print(arr)
    bubble_sort(arr)
    print(arr)
