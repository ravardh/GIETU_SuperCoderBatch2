def AdjacencyList(A_L):
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
    return A_L
def DFS(n, dict, A_L):
    if not dict[n]:
        Q.append(n)
        dict[n]=True
        for i in A_L[n- 1]:
            dest = i[1]
            DFS(dest,dict,A_L)
        print(n,end=" ")
    else:
        return
A_L=[]
Q=[]
dict={}
A_L=AdjacencyList(A_L)
for i in range (1,len(A_L)+1):
    dict[i]=False
n = int(input("from where you want to traverse"))
print("the Dfs:-")
DFS(n,dict, A_L)
