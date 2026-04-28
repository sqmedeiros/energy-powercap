import sys
import heapq

input = sys.stdin.read
data = input().split()
it = iter(data)

n, m = int(next(it)), int(next(it))

# Build graph: adjacency list
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = int(next(it)), int(next(it)), int(next(it))
    graph[a].append((b, c))

# Dijkstra's algorithm
INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0  # starting city is 1
heap = [(0, 1)]  # (distance, node)

while heap:
    d, u = heapq.heappop(heap)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(heap, (dist[v], v))

# Output distances from city 1
print(" ".join(map(str, dist[1:])))