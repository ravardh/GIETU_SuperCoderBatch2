def knapsack(items, prices, weights, max_weight):
    n = len(items)
    ratios = [(prices[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    selected_items = []
    current_weight = 0

    for ratio, index in ratios:
        if current_weight + weights[index] <= max_weight:
            current_weight += weights[index]
            total_value += prices[index]
            selected_items.append(items[index])

    return total_value, selected_items

items = [0, 1, 2, 3, 4, 5, 6]
prices = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
max_weight = 15

total_value, selected_items = knapsack(items, prices, weights, max_weight)

print("Selected items:", selected_items)
print("Total value:", total_value)
