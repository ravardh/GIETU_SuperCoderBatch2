def max_locations_with_treasure(jungle_map, compass_range):
    max_locations = 0
    n = len(jungle_map)
    for i in range(n):
        treasure_count = sum(jungle_map[max(0, i - compass_range):min(n, i + compass_range + 1)])
        max_locations = max(max_locations, treasure_count)
    return max_locations
n = int(input("Enter the number of locations in the jungle map: "))
print("Enter the jungle map (0 for no treasure, 1 for treasure) separated by space:")
jungle_map = list(map(int, input().split()))
compass_range = int(input("Enter the range of the magical compass: "))
max_locs = max_locations_with_treasure(jungle_map, compass_range)
print("Maximum number of locations with treasure:", max_locs)