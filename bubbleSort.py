def bubbleSort(arr):
    for i in range(len(arr)):
        # for round 1 to n-1 
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                (arr[j],arr[j+1])=(arr[j+1],arr[j])

    return arr


print(bubbleSort([4,3,2,1,0]))