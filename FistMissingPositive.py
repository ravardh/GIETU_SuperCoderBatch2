class solution(object):
    def firstMissingPositive(self, nums):

        n = len(nums)

        for i in range(n):

         while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
         for i in range(n):
            if nums[i] != i + 1:
              return i + 1
              return n + 1


nums = [1, 2, 0]
sol = solution()
print(sol.firstMissingPositive(nums))
