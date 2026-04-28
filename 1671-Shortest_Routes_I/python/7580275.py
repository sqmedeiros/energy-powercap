import heapq

N, M = map(int, input().split())
maxN = 10**5
dist = [float('inf')] * (maxN + 1)
G = [[] for _ in range(maxN + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append((b, c))

dist[1] = 0
Q = []
heapq.heappush(Q, (0, 1))

while Q:
    d, u = heapq.heappop(Q)

    if d > dist[u]:
        continue

    for vizinho, peso in G[u]:
        if dist[vizinho] > d + peso:
            dist[vizinho] = d + peso
            heapq.heappush(Q, (d + peso, vizinho))

for i in range(1, N + 1):
    print(dist[i], end=' ' if i < N else '\n')