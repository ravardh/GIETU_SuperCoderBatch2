class Edge:
    def __init__(self,start:str,end:str):
        self.start:str=start
        self.end:str=end
class Graph:
    def __init__(self):
        self.adjacency_list:list=[]

    def insert(self,start:str,end:str):
        isThere:bool=False
        index:int=-1
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                if j and j.start==start:
                    isThere=True
                    index=i
                    break

        if isThere and index!=-1:
            self.adjacency_list[index].append(Edge(start,end))
        else:
            self.adjacency_list.append([Edge(start,end)])

    def display(self):
        for i in self.adjacency_list:
            for j in i:
                print("( ", j.start, " , ", j.end, " )", end="\t")
            print()


if __name__ == '__main__':
    graph: Graph = Graph()
    graph.insert("1","2")
    graph.insert("1","5")
    graph.insert("1","4")
    graph.insert("3","2")
    graph.insert("2","5")
    graph.display()