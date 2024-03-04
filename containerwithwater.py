def max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height1))  # Output: 49

height2 = [1, 1]
print(max_area(height2))  # Output: 1
