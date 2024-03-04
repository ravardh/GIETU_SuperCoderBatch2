
def createGraph(graph, start, end, weight):
    t = (start,end,weight)  
    graph[start - 1].append(t)

v = 9
graph = [[] for _ in range(v)]
# for i in range(v):
#     graph[i] = []

createGraph(graph, 1, 2, 1)
createGraph(graph, 1, 3, 1)
createGraph(graph, 1, 5, 1)
createGraph(graph, 2, 4, 1)
createGraph(graph, 3, 9, 1)
print(graph)

#list of list --> Adjacency lists