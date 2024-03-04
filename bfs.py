from collections import deque

def bfs(graph, root):
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        visited.add(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph = {
  1 : [2,3,9],
  2 : [1,4],
  3 : [1,8],
  4 : [2,5,6],
  5 : [4],
  6 : [4,7],
  7 : [6,8],
  8 : [3,7,9],
  9 : [1,8]
}

bfs(graph, 1)
