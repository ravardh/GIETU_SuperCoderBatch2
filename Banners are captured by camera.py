def noOfBanners(building_heights):
    if len(building_heights) <= 1:
        return len(building_heights)

    banners = 1
    max_height = building_heights[0]

    for height in building_heights[1:]:
        if height > max_height:
            banners += 1
            max_height = height

    return banners

# Test Cases
heights1 = [10, 15, 20, 10, 12]
print("Test Case 1:", noOfBanners(heights1))  # Output: 3

heights2 = [8, 8, 8, 8, 8]
print("Test Case 2:", noOfBanners(heights2))  # Output: 1

heights3 = [5, 10, 5, 15, 5, 20]
print("Test Case 3:", noOfBanners(heights3))  # Output: 4

heights4 = [25, 15, 30, 20, 25]
print("Test Case 4:", noOfBanners(heights4))  # Output: 2
