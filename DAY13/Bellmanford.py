class Edge:
    def __init__(self,s,d,w):
        self.source=s
        self.destination=d
        self.weight=w
class GraphLevelOrder:
    def _init_(self):
            self.l = []
    def insertv(self):
        for i in range(7):
            self.l.append([])
        self.l[0].append(Edge(1,2,6))
        self.l[0].append(Edge(1,3,5))
        self.l[0].append(Edge(1,4,5))


        self.l[1].append(Edge(2,5,-1))

        self.l[2].append(Edge(3,2,-2))
        self.l[2].append(Edge(3,5,1))

       
        self.l[3].append(Edge(4,3,-2))
        self.l[3].append(Edge(4,6,-1))

        self.l[4].append(Edge(5,7,3))

        self.l[5].append(Edge(6,7,3))


        
    def display(self):
        for i in self.l:
            for j in i:
                print("( ", j.source, " , ", j.destination, " )", end="\t")
            print()
    def belMan(self,start):
      dist = dict()
      for x in range(1,len(self.l)+1):
        dist[x]=float('inf')
      dist[start]=0
      for i in range(9):
        for i in range(len(self.l)-1):
          found_key = i+1
          for j in range(len(self.l[found_key-1])):
            dist[self.l[found_key-1][j].destination] = min(dist[self.l[found_key-1][j].destination], dist[found_key] + self.l[found_key-1][j].weight)
      return dist
g=GraphLevelOrder()
g.insertv()
g.display()
start=1
print(g.belMan(start))
