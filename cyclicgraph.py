
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.graph=defaultdict(list)
    def add(self,v,w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    def cycle(self,v,visited,parent):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if(self.cycle(i,visited,v)):
                    return True
                elif parent!=i:
                    return True
            return False
    def cyclic(self):
        visited=[False]*(self.v)
        for i in range(self.v):
            if visited[i]==False:
                if(self.cycle(i,visited,-1))==True:
                    return True
        return False
g=Graph(5)
g.add(1,0)
g.add(1,2)
g.add(4,1)
g.add(2,3)
g.add(5,3)
g.add(3,6)
g.add(4,7)
g.add(7,8)
if g.cyclic():
    print("Graph contains cycle")
else:
    print("Graph doesn't contain cycle ")
