def treasure_loc(locations, compass_range):
    max_location =  0
    n = len(locations)
    
    for i in range(n - compass_range +1):
        window = set(locations[i:i + compass_range])
        max_location =  max(max_location, len(window))
    return max_location
locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
print("Maximum number of locations with treasures:",treasure_loc(locations, compass_range))
            