def knapSack(weights, price, knapWeight):
    n = len(weights)

    dp = [[0] * (knapWeight + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, knapWeight + 1):
            if weights[i - 1] <= w:

                dp[i][w] = max(price[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    selected_items = []
    w = knapWeight
    for i in range(n, 1, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    return dp[n][knapWeight], selected_items

weights = [2,3,5,7,1,4,1]
price = [10,5,15,7,6,18,3]
knapWeight = 15
maxValue, selected_items = knapSack(weights, price, knapWeight)
print("Maximum price:", maxValue)
print("Selected items:", selected_items)
