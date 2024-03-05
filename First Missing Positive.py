def firstMissingPositive(nums):
    var = 1
    for i in nums:
        if i==var:
            var=var+1
    return var

l=[-8]
print(firstMissingPositive(l))