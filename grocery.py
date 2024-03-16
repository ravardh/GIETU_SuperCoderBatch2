def fractional_knapsack(W, N, PW, PP):
    items = [(PW[i], PP[i], i) for i in range(N)]
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    max_profit = 0
    remaining_weight = W

    for weight, profit, index in items:
        if remaining_weight >= weight:
            max_profit += profit
            remaining_weight -= weight
        else:
            fraction = remaining_weight / weight
            max_profit += fraction * profit
            break

    return max_profit

W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

max_profit = fractional_knapsack(W, N, PW, PP)
print("Max Profit:", max_profit)
