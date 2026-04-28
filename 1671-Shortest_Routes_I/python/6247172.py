import sys, heapq

def dijkstra(n, edges):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[1] = 0

    queue = [(0, 1)]
    heapq.heapify(queue)

    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue

        for neighbor, weight in edges[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))

    return distances[1:]


n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))

result = dijkstra(n, edges)
print(*result)