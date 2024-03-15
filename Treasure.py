def max_treasure_locations(l,compass_range):
    max_l=0
    for i in range(len(locations)):
        s=max(0, i-compass_range+1)
        e=min(len(locations), i+compass_range)
        max_l=max(max_l,e-s)
    return max_l
locations = [2, 7, 1, 4, 8, 3, 5]
compass_range = 3
print("Maximum number of potential treasure locations:", max_treasure_locations(locations, compass_range))