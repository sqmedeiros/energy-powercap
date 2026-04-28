import heapq

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    a, b, c = [int(i) for i in input().split()]
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append((b, c))

heap = [(0, 1)]
visited = [-1] * (n+1)
while heap:
    weight1, node1 = heapq.heappop(heap)
    if visited[node1] != -1:
        continue
    visited[node1] = weight1
    for node2, weight2 in graph[node1]:
        if visited[node2] == -1:
            heapq.heappush(heap, (weight2 + weight1, node2))

print(" ".join([str(i) for i in visited[1:]]))