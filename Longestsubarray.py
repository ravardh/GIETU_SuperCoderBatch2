def Longest_subarray(arr):
    prefix_sum = 0
    max_length = 0
    sum_index = {}

    for i in range(len(arr)):
        prefix_sum += arr[i]

        if arr[i] == 0 and max_length == 0:
            max_length = 1
        if prefix_sum == 0:
            max_length = i + 1
        if prefix_sum in sum_index:
            max_length = max(max_length, i - sum_index[prefix_sum])
        else:
            sum_index[prefix_sum] = i
    return max_length

arr = [6, 9, -3, 3, -1, 6, -5]
result = Longest_subarray(arr)
print("Result:", result)

