import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())

INF = 10**15
# use 0..n indexing; we will ignore index 0 for readability
distances = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    distances[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    if w < distances[u][v]:
        distances[u][v] = w
        distances[v][u] = w  # undirected

# optimized triple loop
rng = range(1, n + 1)
for k in rng:
    dk = distances[k]         # local ref to row k
    for i in rng:
        di = distances[i]     # local ref to row i
        ik = di[k]
        if ik == INF:
            continue
        # inline j loop with locals
        for j in rng:
            kj = dk[j]
            ij = di[j]
            if ij > ik + kj:
                di[j] = ik + kj

out = []
for _ in range(q):
    u, v = map(int, input().split())
    ans = distances[u][v]
    out.append(str(-1 if ans >= INF else ans))

sys.stdout.write("\n".join(out))