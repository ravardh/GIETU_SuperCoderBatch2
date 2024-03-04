from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    levels = defaultdict(int)
    levels[start] = 0

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print("Visited vertex:", vertex, "at level:", levels[vertex])
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    levels[neighbor] = levels[vertex] + 1




graph = {
    1: [2, 3, 9],
    2: [1, 4],
    3: [1,8],
    4: [2,5,6],
    5: [4],
    6:[4,7],
    7:[6,8],
    8:[3,7,9],
    9:[1,8]
}

start_vertex = 5  
print("BFS traversal starting from node", start_vertex)
bfs(graph, start_vertex)

