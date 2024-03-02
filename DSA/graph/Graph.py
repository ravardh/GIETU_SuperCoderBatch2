class Edge:
    def __init__(self, start: str, end: str):
        self.start: str = start
        self.end: str = end
        # self.weight: int = weight

    def __str__(self):
        return f"( {self.start}, {self.end}),"


class Graph:

    def __init__(self):
        self.adjacency_list: list = []

    def insert(self, start: str, end: str):

        isThere: bool = False
        index: int = -1
        for i in range(len(self.adjacency_list)):
            if self.adjacency_list[i][0] and self.adjacency_list[i][0].start == start:
                isThere = True
                index = i

        if isThere and index != -1:
            self.adjacency_list[index].append(Edge(start, end))
        else:
            self.adjacency_list.append([Edge(start, end)])

    def display(self):
        for i in self.adjacency_list:
            for j in i:
                print("( ", j.start, " , ", j.end, " )", end="\t")
            print()


if __name__ == '__main__':
    graph: Graph = Graph()

    graph.insert("1", "2")
    graph.insert("1", "5")
    graph.insert("1", "3")

    graph.insert("2", "4")
    graph.insert("2", "1")

    graph.insert("3", "1")
    graph.insert("3", "9")

    graph.insert("4", "2")
    graph.insert("4", "5")
    graph.insert("4", "6")

    graph.insert("5", "1")
    graph.insert("5", "4")
    graph.insert("5", "6")
    graph.insert("5", "7")
    graph.insert("5", "8")
    graph.insert("5", "9")

    graph.insert("6", "7")
    graph.insert("6", "4")

    graph.insert("7", "5")

    graph.insert("8", "5")

    graph.insert("9", "3")
    graph.insert("9", "5")

    graph.display()
