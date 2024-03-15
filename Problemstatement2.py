def longest_subarray_with_zero_sum(arr):
    max_length = 0
    n = len(arr)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum == 0:
                max_length = max(max_length, j - i + 1)
    return max_length
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array separated by space:")
arr = list(map(int, input().split()))
result = longest_subarray_with_zero_sum(arr)
print("Result:", result)
