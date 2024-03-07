class Graph:
    def __init__(self):
        self.garph = None
        self.graph = {}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        self.garph[u].append(v)
    def DFS_util(self,v,visited):
        visited.add(v)
        print(v, end=" ")

        for neighbour in self.graph.get(v,[]):
            if neighbour not in visited:
                self.DFS_util(neighbour,visited)
    def DFS(self,start):
        visited = set()
        self.DFS_util(start,visited)
if __name__ == "__main__":
    graph = Graph()
graph.graph = {
    1:[2,3,9],
    2:[1,4],
    3:[1,8],
    4:[2,5,6],
    5:[4],
    6:[4,7],
    7:[6,8],
    8:[3,7,9],
    9:[1,8]
}
start= 5
graph.DFS(start)