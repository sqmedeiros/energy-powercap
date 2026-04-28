import sys
import heapq
def dijkstra(n, graph):
    INF = 10**18
    dist = [INF] * (n + 1)
    dist[1] = 0

    pq = [(0, 1)]

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, cost in graph[node]:
            new_dist = d + cost
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist[1:]
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
print(*dijkstra(n, graph))