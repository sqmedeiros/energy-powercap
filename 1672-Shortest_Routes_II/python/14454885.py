# CSES Shortest Routes II
import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
INF = 10**18

dist = [[INF] * (n + 1) for _ in range(n + 1)]

# distance to self = 0
for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:  # handle multiple edges
        dist[a][b] = c
        dist[b][a] = c

# Floyd–Warshall
for k in range(1, n + 1):
    dk = dist[k]
    for i in range(1, n + 1):
        di, dik = dist[i], dist[i][k]
        if dik == INF:
            continue
        for j in range(1, n + 1):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd

# answer queries
out = []
for _ in range(q):
    u, v = map(int, input().split())
    d = dist[u][v]
    out.append(str(-1 if d == INF else d))
print("\n".join(out))