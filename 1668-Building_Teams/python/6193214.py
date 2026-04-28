import sys
from collections import deque as dq
n, m = map(int,input().split())
g = [[] for i in range(n+1)]

for i in range(m):
    n1, n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)
q = dq()
vis = [0 for i in range(n+1)]
col = [0 for i in range(n+1)]
res = [0, 0]


for i in range(1, n+1):
    if vis[i]: continue
    if not g[i]:
        col[i] = 1
        continue
    q.append((i, 1))
    vis[i] = 1
    col[i] = 1
    while q:
        cn, color = q.pop()
        cc = 1 if color == 2 else 2
        for child in g[cn]:
            if vis[child]:
                if col[child] != cc:
                    print('IMPOSSIBLE')
                    sys.exit()
                continue
            vis[child] = 1
            col[child] = cc
            q.append((child, cc))

print(*col[1:])