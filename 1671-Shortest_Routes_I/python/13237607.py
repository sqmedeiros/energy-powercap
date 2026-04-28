import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for e in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(S):
    dist = [float('inf')] * (n + 1)
    dist[S] = 0
    heap = [(0, S)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(heap, (dist[v], v))

    return dist[1:] 

source = 1
shortest_distances = dijkstra(source)
print(*shortest_distances)