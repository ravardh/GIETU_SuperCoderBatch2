class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def BFS(self, s):
        visited = {}
        queue = []
        for vertex in self.graph:
            visited[vertex] = False
        queue.append(s)
        while queue:
            s = queue.pop(0)
            if not visited[s]:
                print(s, end=" ")
                visited[s] = True
                for i in self.graph[s]:
                    if not visited[i]:
                        queue.append(i)


if __name__ == '__main__':
    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 9)
    g.addEdge(2, 1)
    g.addEdge(2, 4)
    g.addEdge(3, 1)
    g.addEdge(3, 8)
    g.addEdge(4, 2)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 4)
    g.addEdge(6, 4)
    g.addEdge(6, 7)
    g.addEdge(7, 6)
    g.addEdge(7, 8)
    g.addEdge(8, 7)
    g.addEdge(8, 3)
    g.addEdge(8, 9)
    g.addEdge(9, 1)
    g.addEdge(9, 8)

    print("Following is Breadth First Traversal (starting from vertex 5)")
    g.BFS(5)
