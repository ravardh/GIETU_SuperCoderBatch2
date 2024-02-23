def selection(arr,size):
    for i in range(size):
        min_index=i

        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index=j

        (arr[i],arr[min_index])=(arr[min_index],arr[i])

arr=[4,8,7,1,9,2,3,6,5]
size=len(arr)
selection(arr,size)