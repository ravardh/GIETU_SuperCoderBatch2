def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = []
    while len(visited) < len(graph):
        min_distance = float('infinity')
        min_node = None
        for node in distances:
            if node not in visited and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node
        visited.append(min_node)
        for neighbor, weight in graph[min_node].items():
            distance = min_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    return distances

graph = {
    '1':{'2':4,'8':8},
    '2':{'3':8,'8':11,'1':4},
    '3':{'2':8,'9':2,'6':4,'4':7},
    '4':{'3':7,'6':14,'5':9},
    '5':{'4':9,'6':10},
    '6':{'7':2,'3':4,'4':14,'5':10},
    '7':{'6':2,'9':6,'8':1},
    '8':{'1':8,'2':11,'9':7,'7':1},
    '9':{'3':2,'7':6,'8':7}  
}
start = '1'
result = dijkstra(graph, start)
print(f"Shortest distances from {start}: {result}")
