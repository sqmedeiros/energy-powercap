import heapq

n,m = list(map(int, input().split(" ")))

adj = [[] for _ in range(n)]
dist = [float('inf')] * n
visited = [False] * n

for i in range(m):
    a,b,c = list(map(int, input().split(" ")))
    adj[a-1].append((b-1, c))


def dijkstra(v):
    pq = []
    dist[v] = 0

    heapq.heappush(pq, (0,v))
    while pq:
        d,u = heapq.heappop(pq)
        if(visited[u]):
            continue
        visited[u] = True
        for n, weight in adj[u]:
            if dist[n] > dist[u] + weight:
                dist[n] = dist[u] + weight
            if not visited[n]:
                heapq.heappush(pq, (dist[n],n))

dijkstra(0)
for d in dist:
    print(d, end=" ")