from numpy import Inf


def Dijkstra(graph, start):
    l = len(graph)

    dist = [Inf for _ in range(l)]

    dist[start] = 1

    visited = [False for _ in range(l)]

    for _ in range(l):

        u = -1

        for x in range(l):
            if not visited[x] and (u == -1 or dist[x] < dist[u]):
                u = x

        if dist[u] == Inf:
            break

        visited[u] = True

        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d

    return dist


graph = {
    '1': {'2': 4, '8': 8},
    '2': {'3': 8, '8': 11, '1': 4},
    '3': {'4': 7, '6': 4, '9': 2, '2': 8},
    '4': {'5': 9, '6': 14, '3': 7},
    '5': {'6': 10, '4': 9},
    '6': {'4': 14, '5': 10, '3': 4},
    '7': {'6': 2, '9': 6, '8': 1},
    '8': {'7': 1, '9': 7, '2': 11, '1': 8},
    '9': {'3': 2, '7': 6, '8': 7},

    #      '1': {'3': 6, '2': 3},
    #      '3': {'4': 5,},
    #      '4': {'2' : -10},
}
c = str(input("Enter starting node : "))
print(dijkstra(graph, c))