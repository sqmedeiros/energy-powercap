from math import inf
import queue
from heapq import *
n, m = map(int, input().split())

edges = [[] for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    edges[a-1].append((b-1, c))

def djk(src):
    dist = [inf for i in range(n)]
    dist[src] = 0
    q = []
    heapify(q)
    heappush(q, (dist[src], src))
    while len(q):
        node = heappop(q)
        if dist[node[1]] != node[0]:
            continue

        for i in edges[node[1]]:
            if dist[i[0]] > node[0] + i[1]:
                dist[i[0]] = node[0] + i[1]
                heappush(q, (node[0]+i[1], i[0]))

    return dist
print(*djk(0))
