from heapq import *
from collections import defaultdict
import sys
input=sys.stdin.buffer.readline

n,m=map(int,input().split())
def v():
    return set()
d=defaultdict(v)

for i in range(m):
    a,b,c=map(int,input().split())
    d[a].add((b,c))

dist=[10**20 for i in range(n+1)]

q=[]

heappush(q,(0,1))

dist[1]=0

while(q):
    x=heappop(q)

    y=x[1]
    dis=x[0]

    if(dist[y]<dis):
        continue

    for i in d[y]:
        if(dist[y]+i[1]<dist[i[0]]):
            dist[i[0]]=dist[y]+i[1]
            heappush(q,(dist[i[0]],i[0]))

print(*dist[1:])