# echo "3 4\n1 2 6\n1 3 2\n3 2 3\n1 3 4" | python3 Shortest-Routes-I.py

import sys
from queue import PriorityQueue

n, m = list(map(int, input().strip().split()))
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((c, b))
  # graph[b].append((c, a))

q = PriorityQueue()
q.put((0, 1))
dist = [sys.maxsize] * (n+1)
dist[1] = 0
proc = [False] * (n+1)

while not q.empty():
    it = q.get()
    if proc[it[1]]:
      continue
    proc[it[1]] = True
    for edge in graph[it[1]]:
      if dist[it[1]] + edge[0] < dist[edge[1]]:
        ndist = dist[it[1]] + edge[0]
        dist[edge[1]] = ndist
        q.put((ndist, edge[1]))

print(" ".join(map(str, dist[1:])))