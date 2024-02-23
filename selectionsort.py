def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            
            if array[j] < array[min_index]:
                min_index = j
         
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [3,5,-2,56,-45,67]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)