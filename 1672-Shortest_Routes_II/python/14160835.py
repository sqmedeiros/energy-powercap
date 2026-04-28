import sys
input = sys.stdin.buffer.readline
INF = 10**15

n, m, q = map(int, input().split())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

# Optimized Floyd–Warshall
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

out = []
for _ in range(q):
    a, b = map(int, input().split())
    d = dist[a][b]
    out.append(str(d if d < INF else -1))

sys.stdout.write("\n".join(out))