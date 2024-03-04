class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m = 1
        for num in nums:
            if num == m:
                m += 1
        return m