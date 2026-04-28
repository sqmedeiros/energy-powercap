import heapq

def dijkstra(n, graph):
    distances = [float('inf')] * (n + 1)
    distances[1] = 0

    pq = [(0, 1)]

    while pq:
        dist, node = heapq.heappop(pq) 

        if dist > distances[node]:
            continue
        for neighbor, length in graph[node]:
            if dist + length < distances[neighbor]:
                distances[neighbor] = dist + length
                heapq.heappush(pq, (dist + length, neighbor))
    return distances


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distances = dijkstra(n, graph)

for i in range(1, n + 1):
    print(distances[i], end=' ')