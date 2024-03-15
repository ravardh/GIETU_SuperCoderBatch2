def find(N, K):
    child=list(range(1, N + 1))
    index=0
    while len(child)>1:
        remove_index=(index+K-1)%len(child)
        del child[remove_index]
        index=remove_index%len(child)
    return child[0]
N = 14
K = 20
print("Winner is:",find(N, K))