def largest_consecutive_sum(arr, length):
    if length > len(arr) or length <= 0:
        return "Invalid input length"

    max_sum = 0
    max_indices = 0

    for i in range(len(arr) - length + 1):
        current_sum = sum(arr[i:i+length])
        if current_sum > max_sum:
            max_sum = current_sum
            max_indices = (i, i+length-1)

    return max_sum, arr[max_indices[0]:max_indices[1]+1]


array = [1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
input_length = int(input("Enter the length of consecutive numbers: "))
max_sum, subarray = largest_consecutive_sum(array, input_length)
print("Maximum Sum:", max_sum)
print("Subarray with Maximum Sum:", subarray)
