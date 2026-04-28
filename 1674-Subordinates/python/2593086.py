import sys
sys.setrecursionlimit(10000000)

N = int(input())
par = list(map(int, input().split()))

sub = [0 for i in range(0, N)]
adj = [[] for i in range(0, N + 1)]

for i in range(2, N + 1):
    x = par[i - 2]
    adj[x].append(i)

def dfs(node = 1, par = 0):
    cord = 0
    for x in adj[node]:
        if (x == par):
            continue
        cord += dfs(x, node)
    sub[node - 1] = cord
    return cord + 1


dfs()
print(*sub)