import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
INF = 10**18
# distance matrix
dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    dist[a][b] = min(dist[a][b], c)
    dist[b][a] = min(dist[b][a], c)
for k in range(n):
    dk = dist[k]
    for i in range(n):
        dik = dist[i][k]
        if dik == INF: 
            continue
        di = dist[i]
        for j in range(n):
            if di[j] > dik + dk[j]:
                di[j] = dik + dk[j]
for _ in range(q):
    m, n = map(int, input().split())
    m -= 1; n -= 1
    print(dist[m][n] if dist[m][n] < INF else -1)