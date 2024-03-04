def dfs(graph , node , visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)


graph = {
    
    1:[2,3,9],
    2:[1,4],
    3:[1,8],
    4:[2,6,5],
    5:[4],
    6:[4,7],
    7:[6,8],
    8:[3,7,9],
    9:[1,8]
}
dfs(graph, 5)      