def find_max_locations(locations, compass_range):
    n = len(locations)
    max_locations = 0
    current_range = 0

    for i in range(n):
        if i <= current_range:
            current_range = max(current_range, i + compass_range)
            max_locations = i + 1
        else:
            break 
    return max_locations
locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3

result = find_max_locations(locations, compass_range)
print(f"Maximum number of potential treasure locations: {result}")
