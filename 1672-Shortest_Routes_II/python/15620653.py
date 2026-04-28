input = __import__('sys').stdin.readline
n, m, q = map(int, input().split())

inf = 1000000000000
dist = [inf] * (n+1)*(n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    if c < dist[a*n+b]: 
        dist[a*n+b] = c
        dist[b*n+a] = c

rng = range(1, n+1)

for k in rng:
    dist[k*n+k] = 0

for k in rng:
    for i in rng:
        if dist[i*n+k] == inf:
            continue
        for j in range(1, i):
            d = dist[k*n+j] + dist[i*n+k]
            if d < dist[i*n+j]:
                dist[i*n+j] = dist[j*n+i] = d

for _ in range(q):
    a, b = map(int, input().split())
    if dist[a*n+b] == inf:
        print(-1)
    else:   
        print(dist[a*n+b])