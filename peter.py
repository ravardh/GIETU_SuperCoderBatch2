def fractional_knapsack(W, N, PW, PP):
    profitPerUnit = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    profitPerUnit.sort(reverse=True)
    maxProfit = 0
    
    for unitProfit, weight, profit in profitPerUnit:
        if W >= weight:
            maxProfit += profit
            W -= weight
        else:
            fraction = W / weight
            maxProfit += fraction * profit
            break
            
    return maxProfit

W = float(input("Enter the total weight of the products to carry: "))
N = int(input("Enter the total number of products to choose from: "))
print("Enter the weights of each product:")
PW = list(map(float, input().split()))
print("Enter the profits from each product:")
PP = list(map(float, input().split()))

print("Max Profit:", fractional_knapsack(W, N, PW, PP))
