from collections import defaultdict

class G:
    def _init_(self):
        self.g = defaultdict(list)

    def add_e(self, u, v):
        self.g[u].append(v)

    def bfs(self, s):
        v = [False] * (max(self.g) + 1)
        q = []
        q.append(s)
        v[s] = True
        
        while q:
            s = q.pop(0)
            print(s, end=" ")

            for i in self.g[s]:
                if not v[i]:
                    q.append(i)
                    v[i] = True

if __name__ == '_main_':
    g = G()
    g.add_e(0, 1)
    g.add_e(0, 2)
    g.add_e(1, 2)
    g.add_e(2, 0)
    g.add_e(2, 3)
    g.add_e(3, 3)
    
    print("BFS Traversal (starting from vertex 2)")
    g.bfs(2)