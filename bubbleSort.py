def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = []
print("Enter the number of elements you want to sort:")
a = int(input())
print("Enter", a , "numbers:")
for i in range(a):
    num = input()
    arr.append(num)
bubbleSort(arr)
print("Sorted array is:", arr)
