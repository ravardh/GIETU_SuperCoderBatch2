class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, s, d, w):
        if s not in self.graph:
            self.graph[s] = {}
        if d not in self.graph:
            self.graph[d] = {}
        self.graph[s][d] = w

    def traverse(self, start):
        vertices = list(self.graph.keys())  
        num_vertices = len(vertices)
        
        
        distance = [float('inf')] * num_vertices
        distance[vertices.index(start)] = 0

        visited = set()

        while len(visited) < num_vertices:
            min_distance = float('inf')
            min_vertex_index = None
            
           
            for i, vertex in enumerate(vertices):
                if distance[i] < min_distance and vertex not in visited:
                    min_distance = distance[i]
                    min_vertex_index = i
            visited.add(vertices[min_vertex_index])

           
            for neighbor, w in self.graph[vertices[min_vertex_index]].items():
                neighbor_index = vertices.index(neighbor)
                distance_min = distance[min_vertex_index] + w
                if distance_min < distance[neighbor_index]:
                    distance[neighbor_index] = distance_min
        return distance


g = Graph()
g.add_edge('1', '2', 4)
g.add_edge('1', '8', 8)
g.add_edge('2', '3', 8)
g.add_edge('2', '8', 11)
g.add_edge('3', '4', 7)
g.add_edge('3', '6', 4)
g.add_edge('3', '9', 2)
g.add_edge('4', '5', 9)
g.add_edge('4', '6', 14)
g.add_edge('5', '6', 10)
g.add_edge('6', '7', 2)
g.add_edge('7', '9', 6)
g.add_edge('7', '8', 1)
g.add_edge('8', '9', 7)

print("The min distance is :", g.traverse('1'))
