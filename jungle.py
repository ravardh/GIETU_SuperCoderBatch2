def longest_subarray_with_zero_sum(arr):
    max_length = 0
    cumulative_sum = 0
    sum_index_map = {0: -1}

    for i in range(len(arr)):
        cumulative_sum += arr[i]

        if cumulative_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[cumulative_sum])
        else:
            sum_index_map[cumulative_sum] = i

    return max_length

arr = [9, -3, 3, -1, 6, -5]
result = longest_subarray_with_zero_sum(arr)
print("Result:", result)
