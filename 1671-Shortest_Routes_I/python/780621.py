from heapq import *
n,m = map(int,input().split())
e=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    e[a].append((b,c))

d=[float("inf")]*(n+1)
d[1]=0
v=[0]*(n+1)

q=[(0,1)]
while q:
    a = heappop(q)[1]
    if not v[a]:
        v[a]=1
        for b,c in e[a]:
            if d[b]>d[a]+c:
                d[b]=d[a]+c
                heappush(q,(d[b],b))

print(*d[1:])