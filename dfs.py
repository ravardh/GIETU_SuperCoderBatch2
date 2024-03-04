def dfs(graph,vertex):
    stack=[]
    stack = [vertex]
    visited = set()
    res = []
    while stack:
        v=stack.pop()
        if v not in visited:
            res.append(v)
            visited.add(v)
            stack+=[x for x in graph[v] if x not in visited]
            # print(stack)

    return res[::-1]

def dfsrecursive(graph,start):
    visited = set()
    def dfsr(node):
        visited.add(node)
        print(node,end=" ")
        for v in graph[node]:
            if v not in visited:
                dfsr(v)
        
    dfsr(start)




graph = {
    1: [2, 3, 9],
    2: [1, 4],
    3: [1,8],
    4: [2,5,6],
    5: [4],
    6:[4,7],
    7:[6,8],
    8:[3,7,9],
    9:[1,8]
}

print(dfsrecursive(graph,5))