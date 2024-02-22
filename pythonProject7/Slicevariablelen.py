def Maximum_sum(array, variable_length):
    sum_max = float('-inf')
    max_quadrant = None
    for i in range(len(array) - (variable_length - 1)):
        quadrant_sum = sum(array[i:i+variable_length])
        if quadrant_sum > sum_max:
            sum_max = quadrant_sum
            max_quadrant = tuple(array[i:i+variable_length])
    return max_quadrant, sum_max

array = [1, 4, 3, 6, 7, 9, 5, 8]
variable_length = 4
max_quadrant, sum_max = Maximum_sum(array, variable_length)
print("The consecutive quadrant is: ", max_quadrant)
print("Sum of largest quadrant is: ", sum_max)
