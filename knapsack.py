def knapsack(W, wt, price, n):
   K = [[0] * (W+1) for i in range (n+1)]
   for i in range(n+1):
      for w in range(W+1):
         if(i == 0 or w == 0):
            K[i][w] = 0
         elif(wt[i-1] <= w):
            K[i][w] = max(price [i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
         else:
            K[i][w] = K[i-1][w]
   return K[n][W]

price = [10,5,15,7,6,18,3]
wt = [2,3,5,7,1,4,1]
W = 15
ln = len(price)
profit = knapsack(W, wt, price, ln)
print("Maximum Profit achieved with this knapsack: ")
print(profit)