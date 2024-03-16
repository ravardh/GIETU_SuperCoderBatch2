def find_winner(N, K):
    chairs = list(range(1, N + 1))
    current_position = 0
    while len(chairs) > 1:
        next_position = (current_position + K-1) % len(chairs)
        chairs.pop(next_position)
        current_position = next_position
    return chairs[0]
N = 14
K = 20
print(find_winner(N, K))
