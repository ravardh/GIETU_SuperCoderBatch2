import sys


class Edge:
    def __init__(self, start: str, end: str, weight: int):
        self.start: str = start
        self.end: str = end
        self.weight: int = weight

    def __str__(self):
        return f'{{ {self.start} --> {self.end}, weight : {self.weight} }}'


class Graph:
    def __init__(self):
        self.adjacency_list: list = []

    def insert(self, start: str, end: str, weight: int):
        isThere: bool = False
        index: int = -1
        for i in range(len(self.adjacency_list)):
            if self.adjacency_list[i][0] and self.adjacency_list[i][0].start == start:
                isThere = True
                index = i

        if isThere and index != -1:
            self.adjacency_list[index].append(Edge(start, end, weight))
        else:
            self.adjacency_list.append([Edge(start, end, weight)])

    def shortest_path(self):
        records: dict = {}
        edges: list = []

        for row in self.adjacency_list:
            for edge in row:
                edges.append(edge)
                if edge.start not in records:
                    records[edge.start] = sys.maxsize
                if edge.end not in records:
                    records[edge.end] = sys.maxsize

        records["1"] = 0
        
        for i in range(len(records.keys()) - 1):
            for edge in edges:
                spend: int = records[edge.start]
                if records[edge.end] > spend + edge.weight:
                    records[edge.end] = spend + edge.weight

        print(records)

    def display(self):
        for row in self.adjacency_list:
            for edge in row:
                print(edge, end="\t")
            print()


if __name__ == '__main__':
    graph: Graph = Graph()

    graph.insert("1", "2", 6)
    graph.insert("1", "5", 3)
    graph.insert("1", "4", 5)

    graph.insert("2", "5", -1)

    graph.insert("3", "2", -2)
    graph.insert("3", "5", 3)

    graph.insert("4", "3", -2)
    graph.insert("4", "6", -1)

    graph.insert("5", "7", 3)

    graph.insert("6", "7", 3)

    # graph.display()
    graph.shortest_path()
