def max_treasure_locations(locations, compass_range):
    if not locations:
        return 0
    
    locations.sort()  
    max_count = 1  
    n = len(locations)

    left = 0
    right = 1

    while right < n:
        if locations[right] - locations[left] <= compass_range:
            max_count = max(max_count, right - left + 1)
            right += 1
        else:
            left += 1

    return max_count

locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
max_locations = max_treasure_locations(locations, compass_range)
print("Maximum number of potential treasure locations:", max_locations)
