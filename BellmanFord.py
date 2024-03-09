def bellmanFord(edgeList, startNode):
    nodes = set()
    for start, destination, _ in edgeList:
        nodes.add(start)
        nodes.add(destination)

    dist = {node: float('INF') for node in nodes}
    dist[startNode] = 0
    for _ in range(len(edgeList) - 1):
        for start,destination, weight in edgeList:
            if dist[start] + weight < dist[destination]:
                dist[destination] = dist[start] + weight
    return dist

edgeList = [
    ('1','2',6),
    ('1','3',5),
    ('1','4',5),
    ('2','5',-1),
    ('3','2',-2),
    ('4','3',-2),
    ('4','6',-1),
    ('3','5',1),
    ('5','7',3),
    ('6','7',3)
]

startNode = str(input("Enter starting node : "))
dist = bellmanFord(edgeList, startNode)
for node in sorted(dist):
    print(f"{startNode} --> {node} : {dist[node]}")