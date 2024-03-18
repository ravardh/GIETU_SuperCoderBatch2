def max_value(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = coins[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(coins[i] - dp[i + 1][j], coins[j] - dp[i][j - 1])

    return dp[0][n - 1] > 0

# Example usage:
coins = [18, 20, 15, 30, 10, 14]
if max_value(coins):
    print("First player wins.")
else:
    print("Second player wins.")