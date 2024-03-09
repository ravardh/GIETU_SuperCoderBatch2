def knapsack(items, prices, weights, capacity):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + prices[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(items[i - 1])
            w -= weights[i - 1]

    return result

items = [0, 1, 2, 3, 4, 5, 6]
prices = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
capacity = 15

selected_items = knapsack(items, prices, weights, capacity)
print("Selected items:", selected_items)