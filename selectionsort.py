def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    for i in range(n):
        print("Sorted array:", arr[i])

# Taking user input
arr = []
for _ in range(5):
    arr.append(int(input("Enter a number: ")))

selectionsort(arr)
