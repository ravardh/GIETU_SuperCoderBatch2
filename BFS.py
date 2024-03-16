def AdjacencyList():
    A_L=[]
    n=int(input("enter the  number of vertex:-"))
    for i in range(1,n+1):
        list = []
        print(f"how many connections have for{i}:-")
        con=int(input())
        print(f"entre the connction of {i}by space \n")
        for j in range(0, con):
            b=int(input("dest:-"))
            list.append(tuple((i,b)))
        A_L.append(list)
    j=1
    for i in A_L:
        print(f"for {j}th node:-")
        print(i)
        j+=1
    print("the Bfs:-")
    BFS(A_L)
def BFS(A_L):
    dict={}
    Q=[]
    for i in range(1,len(A_L)+1):
        dict[i]=False
    n=int(input("from where you want to traverse"))
    Q.append(n)
    dict[n]=True
    while Q:
        cur = Q.pop(0)
        print(cur, end=" ")
        for i in A_L[cur - 1]:
            dest=i[1]
            if not dict[dest]:
                Q.append(dest)
                dict[dest] =True
AdjacencyList()
