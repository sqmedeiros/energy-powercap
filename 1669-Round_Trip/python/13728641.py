from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
LGMII = lambda: map(lambda x: int(x) - 1, input().split())
LGLII = lambda: list(map(lambda x: int(x) - 1, input().split()))


inf = float('inf')

def dfs(source, par):
    global ans
    vis.add(source)
    for x in roads[source]:
        if x==par:
            continue
        if x in vis:
            cycle = []
            cur = source
            while cur!= x:
                cycle.append(cur)
                cur = parent[cur]
            cycle.append(x)
            cycle.append(source)
            print(len(cycle))
            print(*cycle[::-1])
            return True
        else:
            parent[x] = source
            if dfs(x,source):
                return True
    return False





n,m = MII()
roads = defaultdict(list)
for _ in range(m):
    u,v = MII()
    roads[u].append(v)
    roads[v].append(u)
vis = set()
parent = defaultdict(int)
found = False
for x in range(1,n+1):
    if x not in vis:
        ans = dfs(x,-1)
        if ans:
            found = True
            break
if not found:
    print("IMPOSSIBLE")