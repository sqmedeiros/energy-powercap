import sys
sys.setrecursionlimit(1 << 20)

def dfs(u):
    sz[u] = 1
    for v in adj[u]:
        dfs(v)
        sz[u] += sz[v]

n = int(input())
p = list(map(int, input().split()))

global adj, sz
adj = [[] for i in range(n)]
for i in range(n - 1):
    adj[p[i] - 1].append(i + 1)

sz = [0] * n
dfs(0)
for i in range(n):
    print(sz[i] - 1, end=' ')