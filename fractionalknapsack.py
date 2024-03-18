def fractional_knapsack(W, N, PW, PP):
    items = [(PW[i], PP[i], i) for i in range(N)]
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    max_profit = 0
    remaining_weight = W
    selected_items = [0] * N  

    for item in items:
        weight, profit, index = item
        if remaining_weight >= weight:
            selected_items[index] = 1
            max_profit += profit
            remaining_weight -= weight
        else:
            fraction = remaining_weight / weight
            selected_items[index] = fraction
            max_profit += fraction * profit
            remaining_weight = 0
            break  

    return max_profit

W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]
max_profit = fractional_knapsack(W, N, PW, PP)
print("Max Profit:", max_profit)