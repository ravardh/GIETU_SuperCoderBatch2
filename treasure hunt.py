def max_treasure_locations(map, compass_range):
    max_locations = 0

    for i in range(len(map)):
        # Define the range of locations to search within the compass range
        start_index = max(0, i - compass_range)
        end_index = min(len(map), i + compass_range + 1)

        # Count the number of potential treasure locations within the range
        potential_locations = end_index - start_index
        max_locations = max(max_locations, potential_locations)
 
    return max_locations
                    
# Example usage
map = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
max_locations = max_treasure_locations(map, compass_range)
print("Maximum number of potential treasure locations:", max_locations)
