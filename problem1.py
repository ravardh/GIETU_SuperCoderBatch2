def fractional_knapsack(W, N, PW, PP):
    ratios = [(PP[i] / PW[i], i) for i in range(N)]
    ratios.sort(reverse=True)  
    max_profit = 0
    remaining_weight = W
    for ratio, i in ratios:
        weight = min(remaining_weight, PW[i])
        max_profit += ratio * weight
        remaining_weight -= weight
    return max_profit
W = float(input("MEter the weight of products to carry"))
N = int(input("Enter the total number of products to choose fromm"))
print("Enter the weights of each products")
PW = list(map(float,input().split()))
print("Netr the profits for each product")
PP = list(map(float, input().split()))
print(f"Max profit:", fractional_knapsack(W,N,PW,PP))
