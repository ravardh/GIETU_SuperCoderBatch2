
def Maximum_sum(array):
    sum_max=float('-inf')
    max_quadrant = None
    for i in range(len(array)-3):
        quadrant_sum=array[i]+array[i+1]+array[i+2]+array[i+3]
        if quadrant_sum>sum_max:
            sum_max=quadrant_sum
            max_quadrant=(array[i], array[i+1], array[i+2], array[i+3])
    return max_quadrant,sum_max
array=[1,4,3,6,7,9,5,8]
max_quadrant,sum_max=Maximum_sum(array)
print("The consecutive quadrant is: ",max_quadrant)
print("Sum of largest quadrant is: ", sum_max)