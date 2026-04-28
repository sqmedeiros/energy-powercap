import heapq
from math import inf

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for _ in range(m):
  v, u, d = map(int, input().split())
  v-=1
  u-=1
  adj[v].append((d, u))

dist = [inf for _ in range(n)]
proc = [False for _ in range(n)]
p_queue = []
dist[0] = 0
heapq.heappush(p_queue, (0, 0))


while p_queue:
  _, node = heapq.heappop(p_queue)
  if(not proc[node]):
    proc[node] = True
    for d, viz in adj[node]:
      if dist[viz] > dist[node]+d:
        dist[viz] = dist[node]+d
        heapq.heappush(p_queue, (dist[viz], viz))

print(*dist)