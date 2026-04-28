import heapq
from collections import defaultdict


def dijkstra(cities, graph, start):
    dist = [float('inf')] * cities
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        distance, node= heapq.heappop(pq)
        if distance > dist[node]:
            continue

        for neighbor, weight in graph[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    return dist


cities, connections =map(int, input().split())
graph = [[] for _ in range(cities)]
for _ in range(connections):
    a, b, c=map(int, input().split())
    graph[a - 1].append((b - 1, c))

distances=dijkstra(cities, graph, 0)

# ans
print(*distances)