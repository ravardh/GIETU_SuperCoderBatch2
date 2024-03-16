def min_key(key, mst_set):
    min_val = float('inf')
    min_index = None
    for v in range(len(key)):
        if key[v] < min_val and not mst_set[v]:
            min_val = key[v]
            min_index = v
    return min_index
def prim_mst(graph):
    num_vertices = len(graph)
    key_values = [float('inf')] * num_vertices
    mst = [None] * num_vertices
    mst_set = [False] * num_vertices
    key_values[0] = 0
    mst[0] = -1
    for _ in range(num_vertices):
        u = min_key(key_values, mst_set)
        mst_set[u] = True
        for v in range(num_vertices):
            if graph[u][v] > 0 and not mst_set[v] and key_values[v] > graph[u][v]:
                key_values[v] = graph[u][v]
                mst[v] = u
    print_mst(mst, graph)
def print_mst(mst, graph):
    print("Edge \tWeight")
    for i in range(1, len(mst)):
        print(mst[i], "-", i, "\t", graph[i][mst[i]])
def input_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix for the graph (Enter 0 if there is no edge):")
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph
graph = input_graph()
prim_mst(graph)