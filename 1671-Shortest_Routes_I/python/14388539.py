def dijstkra(grafo, v):
    dist = [INF] * n
    dist[v] = 0

    fila = [(0, v)]

    while fila:
        d, v = heapq.heappop(fila)

        if dist[v] < d:
            continue

        for vizinho, d1 in grafo[v]:
            if dist[vizinho] > dist[v] + d1:
                dist[vizinho] = dist[v] + d1
                heapq.heappush(fila, (dist[vizinho], vizinho))
    return dist

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 18
n, m = map(int, input().split())
grafo = defaultdict(list)

for i in range(m):
    v, u, d = map(int, input().split())
    grafo[v-1].append((u-1, d))

dist = dijstkra(grafo, 0)
print(*dist)