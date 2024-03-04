from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                traversal.append(vertex)
                visited.add(vertex)
                if vertex in self.graph:
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return traversal

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal from vertex 2:", g.bfs(2))
