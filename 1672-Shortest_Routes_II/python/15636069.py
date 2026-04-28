import sys

input = sys.stdin.readline
n, m, q = map(int, input().split())

INF = 10**18
dist = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

for k in range(1, n+1):
    dk = dist[k]
    for i in range(1, n+1):
        di = dist[i]
        ik = di[k]
        if ik == INF:
            continue
        for j in range(1, n+1):
            v = ik + dk[j]
            if v < di[j]:
                di[j] = v

out = []
for _ in range(q):
    a, b = map(int, input().split())
    d = dist[a][b]
    out.append(str(d if d < INF else -1))

print("\n".join(out))