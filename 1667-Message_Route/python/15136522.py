from collections import deque

n, m = map(int, input().split())
g = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

parent = [-1] * (n + 1)
q = deque([1])
parent[1] = 0 

while q:
    v = q.popleft()
    if v == n:
        break
    for to in g[v]:
        if parent[to] == -1:
            parent[to] = v
            q.append(to)

if parent[n] == -1:
    print("IMPOSSIBLE")
else:
    path = []
    cur = n
    while cur != 0:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    print(len(path))
    print(*path)