def max_potential_locations(locations, compass_range):
    max_locations = 0

    for i in range(len(locations)):
        potential_locations = set()
        for j in range(i - compass_range + 1, i + compass_range):
            if 0 <= j < len(locations):
                potential_locations.add(locations[j])
        max_locations = max(max_locations, len(potential_locations))

    return max_locations

locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
max_locations = max_potential_locations(locations, compass_range)
print("Maximum number of potential treasure locations:", max_locations)
