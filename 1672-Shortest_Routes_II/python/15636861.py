import sys
input= sys.stdin.readline

INF = 10**18

numbert, m, q = map(int, input().split())

# 0-indexed
dist = [[INF]*numbert for _ in range(numbert)]
for i in range(numbert):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    if c < dist[a][b]:
        dist[a][b] = c
        dist[b][a] = c

# FAST Floyd–Warshall
for k in range(numbert):
    dk = dist[k]
    for i in range(numbert):
        di = dist[i]
        ik = di[k]
        if ik == INF:
            continue
        for j in range(numbert):
            nj = ik + dk[j]
            if nj < di[j]:
                di[j] = nj

out = []
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    out.append(str(dist[a][b]) if dist[a][b] < INF else "-1")

print("\n".join(out))