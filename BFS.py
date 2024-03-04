from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

def BFS(graph, start):
    visited = set()
    queue = deque([start])
    levels = defaultdict(int)
    levels[start] = 0
    while queue:
        node = queue.popleft()
        if node not in visited:
            print("visited node", node, "at level:", levels[node])
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    levels[neighbour] = levels[node] + 1


graph = {
    1:[2,3,9],
    2:[1,4],
    3:[1,8],
    4:[2,5,6],
    5:[4],
    6:[4,7],
    7:[6,8],
    8:[3,7,9],
    9:[1,8]
}
start = 5
BFS(graph,start)


# visited = set()
#     queue = deque[(start)]
#     visited.data(start)
#
#     while queue:
#         vertex = queue.popleft()
#         print(vertex, end=" ")
#
#         for neighbour in graph[vertex]:
#             if neighbour not in visited:
#                 queue.append(neighbour)
#                 visited.add(neighbour)
