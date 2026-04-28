import sys

it = map(int, sys.stdin.buffer.read().split())
INF = 10**18

n, m, q = next(it), next(it), next(it)

dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, w = next(it) - 1, next(it) - 1, next(it)
    if w < dist[a][b]:
        dist[a][b] = w
        dist[b][a] = w

for k in range(n):
    dk = dist[k]
    for i in range(n):
        di = dist[i]
        t = di[k]
        if t == INF:
            continue
        for j in range(n):
            v = t + dk[j]
            if v < di[j]:
                di[j] = v

out = []
for _ in range(q):
    a, b = next(it) - 1, next(it) - 1
    d = dist[a][b]
    out.append(str(d if d < INF else -1))

sys.stdout.write("\n".join(out))

# out = [solve() for _ in range(next(it))]
# sys.stdout.write("\n".join(out))
