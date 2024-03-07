def knapsack(values, weights, capacity):
    n = len(values)
    table = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(
                    values[i - 1] + table[i - 1][w - weights[i - 1]],
                    table[i - 1][w]
                )
            else:
                table[i][w] = table[i - 1][w]
                
    return table[n][capacity]



values = [10, 5, 15,7,6,18,3]
weights = [2, 3, 5,7,1,4,1]
capacity = 15

max_value = knapsack(values, weights, capacity)
print("Maximum value that can be obtained:", max_value)
