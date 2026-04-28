import sys
input = sys.stdin.readline

n, m, q = map(int, input().split())
INF = 10**18                           

dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0                    

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a][b]:
        dist[a][b] = dist[b][a] = c

for k in range(1, n + 1):
    dk = dist[k]                     
    for i in range(1, n + 1):
        dik = dist[i][k]
        if dik == INF:                
            continue
        di = dist[i]               
        ndik = dik                    
        for j in range(1, n + 1):
            nd = ndik + dk[j]
            if nd < di[j]:
                di[j] = nd

out = []
for _ in range(q):
    a, b = map(int, input().split())
    d = dist[a][b]
    out.append(str(-1 if d == INF else d))

sys.stdout.write('\n'.join(out))