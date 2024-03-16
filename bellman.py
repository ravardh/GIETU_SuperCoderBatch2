def bellman_ford(g, s):
    v = g.keys()
    d = {vertex: float('inf') for vertex in v}
    d[s] = 0

    for _ in range(len(v) - 1):
        for vertex in v:
            for n, w in g[vertex]:
                if d[vertex] + w < d[n]:
                    d[n] = d[vertex] + w

    return d

g = {
    1: [(2, 5), (3, 3)],
    2: [(3, 2), (4, 4)],
    3: [(2, 3), (4, 4)],
    4: [(3, 2), (5, 1)],
    5: [(4, 2)]
}

s = 1

min_d = bellman_ford(g, s)

if min_d:
    print("Minimum distances from vertex", s)
    for v, dist in min_d.items():
        print(f"To vertex {v}: Minimum distance = {dist}")
