def knapSack(W, wt, val, n):
    ratio = [v/w for v, w in zip(val, wt)]
    index = list(range(n))
    index.sort(key = lambda i: ratio[i], reverse = True)
    profit = 0
    items = []
    for i in index:
        if wt[i] <= W:
            W -= wt[i]
            profit += val[i]
            items.append(i)
        else:
            profit += val[i] * W / wt[i]
            break
    return items

val = [10, 5, 15, 7, 6, 18, 3]
wt = [2, 3, 5, 7, 1, 4, 1]
n = len(val)
W = 15

print("Items in Knapsack =", knapSack(W, wt, val, n))
