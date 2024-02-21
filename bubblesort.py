arr=[5,4,1,6,2,3]

def BubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(1,len(arr)-i):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr
print("Before sorting : ",arr)
BubbleSort(arr)
print("After sorting",arr)