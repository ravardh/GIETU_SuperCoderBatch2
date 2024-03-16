
def dijkstra(start,v):
    f = [float('inf') for _ in range(v)]
    print(f)
    f[start-1]=0
    dist = dict()
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
        
        



    
def CreateGraph(graph,start,destination,weight=0):
    graph[start-1].append(tuple((start,destination,weight)))


v=9
graph=[[] for _ in range(v)]
for i in range(v):
    graph[i]=[]

CreateGraph( graph,1,2,4)
CreateGraph( graph,1,8,8)
CreateGraph( graph,2,3,8)
CreateGraph( graph,2,8,11)
CreateGraph( graph,2,1,4)
CreateGraph( graph,3,2,8)
CreateGraph( graph,3,9,2)
CreateGraph( graph,3,4,7)
CreateGraph( graph,3,6,4)
CreateGraph( graph,4,6,14)
CreateGraph( graph,4,5,9)
CreateGraph( graph,4,3,7)
CreateGraph( graph,5,4,9)
CreateGraph( graph,5,6,10)
CreateGraph( graph,6,3,4)
CreateGraph( graph,6,5,10)
CreateGraph( graph,6,4,14)
CreateGraph( graph,6,7,2)
CreateGraph( graph,7,9,6)
CreateGraph( graph,7,6,2)
CreateGraph( graph,7,8,1)
CreateGraph( graph,8,1,8)
CreateGraph( graph,8,2,11)
CreateGraph( graph,8,7,1)
CreateGraph( graph,8,9,7)
CreateGraph( graph,9,3,2)
CreateGraph( graph,9,7,6)
CreateGraph( graph,9,8,7)
print(graph)

dijkstra(1,v)