def fractional_knapsack(W, N, PW, PP):
    # Calculate profit-to-weight ratio for each product
    ratio = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    
    # Sort the products based on profit-to-weight ratio in descending order
    ratio.sort(reverse=True)
    
    total_profit = 0.0
    remaining_weight = W
    
    # Iterate through the sorted products
    for i in range(N):
        # If the weight of the current product is less than or equal to remaining weight,
        # take the whole product and subtract its weight from remaining weight
        if ratio[i][1] <= remaining_weight:
            total_profit += ratio[i][2]
            remaining_weight -= ratio[i][1]
        else:
            # If the weight of the current product is more than remaining weight,
            # take a fraction of it to fill the remaining weight
            total_profit += ratio[i][0] * remaining_weight
            break  # No more items can be added
        
    return total_profit

# Test the function with the given example
W = 15
N = 4
PW = [5, 10, 10, 5]
PP = [10, 5, 5, 10]

max_profit = fractional_knapsack(W, N, PW, PP)
print("Max Profit:", max_profit)
