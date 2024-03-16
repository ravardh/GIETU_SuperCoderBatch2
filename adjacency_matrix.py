def AdjacencyMatrix():
    mat=[]
    n=int(input("enter the  number of vertex: "))
    for i in range(1,n+1):
        list = [0]*(n+1)
        print(f"how many connections have for{i}:-")
        con=int(input())
        print(f"entre the connction of {i}by space \n")
        for j in range(0, con):
            b=int(input("dest:-"))
            list[b]=1
        A_M.append(list)
    for i in A_M:
        print("\n",i)
AdjacencyMatrix()
