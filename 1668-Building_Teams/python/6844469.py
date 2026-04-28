import sys
from types import GeneratorType
from collections import deque
from heapq import heappop, heappush,heapify
input = sys.stdin.readline
def bfs(i,a,v):
    q=deque([[i,1]])
    while q:
        i,d=q.popleft()
        if v[i]==-1:
            v[i]=d
            d1=1
            if d==1:
                d1=2
            for j in a[i]:
                if v[j]==-1:
                    q+=[[j,d1]]
                else:
                    if v[j]!=d1:
                        return 0
    return 1
t=1
for tt in range(t):
    n,m=list(map(int,input().split()))
    a=[[] for nn in range(n+1)]
    v=[-1]*(n+1)
    for mm in range(m):
        x,y=map(int,input().split())
        a[x]+=[y]
        a[y]+=[x]
    y=1
    for i in range(1,n+1):
        if v[i]==-1:
            y&=bfs(i,a,v)
    if y:
        print(*v[1:])
    else:
        print("IMPOSSIBLE")