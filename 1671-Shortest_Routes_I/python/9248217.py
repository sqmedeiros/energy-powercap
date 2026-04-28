import sys
from heapq import heappop, heappush

n, m = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    adj[a].append((b, c))

dist = [float('inf')] * (n + 1)
visited = [0] * (n + 1)
dist[1] = 0
q = [(0, 1)]

while q:
    d, a = heappop(q)
    if visited[a]:
        continue
    visited[a] = 1
    for b, c in adj[a]:
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            heappush(q, (dist[b], b))


print(" ".join(map(str,dist[1:])))
# res =[]
# # for i in range(1, n + 1):
# #     res.append(str(dist[i]))
# sys.stdout.write(" ".join(res))