import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

start, goal = 1, n

parent = [-1] * (n + 1) 
q = deque([start])
parent[start] = 0  

while q:
    v = q.popleft()
    if v == goal:
        break
    for u in g[v]:
        if parent[u] == -1:
            parent[u] = v
            q.append(u)

if parent[goal] == -1:
    print("IMPOSSIBLE")
else:

    path = []
    cur = goal
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(len(path))
    print(*path)