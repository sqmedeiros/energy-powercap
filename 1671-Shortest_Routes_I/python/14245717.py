from heapq import heappop, heappush

n, m = map(int, input().split())

INF = 1 << 60

adj_list = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())

    adj_list[u].append((v, w))


dist = [INF] * (n + 1)
dist[1] = 0

heap = [(0, 1)]

while heap:
    running, node = heappop(heap)

    if running > dist[node]:
        continue

    for v, w in adj_list[node]:
        if running + w < dist[v]:
            dist[v] = running + w
            heappush(heap, (running + w, v))

print(*dist[1:])