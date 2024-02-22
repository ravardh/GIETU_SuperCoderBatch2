
def max_of_subarrays(nums, n, k):
    result = []

    for i in range(n - k + 1):
        max_in_window = max(nums[i:i+k])
        result.append(max_in_window)

    return result

nums = [3, 6, 7, 2, 1, 8]
result = max_of_subarrays(nums, 6, 2)
print(result)
