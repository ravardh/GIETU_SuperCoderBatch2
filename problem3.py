def long_subarray(arr):
    sum_map = {}
    max_length = 0
    curr_sum = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]
        
        if curr_sum == 0:
            max_length = i+1
        if curr_sum in sum_map:
            max_length = max(max_length, i - sum_map[curr_sum])
        else:
            sum_map[curr_sum] = i
    return max_length
arr = [9,-3,3,-1,6,-5]
print("Longest subarray length with sum zero:", long_subarray(arr))