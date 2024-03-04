from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
graph = {
    '1': ['2', '3', '9'],
    '2': ['1', '4'],
    '3': ['1','8'],
    '4': ['5', '6'],
    '5': ['4'],
    '6': ['4','7'],
    '7': ['6', '8'],
    '8': ['3', '7'],
    '9': ['1', '8']
}                
start_vertex = input("Enter the starting vertex for BFS:")
print("BFS Traversal:")
bfs(graph, start_vertex)