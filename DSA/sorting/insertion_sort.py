def insertion_sort(arr: list) -> None:
    for i in range(1, len(arr)):
        current: int = arr[i]
        j: int = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current
        print(arr)


if __name__ == '__main__':
    arr = [4, 8, 7, 1, 9, 2, 3, 6, 5]
    print(arr)
    insertion_sort(arr)
    print(arr)
