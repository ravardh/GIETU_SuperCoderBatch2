class Adjnode:
    def __init__(self,value):
        self.vertex = value
        self.next = None
class Graph:
    def __init__(self,num):
        self.Vertex = num
        self.graph = [None]*self.Vertex
    def Add_edges(self,s,d):
        node = Adjnode(d)
        node.next = self.graph[s]
        self.graph[s] = node
        node = Adjnode(s)
        node.next = self.graph[d]
        self.graph[d] = node
    def print_graph(self):
        for i in range(self.Vertex):
            print("Vertex" + str(i) + ":",end=" ")
            temp = self.graph[i]
            while temp:
                print("-> {}".format(temp.vertex), end=" ")
                temp = temp.next
                print("\n")
if __name__ == "__main__":
    Vertex = 5

    graph = Graph(Vertex)
    graph.Add_edges(0,1)
    graph.Add_edges(0, 2)
    graph.Add_edges(0, 3)
    graph.Add_edges(1, 2)
graph.print_graph()
