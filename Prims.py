def prim(graph):
    mintree=[]
    visited=set()
    start=list(graph.keys())[0]
    visited.add(start)
    e=[(cost,start,neigh) for neigh,cost in graph[start]]
    e.sort()
    while e:
        cost,u,v=e.pop(0)
        if v not in visited:
            visited.add(v)
            mintree.append((u,v,cost))
            for neigh,cost in graph[v]:
                if neigh not in visited:
                    e.append((cost, v, neigh))
            e.sort()
    return mintree

g={
    '1':[('2',18),('4',20)],
    '2':[('3',17),('10',7)],
    '3':[('2',17),('4',4),('6',11)],
    '4':[('3',4),('1',20)],
    '5':[('4',8),('8',6),('11',5)],
    '6':[('3',11),('9',15),('10',12),('7',16),('8',9)],
    '7':[('10',14),('6',16),('11',13)],
    '8':[('5',6),('6',9)],
    '9':[('6',15)],
    '10':[('2',7),('6',12),('7',14)],
    '11':[('7',13),('5',5)],
}

mintree = prim(g)
print("Minimum Spanning Tree:")
for edge in mintree:
    print(edge)
