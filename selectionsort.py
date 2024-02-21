arr=[5,4,1,6,2,3]
def max(arr,start,end):
    m=0
    max_index=0
    for i in range(start,end):
        if(arr[i]>m):
            m=arr[i]
            max_index=i
    return max_index
def SelectionSort(arr):
    for i in range(0,len(arr)):
        last=len(arr)-i-1
        m=max(arr,0,last)
        arr[last],arr[m]=arr[m],arr[last]
print("Before sorting : ",arr)
SelectionSort(arr)
print("After sorting",arr)