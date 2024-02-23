def partition(array,low,high):
    pivot = array[high]
    i=low-1

    for j in range(low,high):
        if array[j] <= pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])

    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)

data=[1,3,5,9,6,8,4,7,2]
print("Unsorted array")
print(data)

size=len(data)

quicksort(data,0,size-1)

print("Sorted Array")
print(data)