from collections import deque

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
vis = [-1 for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

flag = True
for i in range(N):
    if vis[i] == -1:
        q = deque()
        q.append(i)
        vis[i] = 1
        while q:
            node = q.pop()

            for v in adj[node]:
                if vis[v] == -1:
                    vis[v] = (vis[node] + 1) % 2
                    q.append(v)
                else:
                    flag &= (vis[v] != vis[node])

if flag:
    for i in vis:
        print(i + 1, end=" ")
else:
    print("IMPOSSIBLE")