def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j=i-1
        for j in range(i-1,-2,-1):
            if arr[j]>temp:
                arr[j+1]=arr[j]
            else:
                break
        arr[j+1] = temp
    return arr

print(insertionSort([4,3,2,1,0,9]))