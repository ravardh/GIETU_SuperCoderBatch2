def CreateGraph(graph, start, destination):
    graph[start - 1].append(tuple((start,destination)))

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

v = 9
graph = [[] for _ in range(v)]
for i in range(v):
    graph[i]=[]

CreateGraph(graph, 1, 2)
CreateGraph(graph, 1, 9)
CreateGraph(graph, 1, 3)
CreateGraph(graph, 2, 1)
CreateGraph(graph, 2, 4)
CreateGraph(graph, 3, 1)
CreateGraph(graph, 3, 8)
CreateGraph(graph, 4, 2)
CreateGraph(graph, 4, 6)
CreateGraph(graph, 4, 5)
CreateGraph(graph, 5, 4)
CreateGraph(graph, 6, 4)
CreateGraph(graph, 6, 7)
CreateGraph(graph, 7, 8)
CreateGraph(graph, 7, 6)
CreateGraph(graph, 8, 3)
CreateGraph(graph, 8, 9)
CreateGraph(graph, 8, 7)
CreateGraph(graph, 9, 1)
CreateGraph(graph, 9, 8)
dfs(visited, graph, '5')

