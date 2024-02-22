def maximumSum(arr, k):
    if len(arr) < k:
        return "Invalid input: window size is greater than array size"
    
    maxisum = sum(arr[:k])  
    current_sum = maxisum
    
    for i in range(0, len(arr) - k ):
        current_sum = current_sum - arr[i] + arr[i + k ]
        maxisum = max(maxisum, current_sum) 
    
    return maxisum

a = [1,3,5,2,7,4,8,9,5,3,5,7,9,3,2,0]
k = int(input("Size of k is:"))
print("Maximum sum of subarray of size", k, ":", maximumSum(a, k))
