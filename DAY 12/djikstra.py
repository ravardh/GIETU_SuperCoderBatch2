def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = []

    while len(visited) < len(graph):
        min_node = None
        min_distance = float('inf')
        for node in graph:
            if node not in visited and distances[node] < min_distance:
                min_node = node
                min_distance = distances[node]

       

    return distances

graph = {
    '1': {'2': 4, '8': 8},
    '2': {'1': 4, '8': 11, '3':8},
    '3': {'2': 8, '4': 7, '9':2},
    '4': {'3': 7, '6': 14, '5':9}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node + ":")
print(shortest_distances)
