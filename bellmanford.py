class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])
    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")
V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))
graph = Graph(V)
print("Enter the edges (source, destination, weight):")
for _ in range(E):
    u, v, w = map(int, input().split())
    graph.add_edge(u, v, w)
src = int(input("Enter the source vertex: "))
graph.bellman_ford(src)