nums=[1,3,5,2,7,4,3,5,7,9,3,2,0,8,9,5]
k=int(input("Enter the consecutive value"))
result = []
windowsum = sum(nums[:k])
result.append(windowsum)
    
for i in range(1, len(nums) - k + 1):
    windowsum = windowsum - nums[i - 1] + nums[i + k - 1]
    result.append(windowsum)

print(max(result))