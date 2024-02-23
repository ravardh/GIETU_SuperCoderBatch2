#Sliding Window
def max_sum_subarray(a, k):
    if k > len(a):
        return "k is greater than length of array"
    
    max_sum = sum(a[:k])  
    win_sum = max_sum 
    
    for i in range(len(a) - k):  
        win_sum = win_sum - a[i] + a[i + k]  
        max_sum = max(max_sum, win_sum)  
        
    return max_sum

a=[]
n=int(input("Enter the size of array: "))
for i in range(n):
    e=int(input())
    a.append(e)
k = int(input("Enter the value of k: "))
print("Maximum sum of subarray of length", k, ":", max_sum_subarray(a, k))