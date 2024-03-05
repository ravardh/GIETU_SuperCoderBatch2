

def knapsack_bag_capacity(capacity, weights, prices):
    n = len(prices)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(prices[i - 1] + table[i - 1][w - weights[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]

    max_value = table[n][capacity]

    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if table[i][w] != table[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]

    return max_value, included_items

capacity = 15
prices = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]

max_value, included_items = knapsack_bag_capacity(capacity, weights, prices)
print("Maximum value:", max_value)
print("Included items (0-based indices):", included_items)