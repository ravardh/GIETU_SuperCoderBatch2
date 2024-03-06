# v[i,j] = max(v[i-1,w],v[i-1,w-wB]+p[i])
def knapsack(weights,prices,capacity):
    n = len(weights)
    dp = {}

    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w == 0:
                dp[(i,w)] = 0
            elif weights[i-1] <= w:
                dp[(i,w)] = max(dp[(i-1,w)],dp[(i-1,w-weights[i-1])]+prices[i-1])
            else:
                dp[(i,w)] = dp[(i-1,w)]
                
    return dp[(n,capacity)]
                

weights = [2,3,4,5,6]
prices = [3,4,5,6,7]
capacity = 5