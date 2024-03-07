def firstMissingPositive(nums):
        nums.sort()
        var = 1
        for i in nums:
            if i == var:
                var += 1
        return var
nums=[]
n=int(input("enter the no of element:-"))
print("enter the elements to array:-")
for i in range (0,n):
    nums.append(int(input()))
result =firstMissingPositive(nums)
print("The minimum missing +ve integer is:-",result)
