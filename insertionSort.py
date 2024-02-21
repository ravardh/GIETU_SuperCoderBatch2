arr=[5,4,1,6,2,3]

def InsertionSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if(arr[j]<arr[j-1]):
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
print("Before sorting : ",arr)
InsertionSort(arr)
print("After sorting",arr)