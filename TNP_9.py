class Edge:
    def __init__(self,s,d):
        self.source=s
        self.destination=d
class GraphLevelOrder:
    def __init__(self):
            self.l = [[] for _ in range(4)]
    def insertv(self):

        for i in range(4):
            self.l.append([])
        self.l[0].append(Edge(0,1))
        self.l[0].append(Edge(0,2))

        self.l[1].append(Edge(1,2))
        self.l[1].append(Edge(1,3))

        self.l[2].append(Edge(2,3))
        self.l[2].append(Edge(2,1))

        self.l[3].append(Edge(3,2))
        self.l[3].append(Edge(3,3))
    def display(self):
        for i in self.l:
            for j in i:
                print("( ", j.source, " , ", j.destination, " )", end="\t")
            print()
    def LevelOrder(self,queue,visit,current):
        queue.append(current)
        while len(queue)!=0:
                current=queue.pop(0)
                if(visit[current]==False):
                    print(current,end=" ")
                    visit[current]=True
                    for i in range(len(self.l[current])):
                        queue.append(self.l[current][i].destination)
    def graphDfs(self,visit,current):
        if(visit[current]==True):
            return
        print(current,end=" ")
        visit[current]=True
        for i in range(len(self.l[current])):
            self.graphDfs(visit,self.l[current][i].destination)

g=GraphLevelOrder()
visit=[]
queue=[]
for i in range(4):
        visit.append(False)
g.insertv()
g.display()
print("LEVEL ORDER")
for i in range(4):
        if visit[i]==False:
            g.LevelOrder(queue,visit,i)
print("DFS")
g.graphDfs(visit,0)