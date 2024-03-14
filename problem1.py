def knapsack(W,N,PW,PP):
    PPW = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    PPW.sort(reverse=True)
    
    grt_profit = 0
    total_weight = 0
    
    for ppw,weight,profit in PPW:
        if total_weight + weight <= W:
            total_weight += weight
            grt_profit += profit
        else:
            fractionn = (W - total_weight) / weight
            grt_profit += fractionn * profit
            break
    return grt_profit

W= 15
N= 4
PW = [5,10,10,5]
PP = [10,5,5,10]
print("Greate Profit:", knapsack(W,N,PW,PP))