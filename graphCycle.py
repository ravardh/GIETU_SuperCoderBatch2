def is_cycle(graph):
    visited = []
    stack = []
    path = []

    def visit(vertex, parent):
        if vertex in stack:
            path.append(vertex)
            return True, vertex
        stack.append(vertex)
        for neighbour in graph.get(vertex, []):
            if neighbour != parent:
                result, cycle_start = visit(neighbour, vertex)
                if result:
                    if vertex not in path:
                        path.append(vertex)
                    return True, cycle_start
        stack.pop()
        visited.append(vertex)
        return False, None

    for vertex in graph:
        if vertex not in visited:
            has_cycle, cycle_start = visit(vertex, None)
            if has_cycle:
                if cycle_start not in path:
                    path.append(cycle_start)
                return True, path[::-1]
    return False, []

graph = {
    1: [2, 4],
    2: [1, 3],
    3: [2, 5, 6],
    4: [1, 5, 7],
    5: [3, 4],
    6: [3],
    7: [4, 8],
    8: [7]
}

has_cycle, cycle_path = is_cycle(graph)
print(f"The graph has a cycle: {has_cycle}")
if has_cycle:
    print(f"The cycle is: {cycle_path}")
