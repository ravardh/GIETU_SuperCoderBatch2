def selectionsort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [6, 45, 0, 11, 12,88,35,105,91]
size = len(arr)
selectionsort(arr, size)
print(arr)