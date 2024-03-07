def knapsack(values, weights, capacity):
    n = len(values)
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
           
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
               
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])

  
    included_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            included_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], included_items[::-1]


values = [10, 5, 15, 7, 1, 4, 1]
weights = [2, 3, 5, 7, 6, 18, 3]
capacity = 15
max_value, items = knapsack(values, weights, capacity)
print("Maximum value:", max_value)
