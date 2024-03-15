def find_min_distance_vertex(distances, visited):
    min_distance_vertex = None
    min_distance = float('inf')

    for vertex in range(1, len(distances)):
        if vertex not in visited and distances[vertex] < min_distance:
            min_distance = distances[vertex]
            min_distance_vertex = vertex

    return min_distance_vertex
def AdjacencyList(A_L):
    n = int(input("enter the number of vertices:-"))
    for i in range(1, n + 1):
        connections_list = []
        print(f"how many connections for vertex {i}:-")
        con = int(input())
        print(f"enter the connections of vertex {i} separated by space:")
        for j in range(con):
            b = int(input("dest:-"))
            weight = int(input("weight:-"))
            if i == b:
                print("Source and dest can't be the same.")
                exit()
            connections_list.append((b, weight))
        A_L.append(connections_list)
    j = 1
    for i in A_L:
        print(f"for {j}th node:-")
        print(i)
        j += 1
    return A_L
def MINdist(A_L):
    num_vertices = len(A_L)
    distances = [float('inf')] * (num_vertices + 1)
    visited = set()
    start = int(input("Enter the start vertex: "))
    distances[start] = 0
    while len(visited) < num_vertices:
        cur = find_min_distance_vertex(distances, visited)
        visited.add(cur)
        for dest, weight in A_L[cur - 1]:
            if dest not in visited:
                if distances[dest] > weight + distances[cur]:
                    distances[dest] = weight + distances[cur]
    for i in range(1, num_vertices + 1):
        print(f"{i}:-{distances[i]}")
A_L = []
A_L = AdjacencyList(A_L)
MINdist(A_L)
