import sys
input = sys.stdin.readline
INF = 10**18
n, m, q = map(int, input().split())
d = [[INF]*n for _ in range(n)]
for i in range(n):
    d[i][i] = 0
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    if w < d[u][v]:
        d[u][v] = w
        d[v][u] = w
for k in range(n):
    dk = d[k]
    for i in range(n):
        di = d[i]
        ik = di[k]
        if ik == INF:
            continue
        for j in range(n):
            nj = ik + dk[j]
            if nj < di[j]:
                di[j] = nj
out = []
for _ in range(q):
    x, y = map(int, input().split())
    x -= 1; y -= 1
    out.append(str(d[x][y]) if d[x][y] < INF else "-1")
print("\n".join(out))