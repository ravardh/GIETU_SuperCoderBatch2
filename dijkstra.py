def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_node)

    return distances

graph = {
    1 : {2 : 4, 8 : 8},
    2 : {1 : 4, 3 : 8, 8 : 11},
    3 : {2 : 8, 9 : 2, 4 : 7},
    4 : {3 : 7, 6 : 14, 5 : 9},
    5 : {4 : 9, 6 : 10},
    6 : {5 : 10, 4 : 14, 7 : 2, 3 : 4},
    7 : {9 : 6, 6 : 2, 8 : 1},
    8 : {7 : 1, 1 : 8, 2 : 11, 9 : 7},
    9 : {3 : 2, 7 : 6, 8 : 7}
}

print(dijkstra(graph, 1))
