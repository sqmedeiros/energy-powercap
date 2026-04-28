import sys

input = sys.stdin.readline
INF = 10**18

n, m, q = map(int, input().split())

dist = [[INF] * n for _ in range(n)]

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
    dk = dist[k]
    for i in range(n):
        dik = dist[i][k]
        if dik == INF:
            continue
        di = dist[i]
        nd = dik
        for j in range(n):
            v = nd + dk[j]
            if v < di[j]:
                di[j] = v

out = []
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    res = dist[a][b]
    out.append(str(res if res < INF else -1))

sys.stdout.write("\n".join(out))