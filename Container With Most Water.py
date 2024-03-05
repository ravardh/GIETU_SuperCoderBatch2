def maxArea(height):
        # area = 0
        # for i in range(len(height)) :
        #     for j in range(i + 1, len(height)) :
        #         area = max(area, min(height[j], height[i]) * (j - i))
        # return area
    l, r = 0, len(height) - 1
    maxA = 0
    while l < r:
        area = (r - l) * min(height[r], height[l])
        maxA = max(area, maxA)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        
    return maxA
print(maxArea([1,1]))
