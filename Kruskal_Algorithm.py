class UnionFind:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

def kruskal_algorithm(graph):
    mst = []  
    vertices = set(graph.keys())
    union_find = UnionFind(vertices)
    edges = []

    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            edges.append((weight, vertex, neighbor))

    edges.sort()  

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if union_find.find(vertex1) != union_find.find(vertex2):
            mst.append((vertex1, vertex2, weight))
            union_find.union(vertex1, vertex2)

    return mst

graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('C', 2)],
    'C': [('B', 2), ('A', 5), ('D', 3)],
    'D': [('C', 3), ('E', 4)],
    'E': [('D', 4)]
}

minimum_spanning_tree = kruskal_algorithm(graph)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
