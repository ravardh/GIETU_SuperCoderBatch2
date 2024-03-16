def CreateGraph(graph, start, destination):
    graph[start - 1].append(tuple((start,destination)))

def lo(graph,start):
    vis=[False]*len(graph)
    queue=[]
    queue.append(start)
    vis[start-1]=True
    while queue:
        cur = queue.pop()
        print(cur, end=" ")
        for i in range (0,len(graph[cur - 1])):
            child = graph[cur-1][i][1]
            if not vis[child-1]:
                queue.append(child)
                vis[child-1] = True


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
print(graph)

print("BFS traversal")
start_node = 5 
lo(graph, start_node)

