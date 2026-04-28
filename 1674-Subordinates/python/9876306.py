import sys
sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for _ in range(n)]
boss = list(map(int, input().split()));
for i in range(n-1):
 p, q = boss[i] - 1, i + 1
 G[p].append(q)
 G[q].append(p)

ans  = [0 for _ in range(n)]
def dfs(v, p):
 ans[v] = 1
 for u in G[v]:
  if u != p:
   dfs(u, v)
   ans[v] += ans[u]

dfs(0, -1)
print(*[_ - 1 for _ in ans])