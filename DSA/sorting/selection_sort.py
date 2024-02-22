def swap(arr: list, i: int, j: int):
    arr[i], arr[j] = arr[j], arr[i]


def selection_sort(arr: list) -> None:
    for i in range(len(arr) - 1):
        smallestIdx: int = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallestIdx]:
                smallestIdx = j

        swap(arr, i, smallestIdx)
        print(arr)


if __name__ == '__main__':
    arr = [4, 8, 7, 1, 9, 2, 3, 6, 5]
    print(arr)
    selection_sort(arr)
    print(arr)
