class Edge:
    def __init__(self, start: str, end: str):
        self.start: str = start
        self.end: str = end
        # self.weight: int = weight

    def _str_(self):
        return f"( {self.start}, {self.end}),"


class Graph:

    def __init__(self):
        self.adjacency_list: list = []

    def insert(self, start: str, end: str):

        isThere: bool = False
        index: int = -1
        for i in range(len(self.adjacency_list)):
            for j in self.adjacency_list[i]:
                if j and j.start == start:
                    isThere = True
                    index = i
                    break

        if isThere and index != -1:
            self.adjacency_list[index].append(Edge(start, end))
        else:
            self.adjacency_list.append([Edge(start, end)])

    def display(self):
        for i in self.adjacency_list:
            for j in i:
                print("( ", j.start, " , ", j.end, " )", end="\t")
            print()

    def bfs_traversal(self):
        queue: list = [self.adjacency_list[0][0].start]
        visited: list = [self.adjacency_list[0][0].start]
        while len(queue) != 0:
            cur_vertex: str = queue.pop(0)
            destinations: list = self.__find_dest(cur_vertex)
            for dest in destinations:
                # print(visited, dest)
                if dest not in visited:
                    queue.append(dest)
                    visited.append(dest)

            print(cur_vertex)

    def __find_dest(self, vertex: str) -> list:
        destinations: list = []
        for i in self.adjacency_list:
            for j in i:
                if j.start == vertex:
                    destinations.append(j.end)
        return destinations


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
    print('---------------------------')
    graph.bfs_traversal()
