import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)  

visited = [False]*(n+1)
parent  = [0]*(n+1)
cycle = []

def dfs(u, p):
    visited[u] = True
    for v in adj[u]:
        if v == p:
            continue
        if not visited[v]:
            parent[v] = u
            if dfs(v, u):
                return True
        else:
            # this is where i fucking detect a cycle if i find an already visited ndoe i fucking reconstrcut path fro u to v
            path = [v, u]
            x = u
            while x != v:
                x = parent[x]
                path.append(x)

            cycle.extend(path)
            return True
    return False

for i in range(1, n+1):
    if not visited[i]:
        if dfs(i, 0):
            print(len(cycle))
            print(*cycle)
            break
else:
    print("IMPOSSIBLE")