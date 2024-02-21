def quick(arr, i, j):
    pivot = arr[j]
    l = i-1
    for k in range(i,j):
        if arr[k]<= pivot:
            l+=1
            # swapping
            c=arr[k]
            arr[k]=arr[l]
            arr[l]=c
    l+=1
    # swapping again
    b=arr[l]
    arr[l]=arr[j]
    arr[j]=b

    return l

def sort(arr,i,j):
    if i<j:
        pivotIdx=quick(arr,i,j)
        sort(arr,i,pivotIdx-1)
        sort(arr,pivotIdx+1,j)




arr=[4,8,7,1,9,2,3,6,5] # initialize list
print(arr) # before sort
sort(arr,0,len(arr)-1)
print(arr) #after sort