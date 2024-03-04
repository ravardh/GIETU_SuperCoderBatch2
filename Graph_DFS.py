class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
    def DFS(self, v, visited):
        visited.append(v)
        print(v)
        for i in self.graph[v]:
            if i not in visited:
                self.DFS(i, visited)
    def DFS_search(self, v):
        visited = set()
        self.DFS(v, visited)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.DFS_search(2)
