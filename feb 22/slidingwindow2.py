arr = list(map(int, input("Enter the array elements : ").split()))
k = int(input("Enter the window size: "))
window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum - arr[i - k] + arr[i]
    max_sum = max(max_sum, window_sum)

print("Maximum sum of subarray of length", k, ":", max_sum)
