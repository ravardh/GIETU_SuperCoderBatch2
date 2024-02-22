def mergesort(arr, l,r):
    mid = (l+r)/2
    mergesort(arr, l , mid)
    mergesort(arr, mid+1, r)
    merge(arr,l,mid, r)


def merge(arr, l, mid, r):
    i = l
    j = mid + 1
    k = l
    temp = [len(arr)]

    while i <= mid and j <= r:
        if arr[i] < arr[j]:
            temp[k] = arr[i]
            i = i+1

        else:
            temp[k] = arr[j]

    k = k+1


    while j <= r:
        temp[k] = arr[j]
        k = k+1
        j = j+1

    while i <= mid:
        temp[k] = arr[i]
        i = i+1
        k = k+1

    for m in range(0, len(temp)):
        arr[m+l] = temp[m]

# Testing the function  

n = int(input())
arr = [n]
l = 0
r = n-1

for i in range(0,n):
    element = int(input())
    arr.append(element)

mergesort(arr, l, r)
print("Sorted array is")
for i in range(0,n):
    print(arr[i], end="")