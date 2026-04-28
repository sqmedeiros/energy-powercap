import sys
sys.setrecursionlimit(10**6)

s = int(input())
bosses = list(map(int, input().split()))

g = [[] for _ in range(s + 1)]
for i, b in enumerate(bosses, start=2):
    g[b].append(i)

sub = [0] * (s + 1)

def dfs(u):
    for v in g[u]:
        dfs(v)
        sub[u] += sub[v] + 1

dfs(1)
print(*sub[1:])