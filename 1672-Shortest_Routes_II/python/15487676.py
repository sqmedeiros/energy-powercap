import sys
input = sys.stdin.readline
INF = 10**18

n, m, q = map(int, input().split())

# allocate matrix
dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

# read edges
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    if w < dist[u][v]:
        dist[u][v] = w
        dist[v][u] = w

# ------------- FLOYD WARSHALL, FULLY OPTIMIZED --------------------
for k in range(n):
    row_k = dist[k]
    for i in range(n):
        row_i = dist[i]
        via = row_i[k]
        if via == INF:
            continue
        # inner loop
        for j in range(n):
            nd = via + row_k[j]
            if nd < row_i[j]:
                row_i[j] = nd

# ------------- ANSWER QUERIES ------------------------------------
out = []
for _ in range(q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    ans = dist[u][v]
    out.append(str(ans if ans < INF else -1))

print("\n".join(out))