import sys
#importing
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

# Optimized Floyd–Warshall
for k in range(1, n + 1):
    dk = dist[k]
    for i in range(1, n + 1):
        dik = dist[i][k]
        if dik == INF:
            continue
        di = dist[i]
        for j in range(1, n + 1):
            val = dik + dk[j]
            if val < di[j]:
                di[j] = val

out = []
for _ in range(q):
    a, b = map(int, input().split())
    res = dist[a][b]
    out.append(str(res if res < INF else -1))

print("\n".join(out))