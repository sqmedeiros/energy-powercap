import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(vertex):
    vis[vertex] = 1
    for neigh in adj[vertex]:
        if not vis[neigh]:
            dfs(neigh)


n, m = map(int, input().split())

adj = [[] for i in range(n + 1)]
ans = []
vis = [0 for j in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

for i in range(1, n + 1):
    if not vis[i]:
        ans.append(i)
        dfs(i)

k = len(ans)
print(k - 1)

for i in range(k - 1):
    print(ans[i], ans[i + 1])