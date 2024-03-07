def knapsack(weights, value, capacity):
    n = len(weights)
    sorted_items = sorted([(weights[i], value[i], i) for i in range(n)], key=lambda x: x[1] / x[0], reverse=True)

    max_value = 0
    selected_items = []
    for weight, value, index in sorted_items:
        if capacity >= weight:
            max_value += value
            selected_items.append(index)
            capacity -= weight

    return max_value, selected_items

n = int(input("Enter the number of items: "))
weights = []
values = []
for i in range(n):
    weight = int(input(f"Enter the weight of item {i + 1}: "))
    value = int(input(f"Enter the value of item {i + 1}: "))
    weights.append(weight)
    values.append(value)

capacity = int(input("Enter the capacity of the knapsack: "))

max_value, selected_items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Selected items:", selected_items)

