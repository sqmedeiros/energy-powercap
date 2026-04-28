from sys import stdin

INF = 10**16

input = stdin.buffer.readline

n, m, q = map(int, input().split())

g = [[0 if i == j else INF for i in range(n + 1)] for j in range(n + 1)]


for i in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = min(g[u][v], w)
    g[v][u] = min(g[v][u], w)

for k, gk in enumerate(g):
    for i, gi in enumerate(g):
        for j in range(1, n + 1):
            gi[j] = min(gi[j], gi[k] + gk[j])

for i in range(q):
    u, v = map(int, input().split())
    print(g[u][v] if g[u][v] != INF else -1)