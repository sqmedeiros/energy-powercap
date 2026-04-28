import io, os
import heapq
import sys

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

n, m = map(int, input().decode().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().decode().split())
    adj[u - 1].append((v - 1, w))

dist = [float('infinity') for _ in range(n)]
dist[0] = 0
pq = [(0, 0)]

while pq:
    d, curr = heapq.heappop(pq)

    if d > dist[curr]:
        continue

    for nxt, w in adj[curr]:
        if dist[nxt] > dist[curr] + w:
            dist[nxt] = dist[curr] + w
            heapq.heappush(pq, (dist[nxt], nxt))

sys.stdout.write(" ".join(map(str, dist)))