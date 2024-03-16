def dijkstra(start,v):
    f=[float('inf') for _ in range(v)]
    print(f)
    f[start-1]=0
    dist=dict()
    while len(f)>=0:
        max=float('inf')
        pos=-1
        for x in range(0,v):
            if(x<max):
                min=x
                pos=pos+1
    print(min)
    print(pos)
    print(f)

def Graph(graph,start,dest,weight=0):
    graph[start-1].append(tuple((start,dest,weight)))
v=9
graph=[[] for _ in range(v)]
for i in range(v):
    graph[i]=[]

Graph(graph,1,2,4)
Graph(graph,1,8,8)
Graph(graph,2,3,8)
Graph(graph,2,8,11)
Graph(graph,2,1,4)
Graph(graph,3,2,8)
Graph(graph,3,9,2)
Graph(graph,3,4,7)
Graph(graph,3,6,4)
Graph(graph,4,6,14)
Graph(graph,4,5,9)
Graph(graph,4,3,7)
Graph(graph,5,4,9)
Graph(graph,5,6,10)
Graph(graph,6,3,4)
Graph(graph,6,5,10)
Graph(graph,6,4,14)
Graph(graph,6,7,2)
Graph(graph,7,9,6)
Graph(graph,7,6,2)
Graph(graph,7,8,1)
Graph(graph,8,1,8)
Graph(graph,8,2,11)
Graph(graph,8,7,1)
Graph(graph,8,9,7)
Graph(graph,9,3,2)
Graph(graph,9,7,6)
Graph(graph,9,8,7)
print(graph)
dijkstra(1,v)
