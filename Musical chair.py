def find_winner(N, K):
    children = list(range(1, N + 1))
    index = 0
    while len(children) > 1:
        index = (index + K - 1) % len(children)
        del children[index]
    return children[0]

N = 14
K = 20
print(find_winner(N, K))
