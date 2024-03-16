# DFS 

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs(self, start):
        visited = [False] * self.vertices
        stack = [start]

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                print(vertex, end=' ')
                visited[vertex] = True
                for neighbor in reversed(self.adj_list[vertex]):
                    if not visited[neighbor]:
                        stack.append(neighbor)


# Example usage:
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)

print("Depth First Traversal:")
graph.dfs(0)
