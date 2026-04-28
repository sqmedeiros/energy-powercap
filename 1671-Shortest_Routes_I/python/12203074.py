from heapq import *
def SRI():

    n,m = map(int,input().split())
    Net = [[] for _ in range(n)]
    for f in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        Net[u].append((v,w))

    dist = [-1]*n

    pq = [(0,0)]

    while len(pq) > 0:
        d,x = heappop(pq)
        if dist[x] != -1:
            continue
        dist[x] = d
        for y, w in Net[x]:
            heappush(pq, (d+w,y))
    print(*dist)

SRI()