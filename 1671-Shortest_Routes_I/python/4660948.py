import heapq
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # startNode: (destinationsN, dist)

def dijkstra(graph):
    N = len(graph)
    visited = [False for _ in range(N + 1)]
    dist = [float('inf') for _ in range(N + 1)]
    dist[1] = 0    
    pq = [(0, 1)] #(dist, Node)    
    while pq:
        _, node = heapq.heappop(pq)
        if visited[node]: continue
        visited[node] = True
        for destination, length in graph[node]:
            if dist[node] + length < dist[destination]:
                dist[destination] = dist[node] + length
                heapq.heappush(pq, (dist[destination], destination))
    return dist

dis = dijkstra(graph)[1:]
print(' '.join(map(str, dis)))