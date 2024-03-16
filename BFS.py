#BFS w/o using dict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adjacency[u].append(v)

    def bfs(self, start):
        visited = [False] * self.vertices
        queue = []

        visited[start] = True
        queue.append(start)

        while queue:
            start = queue.pop(0)
            print(start, end=' ')

            for i in self.adjacency[start]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)


# Example usage:
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS Traversal:")
g.bfs(2)
