def knapsack_fractional(W, N, w, p):
    items = sorted([(p[i] / w[i], w[i], p[i]) for i in range(N)], reverse=True)
    mp = 0
    cw = 0
    for d, wt, pr in items:
        if cw + wt <= W:
            mp += pr
            cw += wt
        else:
            rw = W - cw
            mp += d * rw
            break
    return mp


W = 15
N = 4
w = [5, 10, 10, 5]
p = [10, 5, 5, 10]

print("Max Profit:", knapsack_fractional(W, N, w, p))
