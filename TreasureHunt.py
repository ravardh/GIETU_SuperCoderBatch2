def max_potential_locations(map_locations, compass_range):
    max_locations = 0

    for i in range(len(map_locations)):
        count = 0
        for j in range(i, min(i + compass_range + 1, len(map_locations))):
            if map_locations[j] - map_locations[i] <= compass_range:
                count += 1
            else:
                break
        max_locations = max(max_locations, count)

    return max_locations

map_locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 2

max_locations = max_potential_locations(map_locations, compass_range)
print("Maximum number of potential treasure locations:", max_locations)
