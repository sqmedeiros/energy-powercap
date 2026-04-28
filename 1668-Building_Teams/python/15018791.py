import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    d[u].append(v)
    d[v].append(u)
uv=[1]*(n+1)
r=[0]*(n+1)
q=list(range(1,n+1))
f=1
while q:
    u=q.pop()
    if uv[u]:
        uv[u]=0
        t=0
        p=[u]
        while p:
            z=[]
            t^=1
            while p:
                u=p.pop()
                for v in d[u]:
                    if uv[v]:
                        uv[v]=0
                        z.append(v)
                        r[v]=t
                    else:
                        if r[v]^r[u]==0:
                            print("IMPOSSIBLE")
                            f=0
                            break
                if f==0:
                    break
            p=z
            if f==0:
                break
        if f==0:
            break
    if f==0:
        break
if f:
    for i in range(n+1):
        r[i]+=1
    print(*(r[1:]))






