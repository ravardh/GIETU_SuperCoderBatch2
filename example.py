
def fractional_knapsack(W, N, PW, PP):
    ratio=[(PP[i] / PW[i], PW[i], PP[i]) for i in range(N)]
    ratio.sort(reverse=True)
    max_profit=0
    for i in range(N):
        if W==0:
            return max_profit
        if ratio[i][1]<=W:
            max_profit+=ratio[i][2]
            W-=ratio[i][1]
        else:
            max_profit+=ratio[i][0] * W
            W=0
    return max_profit
W=15
N=4
PW=[5, 10, 10, 5]
PP=[10, 5, 5, 10]
print("Max Profit:",fractional_knapsack(W, N, PW, PP))
