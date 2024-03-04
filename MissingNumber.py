class Solution:
    def firstMissingPositive(self, nums):
        maxi = 0
        nums.sort()
        start = 1
        for num in nums:
            if num > 0 and start == num:
                start += 1
            elif num <= 0 or num < start:
                continue
            else:
                return start
        return start
