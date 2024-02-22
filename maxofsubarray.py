def max_of_subarrays(arr, k):
    if k <= 0 or k > len(arr):
        return "Invalid input for window size"
    
    result = []
    max_val = float('-inf')  
    
    for i in range(k):
        max_val = max(max_val, arr[i])
    result.append(max_val)
    
    
    for i in range(1, len(arr) - k + 1):
        if arr[i - 1] == max_val:  
            max_val = max(arr[i:i + k])  
        elif arr[i + k -1 ] > max_val:  
            max_val = arr[i + k -1]  
        
        result.append(max_val)
    
    return result
arr=[]
n=int(input("Enter the no of array elements:"))
print("Enter the elements:")
for i in range(0,n):
	arr.append(int(input()))
print("The array is:",arr)
k = int(input("Enter the size of subarrays (K): "))
result = max_of_subarrays(arr, k)
print("Maximum of each contiguous subarray of size", k, ":", result)
