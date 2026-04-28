# -*- coding: utf-8 -*-
from collections import deque

n,m = map(int,input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)

parent = [-1]*n

ini = 0

q = deque()
flag = 0

for i in range(n):
    if flag==1:
        break
    if parent[i]==-1:
        q.append(i)
        parent[i]=-2
        while(len(q)>0 and flag==0):
            u = q.popleft()
            for v in adj[u]:
                if v==parent[u]:
                    continue
                if parent[v]==-1:
                    parent[v]=u
                    q.append(v)
                    continue
                left = u
                right = v
                flag = 1
                break
#print(u,v)
#print(parent)

if flag==0:
    print("IMPOSSIBLE")
else:
    r = v
    temp = set()
    while(r!=-2):
        #print("here")
        temp.add(r)
        r = parent[r]
    ini = -1
    l = u
    ans = deque()
    tot = 0
    while(l!=-2):
        #print("or this")
        ans.appendleft(l+1)
        tot+=1
        if l in temp:
            ini = l
            break
        l = parent[l]
    r = v
    while(r!=-2):
        #print("or maybe this")
        ans.append(r+1)
        tot+=1
        if r==ini:
            break
        r = parent[r]
    print(tot)
    print(*ans)













