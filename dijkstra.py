import heapq

class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def dijkstra(self, start):
        pq = [(0, start)]
        distances = [float('inf')] * len(self.graph)
        distances[start] = 0

        while pq:
            dist_u, u = heapq.heappop(pq)

            if dist_u > distances[u]:
                continue

            for edge in self.graph:
                if edge[0] == u:
                    v, weight = edge[1], edge[2]
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
                        heapq.heappush(pq, (distances[v], v))

        return distances


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 3, 10)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 7)

    start = 0
    distances = g.dijkstra(start)
    print("Shortest distances from node", start, ":")
    for i, distance in enumerate(distances):
        print("Node", i, ":", distance)
