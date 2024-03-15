def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        cur = min(unvisited, key=lambda n: dist[n])
        unvisited.remove(cur)

        for nbr, weight in graph[cur].items():
            distance = dist[cur] + weight
            if distance < dist[nbr]:
                dist[nbr] = distance

    return dist

graph = [
    ('A', 'B', 6),
    ('A', 'C', 2),
    ('B', 'D', 3),
    ('C', 'B', 1),
    ('C', 'D', 5),
]

start = 'A'
shortest_dist = dijkstra(graph, start)

print("Shortest distances from node", start)
for node, distance in shortest_dist.items():
    print("Node:", node, "Distance:", distance)
