def max_sum_of_three_consecutive(arr):
    if len(arr) < 3:
        return "Array should have at least three elements."
    max_sum = sum(arr[:3])
    for i in range(3, len(arr)):
        current_sum = sum(arr[i - 2:i + 1])
        max_sum = max(max_sum, current_sum)

    return max_sum

data =eval(input("enter the elements in the array"))
max_sum_of_three_consecutive(data)
result = max_sum_of_three_consecutive(data)
print("Max Sum of Three Consecutive Numbers:", result)
