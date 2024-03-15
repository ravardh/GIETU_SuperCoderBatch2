class Edge:
    def __init__(self,s,d,w):
        self.source=s
        self.destination=d
        self.weight=w
class Graph:
    def __init__(self):
            self.l = []
    def insert(self):
        for i in range(7):
            self.l.append([])
        self.l[0].append(Edge(1,2,4))
        self.l[0].append(Edge(1,3,7))
        self.l[0].append(Edge(1,4,3))
        self.l[1].append(Edge(2,5,-3))
        self.l[2].append(Edge(3,2,1))
        self.l[2].append(Edge(3,5,9))
        self.l[3].append(Edge(4,3,-3))
        self.l[3].append(Edge(4,6,5))
        self.l[4].append(Edge(5,7,2))
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
g=Graph()
g.insert()
g.display()
start=1
print(g.belMan(start))