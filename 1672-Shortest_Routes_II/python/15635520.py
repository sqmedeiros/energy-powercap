import sys
input = sys.stdin.readline

INF = 10**18
n, m, q = map(int, input().split())

dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

for k in range(n):
    for i in range(n):
        dik = dist[i][k]
        if dik == INF:
            continue
        row_i = dist[i]
        row_k = dist[k]
        for j in range(n):
            v = dik + row_k[j]
            if v < row_i[j]:
                row_i[j] = v

res = []
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    res.append(str(dist[a][b] if dist[a][b] != INF else -1))

print("\n".join(res))
