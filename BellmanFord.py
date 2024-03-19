class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []

    def edge(self, u, v, w):
        self.graph.append([u, v, w])
    

    def printArr(self, dist):
        print(self.graph)
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i+1}\t\t{dist[i]}")

    def BellmanFord(self, src):

        dist = [float("Inf")] * self.V
        dist[src-1] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u-1] != float("Inf") and dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w

        self.printArr(dist)



g = Graph(7)
g.edge(1, 2, 6)
g.edge(1, 3, 5)
g.edge(1, 4, 5)

g.edge(2, 5, -1)
g.edge(3, 5, 1)
g.edge(3, 2, -2)

g.edge(4, 6, -1)
g.edge(5, 7, 3)
g.edge(6, 7, 3)

g.BellmanFord(1)


#k008Nx