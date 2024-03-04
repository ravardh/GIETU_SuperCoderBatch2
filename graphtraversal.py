from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * (len(self.graph))
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = [False] * (len(self.graph))
        queue = []

        visited[start] = True
        queue.append(start)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            for neighbor in self.graph[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 9)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(3, 8)
print("DFS traversal starting from vertex 5:")
g.dfs(5)
print("\nBFS traversal starting from vertex 5:")
g.bfs(5)