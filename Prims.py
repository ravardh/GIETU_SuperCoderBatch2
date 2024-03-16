import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  

    def prim_mst(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V
        key[0] = 0

        for _ in range(self.V):
            min_key = sys.maxsize
            for v in range(self.V):
                if key[v] < min_key and not mst_set[v]:
                    min_key = key[v]
                    min_index = v

            mst_set[min_index] = True

            for v in range(self.V):
                if 0 < self.graph[min_index][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[min_index][v]
                    parent[v] = min_index

        mst_weight = 0
        mst_edges = []
        for i in range(1, self.V):
            mst_weight += self.graph[i][parent[i]]
            mst_edges.append((parent[i], i, self.graph[i][parent[i]]))

        return mst_weight, mst_edges


g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst_weight, mst_edges = g.prim_mst()
print("Minimum Spanning Tree Weight:", mst_weight)
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)
