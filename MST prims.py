import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_val and mst_set[v] is False:
                min_val = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        parent = [None] * self.V
        key = [sys.maxsize] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V - 1):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and mst_set[v] is False:
                    parent[v] = u
                    key[v] = self.graph[u][v]

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


# Example usage:
g = Graph(5)
g.graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

g.prim_mst()
