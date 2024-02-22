def quicksort(array, start, end):
    if start < end:
      seperation = partition(array, start, end)
      (array, start, seperation-1)
      partition(array, seperation+1, end)

def partition(array, start, end):
    pivot = array[end]
    i =  start-1

    for j in range(start,end):
        if array[j] <= pivot:
            i = i + 1
            # swap elements at indices i and j
            array[j], array[i] = array[i], array[j]
    
    array[i+1], array[end] = array[end], array[i+1]

    return i+1
   

array = [3,2,5,2,1,6]
n = len(array)
quicksort(array,0, n-1)
print("sorted array:")
for i in array:
    print(array[i], end=" ")

