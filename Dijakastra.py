import sys
class Edge:
    def __init__(self, start: str, end: str, weight: int):
        self.start: str = start
        self.end: str = end
        self.weight: int = weight
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
    def display(self):
        for row in self.adjacency_list:
            for edge in row:
                print(edge, end="\t")
            print()
    def __find_dest(self, vertex: str) -> list:
        destinations: list = []
        for i in self.adjacency_list:
            for j in i:
                if j.start == vertex:
                    destinations.append(j.end)
        return destinations
    def __find_distance(self, start: str, end: str) -> int:
        for row in self.adjacency_list:
            if row[0].start == start:
                for edge in row:
                    if edge.end == end:
                        return edge.weight
    def minimum_distance(self) -> None:
        history: dict = {}
        records: dict = {}
        for row in self.adjacency_list:
            history[row[0].start] = sys.maxsize
        history["1"] = 0
        while len(history) != 0:
            min_key: str = "1"
            min_value: int = sys.maxsize
            for key in history.keys():
                if history[key] < min_value:
                    min_key = key
                    min_value = history[key]
            destinations: list = []
            distances: list = []
            for row in self.adjacency_list:
                if row[0].start == min_key:
                    for edge in row:
                        if edge.end in history.keys():
                            destinations.append(edge.end)  
                            distances.append(edge.weight)  

            history.pop(min_key)
            records[min_key] = min_value
            for i in range(len(destinations)):
                if min_value + distances[i] < history[destinations[i]]:
                    history[destinations[i]] = min_value + distances[i]
        print(records)
if __name__ == '__main__':
    graph: Graph = Graph()
    graph.insert("1", "2", 3)
    graph.insert("1", "8", 7)
    graph.insert("2", "1", 4)
    graph.insert("2", "3", 8)
    graph.insert("2", "8", 13)
    graph.insert("3", "2", 7)
    graph.insert("3", "4", 7)
    graph.insert("3", "6", 6)
    graph.insert("3", "9", 2)
    graph.insert("4", "3", 8)
    graph.insert("4", "5", 9)
    graph.insert("4", "6", 11)
    graph.insert("5", "4", 10)
    graph.insert("5", "6", 11)
    graph.insert("6", "5", 10)
    graph.insert("6", "4", 15)
    graph.insert("6", "3", 5)
    graph.insert("6", "7", 7)
    graph.insert("7", "6", 3)
    graph.insert("7", "9", 6)
    graph.insert("7", "8", 1)
    graph.insert("8", "1", 8)
    graph.insert("8", "2", 13)
    graph.insert("8", "9", 7)
    graph.insert("8", "7", 1)
    graph.insert("9", "3", 2)
    graph.insert("9", "8", 7)
    graph.insert("9", "7", 6)
    graph.display()
    graph.minimum_distance()