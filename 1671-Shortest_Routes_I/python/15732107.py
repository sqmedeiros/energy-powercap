n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

inf = 10**15

dist = [inf] * (n+1)

dist[1] = 0

import heapq

heap = []

heapq.heappush(heap, (0, 1))

while heap:
    d, s = heapq.heappop(heap)
    if d > dist[s]:
        continue
    for dd, t in graph[s]:
        nd = d + dd
        if nd < dist[t]:
            dist[t] = nd
            heapq.heappush(heap, (nd, t))

print(' '.join(map(str, dist[1:])))
