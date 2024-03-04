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
    for i in A_L:
        j=1
        print(f"for {j}th node:-")
        print(i)
        j+=1
    print(A_L)
AdjacencyList()