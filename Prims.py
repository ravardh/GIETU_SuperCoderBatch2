from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight))  # Undirected graph

    def prim_mst(self, start):
        visited = set()
        min_heap = [(0, start)]  # (weight, node)
        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, node = heapq.heappop(min_heap)
            if node not in visited:
                visited.add(node)
                mst_weight += weight
                for neighbor, neighbor_weight in self.adj_list[node]:
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (neighbor_weight, neighbor))
                        mst_edges.append((node, neighbor, neighbor_weight))

        return mst_weight, mst_edges

# Example usage:
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 3)

start_node = 'A'
mst_weight, mst_edges = g.prim_mst(start_node)
print("Minimum Spanning Tree Weight:", mst_weight)
print("Minimum Spanning Tree Edges:")
for edge in mst_edges:
    print(edge)
