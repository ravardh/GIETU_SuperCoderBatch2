def sorting(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    sorting(arr, n)

    for num in arr:
        print(num, end=' ')

if __name__ == "__main__":
    main()
