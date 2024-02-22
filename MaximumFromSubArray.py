def max_of_subarrays(arr, n, k):
    array = []
    for i in range(n - k + 1):
        if i + k <= len(arr):
            maximum = max(arr[i:i+k])
            array.append(maximum)
    return array

L=[9,1,5,7,9,4,5,3,6,8]
print(max_of_subarrays(L,len(L),3))
