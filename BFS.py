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
        visited.add(start)

        while queue:
            current_node = queue.popleft()
            print(current_node, end=' ')

            for neighbor in self.graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 6)
print("BFS traversal:")
graph.bfs(1)
