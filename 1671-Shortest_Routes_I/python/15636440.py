import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))
    # If the graph is undirected, also add: adj[b].append((a, c))

INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0  # starting from node 1

pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

# Print distances from 1 to n, or -1 if unreachable
res = [str(d if d < INF else -1) for d in dist[1:]]
print(" ".join(res))