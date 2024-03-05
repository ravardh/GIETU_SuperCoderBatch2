def knapSack(weights, price, k):
    n = len(weights)

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, k + 1):
            if weights[i - 1] <= w:

                dp[i][w] = max(price[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    arr=[]
    w = k
    for i in range(n, 1, -1):
        if dp[i][w] != dp[i - 1][w]:
            arr.append(i - 1)
            w -= weights[i - 1]
    return dp[n][k], arr

weights = [2,3,5,7,1,4,1]
price = [10,5,15,7,6,18,3]
knapWeight = 15
maxi, items = knapSack(weights, price, knapWeight)
print("Maximum price:",maxi)
print("Selected items:",items)