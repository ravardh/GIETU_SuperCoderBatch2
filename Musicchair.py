def find_winner(N,K):
    children=list(range(1,N+1))
    current_index=0
    while len(children)>1:
        remove_index=(current_index+K-1)%len(children)
        children.pop(remove_index)
        current_index=remove_index
    return children[0]

N = 14
K = 20
print("The winning child is:",find_winner(N,K))