import sys

#input functions
readint = lambda: int(sys.stdin.readline())
readints = lambda: map(int,sys.stdin.readline().split())
readar = lambda: list(map(int,sys.stdin.readline().split()))
flush = lambda: sys.stdout.flush()
readin = lambda: sys.stdin.readline()[:-1]
readins = lambda: map(str,sys.stdin.readline().split())

n,m,q = readints()
v = n*n
dv = 999999999999999
#if m == 250000: dv = 999999999
dist = [dv]*(v)
for i in range(0,v,n+1):
    dist[i] = 0
for _ in range(m):
    a,b,c = readints()
    #a -= 1
    #b -= 1
    x = a*n+b-1-n
    y = b*n+a-1-n
    if dist[x] > c: dist[x] = c
    if dist[y] > c: dist[y] = c

for k in range(n):
    for i in range(0,v,n):
        f = dist[i+k]
        for j in range(n):
            #r = f + dist[k*n+j]
            if dist[i+j] > f + dist[k*n+j]:
                dist[i+j] = f + dist[k*n+j]


for snth in range(v):
    if dist[snth] == dv: dist[snth] = -1
#ans = list()
for _ in range(q):
    a,b = readints()
    sys.stdout.write(str(dist[a*n+b-1-n])+"\n")
    #ans.append(dist[a*n+b-1-n])
#print(*ans,sep="\n")