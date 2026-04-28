import sys
input = sys.stdin.readline

INF = 10**18

n, m, q = map(int, input().split())

dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

# Floyd-Warshall optimizado
for k in range(1, n + 1):
    dk = dist[k]              # referencia local a la fila k
    for i in range(1, n + 1):
        dik = dist[i][k]
        if dik == INF:        # si ir i→k es imposible, no sirve intentar rutas
            continue
        di = dist[i]          # referencia local a la fila i
        # loop interno optimizado
        for j in range(1, n + 1):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd

out = []
for _ in range(q):
    a, b = map(int, input().split())
    ans = dist[a][b]
    if ans >= INF:
        out.append("-1")
    else:
        out.append(str(ans))

print("\n".join(out))