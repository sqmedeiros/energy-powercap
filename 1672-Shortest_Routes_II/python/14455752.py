import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
INF = 10**18


dist = [[INF]*n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    if c < dist[a][b]: 
        dist[a][b] = dist[b][a] = c


for k in range(n):
    dk = dist[k]
    for i in range(n):
        dik = dist[i][k]
        if dik == INF:    
            continue
        di = dist[i]
        for j in range(n):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd

out = []
for _ in range(q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    ans = dist[a][b]
    out.append(str(ans if ans < INF else -1))
print("\n".join(out))