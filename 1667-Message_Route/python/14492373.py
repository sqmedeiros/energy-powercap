from collections import deque

n, m = map(int, input().split())
AL = [[] for q in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)
child = [-1] * (n + 1)
child[n] = None
queue = deque([n])
while queue:
    u = queue.popleft()
    for v in AL[u]:
        if child[v] == -1:
            child[v] = u
            queue.append(v)
if child[1] == -1:
    print("IMPOSSIBLE")
else:
    path = []
    u = 1
    while u is not None:
        path.append(u)
        u = child[u]
    print(len(path))
    print(*path)