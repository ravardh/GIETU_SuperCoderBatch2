class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfs(self,start_node):
        visited = []
        stack = [start_node]

        while stack:
            curr_node = stack.pop()
            if curr_node not in visited:
                print(curr_node)
                visited.append(curr_node)

            for curr in self.graph[curr_node]:
                if curr not in visited:
                    stack.append(curr)


g = Graph()
g.add_edge(5,4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(4,6)
g.add_edge(6,7)
g.add_edge(8,7)
g.add_edge(3,8)
g.add_edge(1,9)
g.add_edge(9,8)
g.dfs(5)