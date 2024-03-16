def kruskal(graph):
    edges=[]
    mtree=[]
    parent={}
    def find(n):
        if parent[n]!=n:
            parent[n]=find(parent[n])
        return parent[n]
    
    def union(u,v):
        parent[find(u)]=find(v)
    for u in graph:
        parent[u]=u
        for v,cost in graph[u]:
            edges.append((cost,u,v))
    edges.sort()

    for cost,u,v in edges:
        if find(u)!=find(v):
            mtree.append((u,v,cost))
            union(u,v)
    return mtree

g={
    '1':[('2',18),('4',20)],
    '2':[('3',17),('10',7)],
    '3':[('2',17),('4',4),('6',11)],
    '4':[('3',4),('1',20)],
    '5':[('4',8),('8',6),('11',5)],
    '6':[('3',11),('9',15),('10',12),('7',16),('8',9)],
    '7':[('10', 14),('6',16),('11',13)],
    '8':[('5',6),('6',9)],
    '9':[('6',15)],
    '10':[('2',7),('6',12),('7',14)],
    '11':[('7',13),('5',5)],
}
mintree = kruskal(g)
print("Minimum Spanning Tree:")
for edge in mintree:
    print(edge)
