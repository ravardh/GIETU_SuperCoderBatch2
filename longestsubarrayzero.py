def longest_subarray_with_zero_sum(arr):
    max_length = 0
    sum_map = {}  
    cumulative_sum = 0

    for i in range(len(arr)):
        cumulative_sum += arr[i]

        if cumulative_sum == 0:
            max_length = i + 1

        if cumulative_sum in sum_map:
            max_length = max(max_length, i - sum_map[cumulative_sum])
        else:
            sum_map[cumulative_sum] = i

    return max_length

arr = [9,-3, 3, -1, 6, -5]
print("Length of the longest subarray with sum zero:", longest_subarray_with_zero_sum(arr))