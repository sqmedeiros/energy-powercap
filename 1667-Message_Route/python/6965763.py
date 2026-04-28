from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b); G[b].append(a)

par = [[] for _ in range(n + 1)]
dist = [-1] * (n + 1); dist[1] = 0
dq, seen = deque([1]), set([1])

while dq:
    u = dq.popleft()
    for v in G[u]:
        if v not in seen:
            seen.add(v)
            dq.append(v)
            dist[v] = 1 + dist[u]
            par[v].append(u)

if dist[n] != -1:
    print(dist[n] + 1)
    cur, res = n, [n]
    for i in range(dist[n], 0, -1):
        for p in par[cur]:
            if dist[p] == i - 1:
                res.append(p)
                cur = p
                break
    print(*res[::-1])
else:
    print("IMPOSSIBLE")




