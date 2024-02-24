def binarySearch(arr,size,key):
    start = 0
    end = size-1
    mid = (start+end)//2

    while start<=end:
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            start = mid+1
            mid = (start+end)//2
        elif arr[mid]>key:
            end = mid-1
            mid = (start+end)//2

    return -1

even = [2,4,8,12,14,18]
odd = [1,5,7,9,11]
print(binarySearch(odd,5,56))