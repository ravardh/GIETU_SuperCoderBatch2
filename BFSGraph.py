class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, curr, v):
        if curr not in self.graph:
            self.graph[curr] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[curr].append(v)
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)
g.BFS(3)
