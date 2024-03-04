graph=[]
num_nodes=int(input("Enter number of nodes: "))
for _ in range(num_nodes):
    edge=eval(input("Enter node:"))
    graph.append(edge)
vertex=int(input("Enter the vertex:"))

print("Edges in the graph are :",end=" ")
for i in graph:
    for j in i:
        if vertex == j[0]:
            print(j,end=" ")