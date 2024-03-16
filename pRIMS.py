def PRIMS (A_L):
    Q=[]
    dict={}
    min=float('inf')
    for i in A_L:
        for j in A_L[i]:
            if(j[1]<min):
                min=j[1]
                source=i
                dest=j[0]
    Q.append((source, dest,min))
    dict[source] = True
    dict[dest] = True
    while len(Q)<len(A_L)-1:
        weight=float('inf')
        for k in dict:
            if dict[k]:
                for l in A_L[k]:
                    if l[0] not in dict and l[1]<weight:
                        weight=l[1]
                        edge=(k,l[0],l[1])
        Q.append(edge)
        dict[edge[0]] = True
        dict[edge[1]] = True
    print(Q)
A_L = {
    1:[(2,4),(3,6), (4,3)],
    2:[(5,12)],
    3:[(1,61)],
    4:[(3,9), (6,5)],
    5:[(4,10)],
    6:[(2,11)]
}
PRIMS(A_L)