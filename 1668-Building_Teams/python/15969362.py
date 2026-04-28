from collections import defaultdict
import sys

sys.setrecursionlimit(12**5)

it = map(int,sys.stdin.read().split())
nxt = it.__next__

def DFS(u: int) -> bool:
    # print(*col[1:])
    cur = True
    for v in g[u]:
        if col[v] == 0:
            col[v] = 3 - col[u] #easy switch between state (1) and (2)
            cur &= DFS(v)
        elif col[v] == col[u]:
            return False
    return cur

n,m = nxt(),nxt()
g = defaultdict(list)
for _ in range(m):
    u,v = nxt(),nxt()
    g[u].append(v)
    g[v].append(u)

col = [0] * (n+1)
colorable = True
for i in range(1,n+1):
    if col[i] == 0:
        col[i] = 1
        cur = DFS(i)
        # print(i,cur)
        colorable &= cur

if colorable:
    print(*col[1:])
else:
    print('IMPOSSIBLE')