import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
p_Node = [0] * (n+1)
is_v = [False] * (n+1)
from collections import defaultdict
g = defaultdict(list)
for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

def dfs(now, last):
    p_Node[now] = last
    is_v[now] = True
    for next in g[now]:
        if last != next:
            if is_v[next]:
                path = [now]
                temp = now
                while temp != next:
                    temp = p_Node[temp]
                    path.append(temp)
                path.append(now)
                print(len(path))
                print(*reversed(path))
                sys.exit()
            dfs(next, now)

for i in range(1,n+1):
    if not(is_v[i]):
        dfs(i, 0)

print("IMPOSSIBLE")