from collections import deque

def solve(n,maps):
    visited=[False for _ in range(n)]
    par=[-1 for _ in range(n)]
    q=deque()
    q.append(1)
    ans=-1
    level=0
    found=False
    while len(q)!=0:
        l=len(q)
        level+=1
        for _ in range(l):
            curr=q.popleft()
            if curr==n:
                ans=level
                found=True
            for nbr in maps[curr]:
                if visited[nbr-1]==False:
                    par[nbr-1]=curr
                    q.append(nbr)
                    visited[nbr-1]=True
        if found==True:
            break
    if ans==-1:
        return [-1,[]]
    curr=n
    path=deque()
    path.append(n)
    while curr!=1:
        path.appendleft(par[curr-1])
        curr=par[curr-1]
    return [ans,path]

n,m=list(map(int,input().split()))
maps={}
for i in range(1,n+1):
    maps[i]=[]
for _ in range(m):
    x,y=list(map(int,input().split()))
    maps[x].append(y)
    maps[y].append(x)
count,path=solve(n,maps)
if count==-1:
    print("IMPOSSIBLE")
else:
    print(count)
    for i in range(len(path)):
        print(path[i],end=" " )