from collections import deque

n,m=map(int,input().split())
adj=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

visited=[False]*(n+1)
parent=[-1]*(n+1)
start=1
end=n
q=deque()
q.append(start)

while q:
    u=q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            q.append(v)

if not visited[end]:
    print("IMPOSSIBLE")
    exit()

path=[]
cur=end
while(cur!=start):
    path.append(cur)
    cur=parent[cur]
path.reverse()
path.insert(0,1)
print(len(path))
print(*path)