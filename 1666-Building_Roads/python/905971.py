import sys

n,m=map(int,input().split())
adj=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,next(sys.stdin).split())
    u,v=u-1,v-1
    adj[u].append(v)
    adj[v].append(u)

new=[]
c=0
a=[0]*n
d={}
for i in range(n):
    if a[i]:
        continue
    c+=1
    d[c]=i
    if c>1:
        new.append((d[c-1],i))
    stk=[i]
    while stk:
        u=stk.pop()
        a[u]=c
        for v in adj[u]:
            if a[v]:
                continue
            a[v]=c
            stk.append(v)

print(len(new))
for u,v in new:
    print(u+1,v+1)