from collections import deque


def bfs(x):
    q.append(x)
    while q:
        x = q[0]
        for k in adj[q[0]]:
            if not vis[k]:
                vis[k] = True
                q.append(k)
        q.popleft()


c, r = map(int, input().split())
adj = [[] for _ in range(c+1)]
vis = [False for _ in range(c+1)]
ans = []
q = deque()

for _ in range(r):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, c+1):
    if not vis[i]:
        bfs(i)
        ans.append(i)

print(len(ans)-1)
for i in range(len(ans)-1):
    print(ans[i], ans[i + 1])