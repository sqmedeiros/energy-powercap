from collections import deque
from collections import defaultdict

n, m = list(map(int, input().split()))
G = defaultdict(list)
for i in range(m):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)

visited = set([1])
q = deque([1])
parent = {}
while q:
    u = q.popleft()
    for v in G[u]:
        if v not in visited:
            visited.add(v)
            q.append(v)
            parent[v] = u

if n not in parent:
    print("IMPOSSIBLE")
else:
    path = []
    pos = n
    while pos != 1:
        path.append(pos)
        pos = parent[pos]
    path.append(1)
    print(len(path))
    print(" ".join(list(map(str,path[::-1]))))