class Edge:
    def _init_(self, start, destination):
        self.start = start
        self.destination = destination


def CreateGraph(graph, start, destination):
    graph[start - 1].append(destination)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    visited[start - 1] = True

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for j in graph[node - 1]:
            if not visited[j - 1]:
                queue.append(j)
                visited[j - 1] = True

v = 9
graph = [[] for _ in range(v)]        
start_node = 1  
print("Breadth First Approach:")
bfs(graph, start_node)