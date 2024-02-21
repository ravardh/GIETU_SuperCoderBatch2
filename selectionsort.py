def selectionSort(array, size):
    for ind in range(size):
        min = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr=[]
n=int(input("Enter the number of elements"))
for i in range(n):
    ele=int(input())
    arr.append(ele)
size = len(arr)
selectionSort(arr, size)
print('The array after sorting')
print(arr)