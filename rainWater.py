class Solution(object):
    def maxArea(self, height):
        n=len(height)
        left=0
        right=n-1
        maxArea=0
        while(left<right):
            h=min(height[left],height[right])
            w=right-left
            area=h*w
            maxArea=max(area,maxArea)
            if(height[left]<height[right]):
                left+=1
            elif(height[left]>height[right]):
                right-=1
            else:
                left+=1
                right-=1
        return maxArea

        