def adjecent_List(edges):
    adjecent_list = {}
    for v1,v2 in edges:
        adjecent_list[v1] = adjecent_list.get(v1,[])+[v2]
        adjecent_list[v2] = adjecent_list.get(v2,[])+[v1]

    return adjecent_list

edges = [(1,2),(1,3),(1,5)]

v=int(input("Enter the vertex to be viewed: "))

adj_list = adjecent_List(edges)

for vertex , neighbour in adj_list.items():
    if vertex == v:
        print(f'{vertex}:{neighbour}')
