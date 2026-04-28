from collections import defaultdict
from heapq import *
import sys
input=sys.stdin.buffer.readline
n,m=map(int,input().split())
d=defaultdict(list)
for _ in range(m):
    u,v,w=map(int,input().split())
    d[u].append((v,w))
dis=[10**20 for i in range(n+1)]
visited=[False for i in range(n+1)]
dis[1]=0
h=[]
heappush(h,(0,1))
while h:
    cost,v=heappop(h)
    if visited[v]:
        continue
    visited[v]=True
    for u,di in d[v]:
        if cost+di<dis[u]:
            dis[u]=cost+di
            heappush(h,(dis[u],u))
for i in range(1,len(dis)):
    print(dis[i],end=" ")