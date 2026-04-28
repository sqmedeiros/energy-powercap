from sys import stdin
from collections import defaultdict, deque
n, m = map(int, stdin.readline().split())
val = defaultdict(list)
till = 0
def dfs(c, p):
    global till
    if vis[c] != -1:
        till = c
        s.append(c)
        return 1
    vis[c] = 1
    for v in val[c]:
        if v == p:
            continue
        x = dfs(v, c)
        if x == 1:
            s.append(c)
            if till == c:
                return 2
            else:
                return 1
        else:
            if x == 2:
                return 2
    vis[c] = 2
    return 0


for _ in range(m):
    a, b = map(int, stdin.readline().split())
    val[a].append(b)
    val[b].append(a)

vis = [-1] * (n+1)
s = []
import sys
sys.setrecursionlimit(10**6)
for  i in range(1, n+1):
    if dfs(i, -1) and len(s) > 2:
        print(len(s))
        print(*s)
        break
    s = []
else:
    print("IMPOSSIBLE")