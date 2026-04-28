import sys
input = sys.stdin.readline

INF = 10**18
n, m, q = map(int, input().split())

dist = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dist[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    if w < dist[u][v]:
        dist[u][v] = dist[v][u] = w

for k in range(1, n+1):
    dk = dist[k]
    for i in range(1, n+1):
        di = dist[i]
        aik = di[k]
        if aik == INF:
            continue
        for j in range(1, n+1):
            val = aik + dk[j]
            if val < di[j]:
                di[j] = val

out = []
for _ in range(q):
    a, b = map(int, input().split())
    out.append(str(-1 if dist[a][b] == INF else dist[a][b]))

print("\n".join(out))