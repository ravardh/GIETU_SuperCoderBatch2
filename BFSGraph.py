from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start+1])
    while queue:
        curr = queue.popleft()
        if not visited[curr]:
            print(curr, end=' ')
            visited[curr] = True
            for neighbor, _ in graph[curr]:
                if not visited[neighbor]:
                    queue.append(neighbor)

def createGraph(graph, start, end):
    t = (end)
    graph[start].append(t)

v = 10
graph = [[] for _ in range(v)]

createGraph(graph, 1, 2, 1)
createGraph(graph, 1, 3, 2)
createGraph(graph, 1, 9, 1)
createGraph(graph, 2, 4, 1)
createGraph(graph, 2, 1, 1)
createGraph(graph, 3, 1, 0)
createGraph(graph, 3, 8, 1)
createGraph(graph,4,2,1)
createGraph(graph,4,5,4)
createGraph(graph,4,6,0)
createGraph(graph,5,4,0)
createGraph(graph,6,4,0)
createGraph(graph,6,7,2)
createGraph(graph,7,8,1)
createGraph(graph,7,6,1)
createGraph(graph,8,9,1)
createGraph(graph,8,3,1)
createGraph(graph,8,7,0)
createGraph(graph,9,1,1)
createGraph(graph,9,8,0)

print(graph)

start = 0
bfs(graph, start)
