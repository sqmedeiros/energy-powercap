import sys
sys.setrecursionlimit(10**6)

n = int(input())
bosses = list(map(int, input().split()))

p = [[] for _ in range(n + 1)]
for i, b in enumerate(bosses, start=2):
    p[b].append(i)

sub = [0] * (n + 1)

def dfs(u):
    for v in p[u]:
        dfs(v)
        sub[u] += sub[v] + 1

dfs(1)
print(*sub[1:])