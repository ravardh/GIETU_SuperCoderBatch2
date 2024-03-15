class Graph:
    def _init_(self, vertices):
        self.V = vertices
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))
    def bellmanFord(self, src):
        dist = [float('inf')] * self.V
        dist[src - 1] = 0
        for _ in range(self.V - 1):
            for u, v, weight in self.graph:
                if dist[u - 1] != float('inf') and dist[u - 1] + weight < dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + weight
        for u, v, weight in self.graph:
            if dist[u - 1] != float('inf') and dist[u - 1] + weight < dist[v - 1]:
                print("Graph contains negative weight cycle")
                return
        return dist
g = Graph(7)
g.addEdge(1, 2, 6)
g.addEdge(1, 3, 5)
g.addEdge(1, 4, 5)
g.addEdge(2, 5, -1)
g.addEdge(3, 2, -2)
g.addEdge(3, 5, 1)
g.addEdge(4, 3, -2)
g.addEdge(4, 6, -1)
g.addEdge(5, 7, 3)
g.addEdge(6, 7, 3)
src = 1
print("Vertex \t Distance from source")
for i, d in enumerate(g.bellmanFord(src)):
    print(f"{i+1} \t\t {d}")