def longest_zero_sum_subarray(arr):
    # Create a hashmap to store cumulative sum and its index
    sum_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]

        # If current sum is 0, update max_len to current index + 1
        if curr_sum == 0:
            max_len = i + 1

        # If current sum is already in sum_map, update max_len
        if curr_sum in sum_map:
            max_len = max(max_len, i - sum_map[curr_sum])
        else:
            # Store current sum and its index in sum_map
            sum_map[curr_sum] = i

    return max_len

# Test the function with the provided example
arr = [9, -3, 3, -1, 6, -5]
result = longest_zero_sum_subarray(arr)
print("Length of longest subarray with sum zero:", result)
