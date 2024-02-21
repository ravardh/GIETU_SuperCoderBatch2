def conquer(arr: list, st: int, end: int, mid: int) -> None:
    newArr: list = []
    idx_1: int = st
    idx_2: int = mid + 1
    x: int = 0

    while idx_1 <= mid and idx_2 <= end:
        if arr[idx_1] <= arr[idx_2]:
            newArr.append(arr[idx_1])
            idx_1 += 1
        else:
            newArr.append(arr[idx_2])
            idx_2 += 1

    while idx_1 <= mid:
        newArr.append(arr[idx_1])
        idx_1 += 1

    while idx_2 <= end:
        newArr.append(arr[idx_2])
        idx_2 += 1
    j: int = st
    for i in range(len(newArr)):
        arr[j] = newArr[i]
        j += 1

    print(arr)


def divide(arr: list, st: int, end: int) -> None:
    if st < end:
        mid: int = (st + end) // 2
        divide(arr, st, mid)
        divide(arr, mid + 1, end)
        conquer(arr, st, end, mid)


if __name__ == '__main__':
    arr: list = [4, 8, 7, 1, 9, 2, 3, 6, 5]
    print(arr)
    divide(arr, 0, len(arr) - 1)
    print(arr)