def insertionsort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the elements of the array:")
for _ in range(n):
    element = int(input())
    arr.append(element)
insertionsort(arr)
print("Sorted array is:", arr)
