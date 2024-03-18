def fractional_knapsack(W, N, PW, PP):
    items = [(PW[i], PP[i]) for i in range(N)]
    items.sort(key=lambda x: x[1]/x[0], reverse=True)
    
    total_profit = 0
    total_weight = 0

    for weight, profit in items:
        if total_weight + weight <= W:
            total_weight += weight
            total_profit += profit
        else:
            fraction = (W - total_weight) / weight
            total_profit += fraction * profit
            break

    return total_profit

W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

max_profit = fractional_knapsack(W, N, PW, PP)
print("Max Profit:", max_profit)



