from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
p = [-1] * (N + 1)
vis = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = deque([1])
vis[1] = True

while Q:
    u = Q.popleft()
    for v in G[u]:
        if not vis[v]:
            vis[v] = True
            p[v] = u
            Q.append(v)

if not vis[N]:
    print("IMPOSSIBLE")
else:
    ans = []
    u = N
    while u != -1:
        ans.append(u)
        u = p[u]

    print(len(ans))
    print(' '.join(map(str, ans[::-1])))