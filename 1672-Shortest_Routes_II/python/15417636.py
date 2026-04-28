import sys
input = sys.stdin.readline

INF = 10**18

n, m, q = map(int, input().split())

# Matriz de distancias inicializada con infinito
dist = [[INF]* (n+1) for _ in range(n+1)]

# Distancia a sí mismo = 0
for i in range(1, n+1):
    dist[i][i] = 0

# Leemos aristas
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c     # grafo no dirigido

# Floyd–Warshall
for k in range(1, n+1):
    dk = dist[k]
    for i in range(1, n+1):
        dik = dist[i][k]
        if dik == INF:
            continue
        di = dist[i]
        for j in range(1, n+1):
            via = dik + dk[j]
            if via < di[j]:
                di[j] = via

# Respondemos las q consultas
out = []
for _ in range(q):
    a, b = map(int, input().split())
    ans = dist[a][b]
    if ans >= INF//2:
        out.append("-1")
    else:
        out.append(str(ans))

print("\n".join(out))

