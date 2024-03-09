import sys

class Graph():
    def __init__(self,vertex):
        self.v=vertex
        self.graph = [[0 for column in range(vertex)]for row in range(vertex)]

    def printSoln(self,dist):
        print("vertex \tDistance from Start")
        for node in range(self.v):
            print(f"{node}","\t",dist[node])


    def minDist(self,dist,sptSet):
        # max size a list or iterable can store
        min=sys.maxsize
        for u in range(self.v):
            if u<min and sptSet[u]==False:
                min = dist[u]
                min_index = u
        return min_index
    
    def dijkstra(self,src):
        dist = [sys.maxsize]*self.v
        dist[src]=0
        sptSet = [False]*self.v
        for cout in range(self.v):
            x=self.minDist(dist,sptSet)
            sptSet[x]=True
            for y in range(self.v):
                if self.graph[x][y]>0 and sptSet[y]==False and \
                    dist[y]>dist[x]+self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    
        self.printSoln(dist)


if __name__ == "__main__":
    g = Graph(8)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
 
    g.dijkstra(0)