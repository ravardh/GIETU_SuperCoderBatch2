def bellman_ford(graph, source):
    distances = {node: float('infinity') for node in graph}
    distances[source] = 0
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
    1 : {2 : 6, 3 : 5, 4 : 5},
    2 : {5 : -1},
    3 : {2 : -2, 5 : 1},
    4 : {3 : -2, 6 : -1},
    5 : {7 : 3},
    6 : {7 : 3},
    7 : {}
}

print(bellman_ford(graph, 1))
