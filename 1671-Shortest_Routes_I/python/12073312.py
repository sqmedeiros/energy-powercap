import sys
import heapq
from collections import defaultdict

def dijkstra(n, graph):
    INF = float('inf')
    dist = [INF] * (n + 1)
    dist[1] = 0  # Start from city 1
    pq = [(0, 1)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)

        if d > dist[node]:  # Ignore outdated distances
            continue

        for neighbor, cost in graph[node]:
            if dist[node] + cost < dist[neighbor]:
                dist[neighbor] = dist[node] + cost
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist[1:]  # Exclude index 0 (1-based indexing)

# Input
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

# Compute shortest paths
result = dijkstra(n, graph)

# Output shortest distances
print(*result)