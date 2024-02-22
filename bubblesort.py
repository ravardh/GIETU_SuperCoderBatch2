def sorting(arr, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sorting(arr, n)

    for num in arr:
        print(num, end=' ')

if __name__ == "__main__":
    main()
