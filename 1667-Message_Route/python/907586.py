from collections import deque

n,m=map(int,input().split())
adj=[set() for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    u,v=u-1,v-1
    adj[u].add(v)
    adj[v].add(u)

que=deque([0])
p=[-1]*n
p[0]=-2
while que:
    u=que.popleft()
    if u==n-1:
        break
    for v in adj[u]:
        if p[v]!=-1:
            continue
        p[v]=u
        que.append(v)

if p[n-1]==-1:
    print('IMPOSSIBLE')
else:
    ans=[]
    u=n-1
    while u!=-2:
        ans.append(u+1)
        u=p[u]
    print(len(ans))
    print(*reversed(ans))