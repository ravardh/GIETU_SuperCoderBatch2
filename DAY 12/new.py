def shortestPath(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    visited = []
    while len(visited) < len(graph):
        min_distance = float('infinity')
        min_vertex = None
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        visited.append(min_vertex)

        for neighbor, weight in graph[min_vertex].items():
            distance = distances[min_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    return distances


graph = {
    '1': {'2': 4, '8': 8},
    '2': {'1': 4, '8': 11, '3': 8},
    '3': {'2': 8, '9': 2, '4': 7},
    '4': {'3': 7, '6': 14, '5': 9},
    '5': {'4': 9, '6': 10},
    '6': {'7': 2, '3': 4, '4': 14, '5': 10},
    '7': {'8': 1, '9': 6, '6': 2},
    '8': {'1': 8, '2': 11, '9': 7, '7': 1},
    '9': {'8': 7, '3': 2, '7': 6}
}

print(shortestPath(graph, '1'))
