def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        minId = i
        for j in range(i + 1, n):
            if arr[j] < arr[minId]:
                minId = j
        arr[i], arr[minId] = arr[minId], arr[i]

arr = []
print("Enter the number of elements you want to sort:")
a = int(input())
print("Enter", a , "numbers:")
for i in range(a):
    num = input()
    arr.append(num)
selectionSort(arr)
print("Sorted array is:", arr)
