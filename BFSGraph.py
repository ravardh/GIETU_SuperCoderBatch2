from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if not visited[curr]:
            print(curr, end=' ')
            visited[curr] = True
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)

def createGraph(graph, start, end):
    graph[start].append(end)
    graph[end].append(start)  

v = 10
graph = [[] for _ in range(v)]

createGraph(graph, 1, 2)
createGraph(graph, 1, 3)
createGraph(graph, 1, 9)
createGraph(graph, 2, 4)
createGraph(graph, 2, 1)
createGraph(graph, 3, 1)
createGraph(graph, 3, 8)
createGraph(graph, 4, 2)
def adjacency_list():
    adj_list = []
    vertices = int(input("Enter the number of vertices: "))
    
    for i in range(1, vertices + 1):
        conn = []
        print(f"How many connections does vertex {i} have: ")
        numconn = int(input())
        print(f"Enter the connections for vertex {i} separated by space: ")
        for _ in range(numconn):
            dest = int(input("Destination: "))
            conn.append(tuple((i, dest)))
        adj_list.append(conn)
        
    for i, vertex_connections in enumerate(adj_list, start=1):
        print(f"For vertex {i}:")
        print(vertex_connections)
        
    print("BFS traversal:")
    bfs(adj_list)

def bfs(adj_list):
    visited = {}
    queue = []
    
    for i in range(1, len(adj_list) + 1):
        visited[i] = False
    
    start_vertex = int(input("Enter the starting vertex for BFS: "))
    queue.append(start_vertex)
    visited[start_vertex] = True
    
    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        for connection in adj_list[current - 1]:
            dest = connection[1]
            if not visited[dest]:
                queue.append(dest)
                visited[dest] = True

adjacency_list()
