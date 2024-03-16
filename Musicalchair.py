def winner_position(N, K):
    if N == 1:
        return 1
    else:
        return (winner_position(N - 1, K) + K - 1) % N + 1
N = 14
K = 20
print(winner_position(N, K))
