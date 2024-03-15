def fractional_knapsack(W, N, PW, PP):
    # Calculate profit-to-weight ratio for each product
    ratio = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    
    # Sort products by profit-to-weight ratio in descending order
    ratio.sort(reverse=True)
    
    max_profit = 0
    
    for i in range(N):
        if W == 0:
            return max_profit
        # Take the whole product if its weight is less than or equal to remaining capacity
        if ratio[i][1] <= W:
            max_profit += ratio[i][2]
            W -= ratio[i][1]
        else:
            # Take a fraction of the product if its weight is more than remaining capacity
            max_profit += ratio[i][0] * W
            W = 0

    return max_profit

# Test case
W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

print("Max Profit:", fractional_knapsack(W, N, PW, PP))
