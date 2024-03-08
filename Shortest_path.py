import heapq
import sys
graph = [[] for i in range(100001)]
edges = []
def add_edge(u,v,w):
	graph[u].append((v,w))
	graph[v].append((u,w))
	edges.append((u,v,w))
def dijsktras(src,N):
	dis = [sys.maxsize] * N
	vis = [False] * N
	pq = [(0, src)]
	dis[src] = 0
	while pq:
		weight, node = heapq.heappop(pq)
		if vis[node]:
			continue
		vis[node] = True
		for child, child_weight in graph[node]:
			if dis[child] > child_weight + weight:
				dis[child] = weight + child_weight
				heapq.heappush(pq, (dis[child], child))
	return dis
def shortest_distance(N, M, A, B):
	disA = dijsktras(A, N)
	disB = dijsktras(B, N)
	ans = disA[B]
	for u, v, weight in edges:
		cur = min(disA[u] + disB[v], disA[v] + disB[u]) + (weight // 2)
		ans = min(ans, cur)
	return ans
if __name__ == "__main__":
	N, M, A, B = 9, 14, 0, 2
	add_edge(0, 1, 4)
	add_edge(1, 2, 8)
	add_edge(2, 3, 7)
	add_edge(3, 4, 9)
	add_edge(4, 5, 10)
	add_edge(5, 6, 2)
	add_edge(6, 7, 1)
	add_edge(7, 0, 8)
	add_edge(1, 7, 11)
	add_edge(7, 8, 7)
	add_edge(2, 8, 2)
	add_edge(6, 8, 6)
	add_edge(2, 5, 4)
	add_edge(3, 5, 14)
	print(shortest_distance(N, M, A, B))