def MainQuick(array, start, end):
    if start < end:
        pivot = quickSort(array, start, end)
        MainQuick(array, start, pivot - 1)
        MainQuick(array, pivot + 1, end)
def quickSort(array, start, end):
    pivot = array[end]
    j = start - 1
    for i in range(start, end):
        if array[i] < pivot:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[end], array[j + 1] = array[j + 1], array[end]
    return j + 1

n = int(input("Enter the number of elements: "))
array = []
for i in range(0, n):
    array.append(int(input()))

print("Before Sorting:", array)
MainQuick(array, 0, n - 1)
print("After Sorting:", array)
