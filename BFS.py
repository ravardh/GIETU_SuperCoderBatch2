from collections import deque
def bfs(graph, start):
  visited = set()  # Keep track of visited nodes
  queue = deque([start])  # Use a queue for BFS exploration
  while queue:
    node = queue.popleft()  # Dequeue the first node
    visited.add(node)  # Mark the node as visited
    # Explore unvisited neighbors
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)
  return visited
graph = {
  0: [1, 2],
  1: [0, 3, 4],
  2: [0, 5],
  3: [1],
  4: [1],
  5: [2],
}

starting_node = 0
result = bfs(graph, starting_node)
print("Visited nodes in BFS order:", result)