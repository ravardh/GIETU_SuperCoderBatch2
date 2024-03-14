import heapq
import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.edges = []

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
        self.edges.append((u, v, w))

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distances = [float('inf')] * graph.V
        self.visited = [False] * graph.V
        self.pq = []

    def shortest_path(self, src):
        self.distances[src] = 0
        heapq.heappush(self.pq, (0, src))

        while self.pq:
            weight, node = heapq.heappop(self.pq)
            if self.visited[node]:
                continue
            self.visited[node] = True

            for child, child_weight in self.graph.graph[node]:
                if self.distances[child] > child_weight + weight:
                    self.distances[child] = child_weight + weight
                    heapq.heappush(self.pq, (self.distances[child], child))

class ShortestDistance:
    def __init__(self, graph):
        self.graph = graph

    def shortest_distances_from_source(self, src):
        dijkstra = Dijkstra(self.graph)
        dijkstra.shortest_path(src)
        return dijkstra.distances

if __name__ == "__main__":
    N, M = 9, 14

    g = Graph(N)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 2, 8)
    g.add_edge(2, 3, 7)
    g.add_edge(3, 4, 9)
    g.add_edge(4, 5, 10)
    g.add_edge(5, 6, 2)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 0, 8)
    g.add_edge(1, 7, 11)
    g.add_edge(7, 8, 7)
    g.add_edge(2, 8, 2)
    g.add_edge(6, 8, 6)
    g.add_edge(2, 5, 4)
    g.add_edge(3, 5, 14)

    shortest_dist = ShortestDistance(g)
    for i in range(N):
        shortest_distances = shortest_dist.shortest_distances_from_source(i)
        print(f"Node {i}: ", end="")
        for j, distance in enumerate(shortest_distances):
            if distance != float('inf'):
                print(f"{j}:{distance}", end=", ")
        print()
