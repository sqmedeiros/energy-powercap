import heapq

n, m = map(int, input().split())
pq = []
graph = [[] for i in range(0, n + 1)]
for i in range(0, m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    #graph[v].append([u, w])
dist = [1e18 for i in range(0, n + 1)]
vis = [False for i in range(0, n + 1)]
#src, des = map(int, input().split())
src = 1
dist[src] = 0
heapq.heappush(pq, (0, src))
while pq:
    d, u = heapq.heappop(pq)
    if (vis[u]):
        continue
    vis[u] = True
    for v, w in graph[u]:
        if not vis[v] and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))
for i in range(1, n + 1):
    print(f"{int(dist[i])} ",end='')