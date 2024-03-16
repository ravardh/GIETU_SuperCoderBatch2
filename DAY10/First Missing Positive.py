class Solution:
    def firstMissingPositive(self, nums: List[int]):
        nums=set(nums)
        i=1
        while i in nums:
            i+=1
        return i
nums=[1,3,-7,4]
firstMissingPositive(nums)

        
                
            