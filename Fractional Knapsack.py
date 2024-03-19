def fractional_knapsack(W, N, PW, PP):
    unit_profit = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    
    print(unit_profit)
    unit_profit.sort(reverse=True)
    print(unit_profit)
    
    max_profit = 0
    
    for unit_price, weight, profit in unit_profit:
        if W >= weight:
            max_profit += profit
            W -= weight
        else:
            fraction = W / weight
            max_profit += fraction * profit
            break
        
    return max_profit

W = int(input("Enter the bag capacity: "))
N = int(input("Enter the number of items in bag: "))
PW = eval(input("Weight of each product: "))
PP = eval(input("Profit from each product: "))

print("Max Profit:", fractional_knapsack(W, N, PW, PP))
