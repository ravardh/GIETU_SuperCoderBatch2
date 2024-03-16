def sort(A_L):
    edges = []
    for i, adj_list in enumerate(A_L):
        for j, w in adj_list:
            edges.append((i + 1, j, w))
    edges.sort(key=lambda x: x[2])
    return edges

def Kruskal(A_L):
    sorted_edges = sort(A_L)
    v = len(A_L)
    parent = list(range(v + 1))
    Q = []

    for u, v, w in sorted_edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            Q.append((u, v, w))

    print("Minimum Spanning Tree Edges:")
    for edge in Q:
        print(edge)

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
def union(parent, x, y):
    x_set = find(parent, x)
    y_set = find(parent, y)
    parent[x_set] = y_set
adj_list = [
    [(2, 6), (3, 5), (10, 14)],
    [(1, 14), (4, 24)],
    [(1, 2), (7, 3)],
    [(2, 3), (4, 43), (7, 20), (8, 2)],
    [(4, 2), (5, 2)],
    [(5, 4), (6, 1), (10, 1), (9, 1)],
    [(3, 5), (4, 3), (11, 2)],
    [(4, 5), (8, 11)],
    [(6, 13), (8, 13)],
    [(1, 10), (6, 11)],
    [(7, 18)]
]

Kruskal(adj_list)
