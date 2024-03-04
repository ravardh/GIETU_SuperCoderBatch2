from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

solution = Solution()
nums1 = [1, 2, 0]
nums2 = [3, 4, -1, 1]
nums3 = [7, 8, 9, 11, 12]

print(solution.firstMissingPositive(nums1)) 
print(solution.firstMissingPositive(nums2))  
print(solution.firstMissingPositive(nums3))  