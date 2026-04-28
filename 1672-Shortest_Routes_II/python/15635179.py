import sys
input = sys.stdin.readline
INF = 10**15
n, m, q = map(int, input().split())
d = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < d[a][b]:
        d[a][b] = d[b][a] = c
for k in range(1, n+1):
    dk = d[k]
    for i in range(1, n+1):
        di, dik = d[i], d[i][k]
        if dik == INF: 
            continue
        for j in range(1, n+1):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd
out = []
for _ in range(q):
    a, b = map(int, input().split())
    out.append(str(d[a][b] if d[a][b] < INF else -1))
print("\n".join(out))