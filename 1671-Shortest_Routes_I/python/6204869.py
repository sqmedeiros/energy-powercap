import heapq
from math import inf

n, m = map(int, input().split())

graph = {key: [] for key in range(1, n + 1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


distances = [inf] * n
distances[0] = 0
visited = [False] * n

start_node = (0, 1)
heap = [start_node]
heapq.heapify(heap)

while heap:
    dist, node = heapq.heappop(heap)

    if visited[node - 1] or dist > distances[node - 1]:
        continue

    visited[node - 1] = True

    for item in graph[node]:
        n, w = item
        if distances[n - 1] > dist + w:
            distances[n - 1] = dist + w
            heapq.heappush(heap, (distances[n -1], n))

print(*distances, sep=" ")