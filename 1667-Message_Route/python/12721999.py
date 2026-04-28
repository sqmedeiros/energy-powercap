# -*- coding: utf-8 -*-
from collections import deque

n,m = map(int,input().split())

visited = [0]*n

flag = 0
#dist = [n+1]*n
#dist[0] = 0
prev = [-1]*n

adj = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)

q = deque()

q.append(0)

visited[0] = 1

while(len(q)>0):
    i = q.popleft()        
    for v in adj[i]:
        if visited[v]==0:
            q.append(v)
            visited[v]=1
            prev[v] = i
            #dist[v] = dist[i]+1

#print(prev)

if prev[n-1]==-1:
    print("IMPOSSIBLE")
else:
    ans = []
    p = n-1
    dist = 0
    while(p!=0):
        ans.append(p+1)
        p = prev[p]
        dist+=1
    ans.append(p+1)
    dist+=1
    ans.reverse()
    print(dist)
    print(*ans)


