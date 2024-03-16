def is_cyclic(graph):
    visited=set()
    stack=set()
    def dfs(node):
        visited.add(node)
        stack.add(node)
        for n in graph[node]:
            if n not in visited:
                if dfs(n):
                    return True
            elif n in stack:
                return True
        stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

g={}
ver=int(input("Enter the number of vertices:"))
edg=int(input("Enter the number of edges:"))
print("Enter the edges in the format (u,v):")
for _ in range(edg):
    u,v=map(int,input().split())
    if u not in g:
        g[u]=[]
    g[u].append(v)
if is_cyclic(g):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
