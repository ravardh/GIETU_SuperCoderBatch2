def max_Profit(length, price):
    N = len(length)
    dp = [0] * (N + 1)
    
    for i in range(1, N + 1):
        max_profit = 0
        for j in range(i):
            max_profit = max(max_profit, price[j] + dp[i - j - 1])
        dp[i] = max_profit
        
    return dp[N]

# Test Cases
length1 = [1, 2, 3, 4, 5, 6, 7, 8]
price1 = [1, 5, 8, 9, 10, 17, 17, 20]
print("Maximum profit for Test Case 1:", max_Profit(length1, price1))  # Output: 22

length2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
price2 = [3, 5, 8, 9, 10, 17, 17, 20, 22, 25, 30, 35]
print("Maximum profit for Test Case 2:", max_Profit(length2, price2))  # Output: 36
