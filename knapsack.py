def knapsack(W,N,PW,PP):
    items=[]
    for i in range(N):
        items.append((PP[i]/PW[i],PW[i],PP[i]))
    items.sort(reverse=True)
    totalWeight=0
    totalProfit=0
    for fra,w,p in items:
        if totalWeight+w<=W:
            totalWeight+=w
            totalProfit+=p
        else:
            rem=W-totalWeight
            fract=rem/w
            totalProfit +=fract*p
            break
    return totalProfit
W=15
N=4
PW=[5, 10, 10, 5]
PP=[10, 5, 5, 10]
max_profit=knapsack(W,N,PW,PP)
print("Maximum Profit:-",max_profit)
