from collections import defaultdict
import heapq

def find(n, v, adj):
    dist = [float("inf")] * (n + 1)
    par = [-1] * (n + 1)
    visited = [False] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]  # Priority queue to store vertices and their distances
    while pq:
        _, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        for to, w in adj[u]:
            if dist[u] + w < dist[to]:
                dist[to] = dist[u] + w
                par[to] = u
                heapq.heappush(pq, (dist[to], to))

    print(*dist[1:])


n, m = map(int, input().split())
adj = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

find(n, m, adj)