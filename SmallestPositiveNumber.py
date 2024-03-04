class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        result = 1
        
        for i in range(len(nums)):
            if nums[i] <= 0 or (i > 0 and nums[i] == nums[i - 1]):
                continue
            
            if nums[i] != result:
                return result
            
            result += 1
        
        return result
