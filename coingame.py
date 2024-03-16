def coin_game(coins):
    n = len(coins)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = coins[i]
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = max(coins[i] - dp[i + 1][j], coins[j] - dp[i][j - 1])

    if dp[0][n - 1] > 0:
        return "First player wins."
    elif dp[0][n - 1] < 0:
        return "Second player wins."
    else:
        return "It's a draw."

coins = [18, 20, 15, 30, 10, 14]
print(coin_game(coins))  
