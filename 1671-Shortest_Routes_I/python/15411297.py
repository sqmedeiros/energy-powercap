import sys
import heapq

input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a = int(data[index])
    index += 1
    b = int(data[index])
    index += 1
    c = int(data[index])
    index += 1
    graph[a].append((b, c))

INF = 10**18
dist = [INF] * (n + 1)
dist[1] = 0

pq = [(0, 1)]  

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

for i in range(1, n + 1):
    print(dist[i], end=' ')
print()