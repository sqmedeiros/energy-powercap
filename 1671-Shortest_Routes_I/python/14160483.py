import sys, heapq
input = sys.stdin.buffer.readline
INF = 10**18

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dist = [INF] * (n+1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(pq, (nd, v))

sys.stdout.write(" ".join(map(str, dist[1:])) + "\n")