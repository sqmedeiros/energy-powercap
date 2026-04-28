import sys
sys.setrecursionlimit(10**9)
n, *b = map(int, open(0).read().split())
G = [[] for _ in range(n+1)]
for i, j in enumerate(b, 2):
 G[j] += i,

p = -~n*[0]
v = -~n*[1]


def dfs(x):
 if v[x]:
  v[x] = 0
  for u in G[x]:
   p[x] += dfs(u)+1
 return p[x]


print(' '.join(map(str, map(dfs, range(1, n+1)))))