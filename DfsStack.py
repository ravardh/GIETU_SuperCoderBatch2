def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([v for v in graph[vertex] if v not in visited])

    return visited

graph = {
    '1': ['3', '9', '8'],
    '2': ['1', '4'],
    '3': ['1', '8'],
    '4': ['2', '5', '6'],
    '5': ['4'],
    '6': ['4', '7'],
    '7': ['6', '8'],
    '8': ['3', '9', '7'],
    '9': ['1', '8']
}
print("The DFS traversal of this graph is:")
print(dfs(graph, '1'))
