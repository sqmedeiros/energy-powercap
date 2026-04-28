import sys

iteratable=iter(sys.stdin.read().split())
infinity=10**18
n,m,q=int(next(iteratable)),int(next(iteratable)),int(next(iteratable))
d=[[infinity]*(n+1)for i in range (n+1)]
for i in range (1,n+1):
    d[i][i]=0
for i in range(m):
    a,b,c=int(next(iteratable)),int(next(iteratable)),int(next(iteratable))
    if c<d[a][b]:
        d[a][b]=c
        d[b][a]=c
for k in range(1, n + 1):
    dk = d[k] 
    for i in range(1, n + 1):
        dik = d[i][k]
        if dik == infinity:
            continue 
        di = d[i]
        for j in range(1, n + 1):
            alt = dik + dk[j]
            if alt < di[j]:
                di[j] = alt


for i in range(q):
    x,y=int(next(iteratable)),int(next(iteratable))
    dist=d[x][y]
    if dist>=infinity:
        print("-1")
    else:
        print(dist)