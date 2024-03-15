def fractional_knapsack(W, N, w, p):
    u = [(p[i] / w[i], w[i], p[i]) for i in range(N)]
    u.sort(reverse=True)
    t = 0
    r = W
    
    for i in range(N):
        if u[i][1] <= r:
            t += u[i][2]
            r -= u[i][1]
        else:
            f = r / u[i][1]
            t += f * u[i][2]
            break
    
    return t


W = 15
N = 4
w = [5, 10, 10, 5]
p = [10, 5, 5, 10]

print("Max Profit:", fractional_knapsack(W, N, w, p)) 