class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

solution = Solution()

nums1 = [1, 2, 0]
print(f"{solution.firstMissingPositive(nums1)}")

nums2 = [3, 4, -1, 1]
print(f"{solution.firstMissingPositive(nums2)}")

nums3 = [7, 8, 9, 11, 12]
print(f"{solution.firstMissingPositive(nums3)}")
