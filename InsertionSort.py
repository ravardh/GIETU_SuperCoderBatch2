def insertionSort(arr):
    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1
        while j >= 0 and num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num
    return  arr

arr = []
print("Enter the number of elements you want to sort:")
a = int(input())
print("Enter", a , "numbers:")
for i in range(a):
    x = input()
    arr.append(x)
insertionSort(arr)
print("Sorted array is:", arr)
