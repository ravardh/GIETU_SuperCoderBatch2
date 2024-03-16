def find_winner(N, K):
    chairs = list(range(1, N + 1))
    index = 0

    while len(chairs) > 1:
        index = (index + K - 1) % len(chairs)
        chairs.pop(index)

    return chairs[0]
N = 14
K = 20
print("Winner:", find_winner(N, K)) 
