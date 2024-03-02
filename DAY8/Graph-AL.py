class  edge:
    def __init__(self,start,destination):
        self.start=start
        self.destination=destination
v=9
graph=[[] for _ in range(v)]
for i in range(v):
    graph[i]=[]
def CreateGraph(graph,start,destination):
    graph[start-1].append(tuple((start,destination)))

CreateGraph( graph,1,2)
CreateGraph( graph,1,5)
CreateGraph( graph,1,3)
CreateGraph( graph,2,1)
CreateGraph( graph,2,4)
CreateGraph( graph,3,1)
CreateGraph( graph,3,9)
CreateGraph( graph,4,2)
CreateGraph( graph,4,6)
CreateGraph( graph,4,5)
CreateGraph( graph,5,1)
CreateGraph( graph,5,4)
CreateGraph( graph,5,7)
CreateGraph( graph,5,8)
CreateGraph( graph,5,9)
CreateGraph( graph,6,4)
CreateGraph( graph,6,7)
CreateGraph( graph,7,5)
CreateGraph( graph,7,6)
CreateGraph( graph,8,5)
CreateGraph( graph,9,5)
CreateGraph( graph,9,3)
print(graph)