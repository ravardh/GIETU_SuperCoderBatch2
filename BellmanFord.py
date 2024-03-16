def bellamn_ford(graph,source,last):
    my_dict = {}
    for i in range(source,last+1):
        if(i==1):
            my_dict[i]=0
        else:
            my_dict[i]=float('inf')

    
    for i in range(source,last):
        for v1,v2,wt in graph:
            if (my_dict[v1]+wt)<my_dict[v2]:
                my_dict[v2] = my_dict[v1]+wt

    print(my_dict)

if __name__ == '__main__':
    graph = [(1,2,6),(1,3,5),(1,4,5),(2,5,-1),(3,2,-2),(3,5,1),(4,3,-2),(4,6,-1),(5,7,3),(6,7,3)]
    source=1
    last=7
    bellamn_ford(graph,source,last)