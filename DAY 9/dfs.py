class Edge:
    def _init_(self, start, destination):
        self.start = start
        self.destination = destination



def CreateGraph(graph, start, destination):
    graph[start - 1].append(destination)

def Bfs(graph, start):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    visited[start - 1] = True

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbor in graph[node - 1]:
            if not visited[neighbor - 1]:
                queue.append(neighbor)
                visited[neighbor - 1] = True

def Dfs(graph,start,destination):
    if start  in visited:
        pass
    visited[start]=True
    for neighbor in graph[start - 1]:
            if not visited[neighbor - 1]:
                Dfs(destination)
    print(start)            





v = 9
graph = [[] for _ in range(v)]
CreateGraph(graph, 1, 2)
CreateGraph(graph, 1, 5)
CreateGraph(graph, 1, 3)
CreateGraph(graph, 2, 1)
CreateGraph(graph, 2, 4)
CreateGraph(graph, 3, 1)
CreateGraph(graph, 3, 9)
CreateGraph(graph, 4, 2)
CreateGraph(graph, 4, 6)
CreateGraph(graph, 4, 5)
CreateGraph(graph, 5, 1)
CreateGraph(graph, 5, 4)
CreateGraph(graph, 5, 7)
CreateGraph(graph, 5, 8)
CreateGraph(graph, 5, 9)
CreateGraph(graph, 6, 4)
CreateGraph(graph, 6, 7)
CreateGraph(graph, 7, 5)
CreateGraph(graph, 7, 6)
CreateGraph(graph, 8, 5)
CreateGraph(graph, 9, 5)
CreateGraph(graph, 9, 3)

start_node = 1  
print("Breadth First Approach:" )
Bfs(graph, start_node)
print("Depth First Approach:")
Dfs(graph,start_node)