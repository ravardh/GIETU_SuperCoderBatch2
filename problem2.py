def longest_subarray_with_zero_sum(arr):
    prefix_sum=0
    max_length=0
    sum_index={}   
    for i, num in enumerate(arr):
        prefix_sum+=num
        if num==0 and max_length==0:
            max_length=1
        if prefix_sum==0:
            max_length=i+1
        if prefix_sum in sum_index:
            max_length=max(max_length,i-sum_index[prefix_sum])
        else:
            sum_index[prefix_sum]=i
    return max_length   
arr=list(map(int, input().split()))
result=longest_subarray_with_zero_sum(arr)
print("Result:",result)
