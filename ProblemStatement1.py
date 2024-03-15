def fractional_knapsack(W, N, PW, PP):
    max_profit = [0] * (W + 1)
    for i in range(N):
        for j in range(W, PW[i] - 1, -1):
            max_profit[j] = max(max_profit[j], max_profit[j - PW[i]] + PP[i] / PW[i])
    return max_profit[W]
W = int(input("Enter the total weight: "))
N = int(input("Enter the total number of products: "))
print("Enter the weights of the products separated by space:")
PW = list(map(int, input().split()))
print("Enter the profits from the products separated by space:")
PP = list(map(int, input().split()))
max_profit = fractional_knapsack(W, N, PW, PP)
print("Max Profit:", max_profit)
