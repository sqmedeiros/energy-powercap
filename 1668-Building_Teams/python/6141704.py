import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
maxN = 10**5 + 1
G = [[] for _ in range(maxN)]
vis = [False] * maxN
team = [False] * maxN
possible = True

def dfs(u, p = 0):
    global possible
    for v in G[u]:
        if v != p:
            if not vis[v]:
                team[v] = not team[u]
                vis[v] = True
                dfs(v, u)
            elif team[v] == team[u]:
                possible = False

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(1, N + 1):
    if not vis[i]:
        vis[i] = True
        dfs(i)

if not possible:
    print("IMPOSSIBLE")
else:
    for i in range(1, N + 1):
        print(1 if team[i] else 2, end=(" " if i < N else "\n"))