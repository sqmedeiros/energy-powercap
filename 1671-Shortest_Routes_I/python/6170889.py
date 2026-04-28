import heapq

maxN = int(1e5)

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

N, M = map(int, input().split())
dist = [float('inf')] * (maxN + 1)
G = [[] for _ in range(maxN + 1)]
Q = []

for _ in range(M):
    a, b, c = map(int, input().split())
    G[a].append(Edge(b, c))

dist[1] = 0
heapq.heappush(Q, Node(1, 0))
while Q:
    d = Q[0].dist
    u = Q[0].id
    heapq.heappop(Q)

    if d > dist[u]:
        continue

    for e in G[u]:
        if dist[e.v] > d + e.w:
            dist[e.v] = d + e.w
            heapq.heappush(Q, Node(e.v, d + e.w))

for i in range(1, N + 1):
    print(dist[i], end=" ")
print()