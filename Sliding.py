def sliding_window(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid input"

    result = []
    max_sum = sum(arr[:k])
    result.append(max_sum)

    for i in range(1, n - k + 1):
        max_sum = max_sum - arr[i - 1] + arr[i + k - 1]
        result.append(max_sum)
    return result
arr_str = input("Enter the array elements: ")
arr = list(map(int, arr_str.split()))
k = int(input("Enter the window size: "))
result = sliding_window(arr, k)
print("Resulting sliding window sums:",result)