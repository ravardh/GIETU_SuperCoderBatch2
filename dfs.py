def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited 
graph = {
    '1': set(['2', '3', '9']),
    '2': set(['1', '4']),
    '3': set(['1','8']),
    '4': set(['5', '6']),
    '5': set(['4']),
    '6': set(['4','7']),
    '7': set(['6', '8']),
    '8': set(['3', '7']),
    '9': set(['1', '8'])
}                   
dfs(graph, '1')