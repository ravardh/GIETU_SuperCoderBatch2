class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
    def find(self, item):
        if self.parent[item] == item:
            return item
        return self.find(self.parent[item])
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parent[y_root] = x_root
def kruskal_mst(graph):
    num_vertices = len(graph)
    result = []
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    edges.sort(key=lambda x: x[2])
    disjoint_set = DisjointSet(range(num_vertices))
    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            result.append((u, v, weight))
            disjoint_set.union(u, v)
    return result
def print_mst(mst):
    print("Edge \tWeight")
    for edge in mst:
        print(edge[0], "-", edge[1], "\t", edge[2])
def input_graph():
    num_vertices = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix for the graph (Enter 0 if there is no edge):")
    for _ in range(num_vertices):
        row = list(map(int, input().split()))
        graph.append(row)
    return graph
graph = input_graph()
mst = kruskal_mst(graph)
print_mst(mst)