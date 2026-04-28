import sys
input = sys.stdin.readline

INF = 10**18

n, m, q = map(int, input().split())

# 0-indexed
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

# FAST Floyd–Warshall
for k in range(n):
    dk = dist[k]
    for i in range(n):
        di = dist[i]
        ik = di[k]
        if ik == INF:
            continue
        for j in range(n):
            nj = ik + dk[j]
            if nj < di[j]:
                di[j] = nj

out = []
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    out.append(str(dist[a][b]) if dist[a][b] < INF else "-1")

print("\n".join(out))

#B