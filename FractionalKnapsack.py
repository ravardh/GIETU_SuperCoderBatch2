def Fractional_knapsack(W, N, PW, PP):
    ratio = [(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]

    ratio.sort(reverse=True)

    max_profit = 0

    for r, w, p in ratio:
        if W >= w:
            max_profit += p
            W -= w
        else:
            max_profit += (W / w) * p
            break
    return max_profit

W = int(input("Enter the total weight of the products to carry: "))
N = int(input("Enter the total number of products to choose from: "))
print("Enter the weight of each product:")
PW = list(map(int, input().split()))
print("Enter the profit from each product:")
PP = list(map(int, input().split()))

print("max Profit:", Fractional_knapsack(W, N, PW, PP))
