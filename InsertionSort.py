def insertionSort(array):
    n = len(array)
    for i in range(1,n):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j],array[j-1] = array[j-1],array[j]
            j = j-1
    return array
array = [40,30,20,10]
insertionSort(array)
print(array) 
