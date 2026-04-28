import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# distance array
dist = [10**18] * (n + 1)
dist[1] = 0

pq = [(0, 1)]  # (distance, node)

while pq:
    d, u = heapq.heappop(pq)

    if d > dist[u]:
        continue

    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

print(*dist[1:])