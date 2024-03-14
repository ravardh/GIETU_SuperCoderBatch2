def longest_subarray_with_zero_sum(nums):
    max_length = 0
    sum_indices = {0: -1}   
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum in sum_indices:
            max_length = max(max_length, i - sum_indices[current_sum])
        else:
            sum_indices[current_sum] = i  
    return max_length
nums = [9, -3, 3, -1, 6, -5]
print(longest_subarray_with_zero_sum(nums)) 