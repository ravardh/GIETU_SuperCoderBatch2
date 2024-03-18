def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

res=knapsack([2,3,5,7,1,4,1],[10,5,15,7,6,18,3],15)
print(res)

def knapsack(weights, values, capacity):
    n = len(weights)
    # Create a table to store the maximum value that can be obtained with the given capacity
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build up the table using bottom-up dynamic programming
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is less than or equal to the current capacity,
            # we can either include it or exclude it and take the maximum value
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight is greater than the current capacity,
                # we cannot include it
                dp[i][w] = dp[i - 1][w]

    # The maximum value is stored at the bottom-right corner of the table
    return dp[n][capacity]

# Example usage:
weights = [2,3,5,7,1,4,1]
values = [10,5,15,7,6,18,3]
capacity = 15
print("Maximum value that can be obtained:", knapsack(weights, values, capacity))

