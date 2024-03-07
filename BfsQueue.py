def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

graph = {
    '1': ['3', '9','8'],
    '2': ['1', '4' ],
    '3': ['1', '8'],
    '4': ['2','5','6'],
    '5': ['4'],
    '6': ['4', '7'],
    '7': ['6','8'],
    '8': ['3','9','7'],
    '9': ['1','8']
}

print("BFS Traversal of the queue is found:")
bfs(graph, '1')
