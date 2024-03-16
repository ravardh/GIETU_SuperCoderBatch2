def maxSum(arr, k):
	n = len(arr)
	if n < k:
		print("Invalid")
		return -1

	window_sum = sum(arr[:k])
	max_sum = window_sum


	for i in range(n - k):
		window_sum = window_sum - arr[i] + arr[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum


arr=[1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
k = 3
print(maxSum(arr, k))
