from collections import deque
def input_graph():
    global v,e,adj
    v,e=map(int,input().split())
    adj=[[] for _ in range(v+1)]
    for _ in range(e):
        i,j=map(int,input().split())
        adj[i].append(j)
        adj[j].append(i)
def bfs(x):
    global vis,pre
    pre=[0]*(v+1)
    vis[x]=True
    q=deque([x])
    while q:
        s=q.popleft()
        for c in sorted(adj[s]):
            if not vis[c]:
                pre[c]=s
                q.append(c)
                vis[c]=True
input_graph()
vis=[False]*(v+1)
bfs(1)
res=[]
if not vis[v]:
    print("IMPOSSIBLE")
else:
    cur=v
    while True:
        res.append(cur)
        if cur==1:
            break
        cur=pre[cur]
    print(len(res))
    print(*reversed(res))