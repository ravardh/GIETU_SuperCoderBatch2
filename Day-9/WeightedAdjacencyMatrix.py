def AdjacencyMatrix():
    A_M=[]
    n=int(input("enter the  number of vertex:-"))
    for i in range(1,n+1):
        list = [-1]*(n+1)
        list[i]=0
        print(f"how many connections have for{i}:-")
        con=int(input())
        print(f"entre the connction of {i}by space \n")
        for j in range(0, con):
            b=int(input("dest:-"))
            if(b==i):
                print("Source destination can't be same")
                exit()
            else:
                list[b]=int(input("enter the weight"))
        A_M.append(list)
    for i in A_M:
        print("\n",i)
AdjacencyMatrix()