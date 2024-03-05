def knapSack(bag_capacity, weight, profit, n): 
    K = [[0 for x in range(bag_capacity + 1)] for x in range(n + 1)] 
  
    for i in range(n + 1): 
        for w in range(bag_capacity + 1):
            if  i==0 or w==0:
                K[i][w]=0
            elif weight[i-1] <= w: 
                K[i][w] = max(K[i-1][w],K[i-1][w-weight[i-1]]+profit[i-1] ) 
  
    return K[n][bag_capacity] 
  
  
profit = [10, 5, 15, 7, 6, 18, 3] 
weight = [2, 3, 5, 7, 1, 4, 1] 
bag_capacity = 15
n = len(profit) 
print(knapSack(bag_capacity, weight, profit, n)) 