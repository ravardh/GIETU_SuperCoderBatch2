class Solution:
    def maxArea(self, height):
        n = len(height)
        i = 0
        j = n - 1
        maxiArea = 0

        while i < j:
            maxiArea = max(maxiArea, min(height[j], height[i]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxiArea
