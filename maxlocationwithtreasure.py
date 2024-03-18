def max_locations_with_treasure(locations, compass_range):
    max_locations = 0
    left = 0
    treasure_locations = set()

    for right in range(len(locations)):
        while locations[right] - locations[left] > compass_range:
            left += 1
        treasure_locations.add(locations[right])
        max_locations = max(max_locations, right - left + 1)

    return max_locations

# Example usage:
locations = [1, 3, 4, 6, 7, 9, 10]
compass_range = 3
print("Maximum number of locations with treasure:", max_locations_with_treasure(locations, compass_range))