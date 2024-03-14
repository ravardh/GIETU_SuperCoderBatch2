def max_treasure_locations(locations, compass_range):
    max_locations = 0
    for i in range(len(locations)):
        start = max(0, i - compass_range + 1)
        end = min(len(locations), i + compass_range)
        max_locations = max(max_locations, end - start)
    return max_locations
locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
print("Maximum number of potential treasure locations:", max_treasure_locations(locations, compass_range))
