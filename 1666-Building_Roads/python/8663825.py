import sys
sys.setrecursionlimit(1000000)


def dfs(x):
    if vis[x]:
        return
    vis[x] = True
    for k in adj[x]:
        dfs(k)


n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
vis = [False for _ in range(n+1)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n+1):
    if not vis[i]:
        ans.append(i)
        dfs(i)

print(len(ans) - 1)
for i in range(0, len(ans) - 1):
    print(ans[i], ans[i + 1])

