import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (n+1)
rep = []

def dfs(node):
    visited[node] = True
    for u in adj[node]:
        if not visited[u]: dfs(u)

def count_components():
    for i in range(1, n+1):
        if not visited[i]:
            rep.append(i)
            dfs(i)

count_components()

print(len(rep) - 1)
for u in rep[1:]:
    print(rep[0], u)