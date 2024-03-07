def knapsack(items, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if items[i - 1][1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], items[i - 1][0] + dp[i - 1][w - items[i - 1][1]])
    included_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(items[i - 1])
            w -= items[i - 1][1]
    return dp[n][capacity], included_items
items = [(18, 4), (15, 5), (7, 7), (10, 2), (6, 1), (5, 3), (3, 1)]
capacity = 15
max_price, included_items = knapsack(items, capacity)
print("Maximum price:", max_price)
print("Included items:")
for price, weight in included_items:
    print("Price:", price, "Weight:", weight)