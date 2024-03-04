class edge:
    def __init__(self,source,destination):
        self.source=source
        self.destination=destination
def createGraph(graph,start,end,weight):
    graph[start-1].append(tuple())
        
l=[]
l.append(edge(1,2))
l.append(edge(1,3))
l.append(edge(1,5))
l.append(edge(2,1))
l.append(edge(2,4))
l.append(edge(3,1))
l.append(edge(3,9))
l.append(edge(4,2))
l.append(edge(4,6))
l.append(edge(4,5))
l.append(edge(5,1))
l.append(edge(5,9))
l.append(edge(5,8))
l.append(edge(5,7))
l.append(edge(6,4))
l.append(edge(6,7))
l.append(edge(7,6))
l.append(edge(7,5))
l.append(edge(8,5))
l.append(edge(9,3))


















