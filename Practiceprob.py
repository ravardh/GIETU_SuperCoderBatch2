def max_of_subarrays(arr, k):
    n = len(arr)
    result = []

    for i in range(n - k + 1):
        max_in_window = max(arr[i:i+k])
        result.append(max_in_window)

    return result
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = int(input("Enter the window size:"))
print("Maximum for each contiguous subarray of size", k, ":")
print(max_of_subarrays(arr, k))
