import heapq

n, m = map(int, input().split())

adj = []
for _ in range(n + 1):
    empty_list = []
    adj.append(empty_list)

for _ in range(m):
    a, b, c = map(int, input().split())
    pair = (b, c)
    adj[a].append(pair)

INF = 10**30
dist = []
for _ in range(n + 1):
    dist.append(INF)

dist[1] = 0

pq = []
heapq.heappush(pq, (0, 1))

while pq:
    d, u = heapq.heappop(pq)
    if d != dist[u]:
        continue

    for edge in adj[u]:
        v = edge[0]
        w = edge[1]
        new_dist = d + w

        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(pq, (new_dist, v))

out = []
for i in range(1, n + 1):
    out.append(str(dist[i]))
print(" ".join(out))