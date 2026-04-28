import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

vis = [0]*(n+1)
par = [-1]*(n+1)
found = False

def dfs(u, p):
    global found
    vis[u] = 1
    par[u] = p
    for v in g[u]:
        if v == p:
            continue
        if vis[v]:
            # cycle found
            path = [v]
            curr = u
            while curr != v:
                path.append(curr)
                curr = par[curr]
            path.append(v)
            path.reverse()
            print(len(path))
            print(" ".join(map(str, path)))
            found = True
            return True
        else:
            if dfs(v, u):
                return True
    return False

for i in range(1, n+1):
    if not vis[i]:
        if dfs(i, -1):
            break

if not found:
    print("IMPOSSIBLE")