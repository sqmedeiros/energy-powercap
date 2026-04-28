from typing import List
from collections import deque

n,m = map(int, input().split())

adj: List[List[int]] = [[] for _ in range(n)]
# -2 = start, -1 = unvisited
parent = [-1 for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

queue = deque()
queue.append(0)
parent[0] = -2

while queue:
    u = queue.popleft()
    if u == n-1:
        path = []
        while u != -2:
            path.append(u)
            u = parent[u]
        print(len(path))
        for x in reversed(path):
            print(x+1, end=" ")
        print()
        exit(0)
    for v in adj[u]:
        if parent[v] == -1:
            parent[v] = u
            queue.append(v)
print("IMPOSSIBLE")