def adjlist():
    adjancencylist= {}
    
    vertices = int(input("Enter the number of vertices:"))
    edges = int(input("Enter the number of edges:"))
    
    for i in range(edges):
        u, v = map(int, input("Enter edge (u,v):").split())
        
        #normal
        if u in adjancencylist:
            adjancencylist[u].append(v)
        else:
            adjancencylist[u] = [v]
            
        #undirected
        if v in adjancencylist:
            adjancencylist[v].append(u)
        else:
            adjancencylist[v] = [u]    
            
    return adjancencylist
adj_list = adjlist()
print("Adjacency List:")
for vertex, neighbours in adj_list.items():
    print(vertex, "->", neighbours)