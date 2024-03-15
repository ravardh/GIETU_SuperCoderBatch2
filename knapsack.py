
def knapsack(w, v, cp):
  n = len(w)
  dp = [[0 for _ in range(cp + 1)] for _ in range(n + 1)]
  for i in range(1, n + 1):
    for j in range(1, cp + 1):
      if w[i - 1] <= j:
        dp[i][j] = max(dp[i - 1][j], v[i - 1] + dp[i - 1][j - w[i - 1]])
      else:
        dp[i][j] = dp[i - 1][j]
  return dp[n][cp]

w = [2, 3, 1, 4]
v = [4, 5, 3, 7]
cp = 6

max_value = knapsack(w, v, cp)
print("max value",max_value)