def fractional_knapsack(W, N, PW, PP):
    profit_per_unit_weight = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]

    
    profit_per_unit_weight.sort(reverse=True)

    max_profit = 0
    current_weight = 0

    for ppuw, weight, profit in profit_per_unit_weight:
        if current_weight + weight <= W:
            
            max_profit += profit
            current_weight += weight
        else:
            
            remaining_capacity = W - current_weight
            max_profit += ppuw * remaining_capacity
            break

    return max_profit

# Test case
W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

print("Max Profit:", fractional_knapsack(W, N, PW, PP))
