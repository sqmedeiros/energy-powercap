import sys
import heapq
input = sys.stdin.readline

#adadadasdasdasss
INF = 10**30
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append((b, c))

dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]

while pq:
    cur_d, v = heapq.heappop(pq)
    if cur_d > dist[v]:
        continue
    for to, w in g[v]:
        nd = cur_d + w
        if nd < dist[to]:
            dist[to] = nd
            heapq.heappush(pq, (nd, to))

print(*dist[1:])