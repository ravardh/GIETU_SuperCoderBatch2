def bfs(graph,start):
    v=[] 
    q=[]
    q.append(start)
    v.append(start)
    while q:
        c=q.pop(0)
        print(c)
        for n in graph[c]:
            if n not in v:
                v.append(n)
                q.append(n)
            

graph = {'1':['2','3','9'],'2':['1','4'],'3':['1','8'],'4':['2','5','6'],
         '5':['4'],'6':['4','7'],'7':['8','6'],'8':['9','3','7'],'9':['1','8']}
bfs(graph,'3')

def dfs( v,graph,start):
    
    if start not in  v:
        v.append(start)
        print(v[::-1])
        for n in graph[start]:
            dfs(v,graph,n)
v=[]
graph = {'1':['2','3','9'],'2':['1','4'],'3':['1','8'],'4':['2','5','6'],
         '5':['4'],'6':['4','7'],'7':['8','6'],'8':['9','3','7'],'9':['1','8']}
dfs(v,graph,'5')