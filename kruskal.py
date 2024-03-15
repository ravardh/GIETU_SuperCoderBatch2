class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        self.parent[self.find(vertex1)] = self.find(vertex2)

def kruskal(graph):
    mst = []
    disjoint_set = DisjointSet(graph.keys())
    edges = []

    # Convert adjacency list to list of edges
    for u, neighbors in graph.items():
        for v, weight in neighbors:
            edges.append((weight, u, v))

    edges.sort()

    for weight, u, v in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            disjoint_set.union(u, v)

    return mst

# Example usage:
graph = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('B', 1), ('D', 5), ('E', 6)],
    'D': [('A', 3), ('B', 4), ('C', 5), ('E', 7)],
    'E': [('C', 6), ('D', 7)]
}
mst = kruskal(graph)
print("Minimum Spanning Tree (MST):", mst)
