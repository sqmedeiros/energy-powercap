import sys
input=sys.stdin.readline
n,m,q=map(int,input().split())
INF=10**18
dist=[[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i]=0
for i in range(m):
    u,v,wt=map(int,input().split())
    u-=1
    v-=1
    if dist[u][v]>wt:
        dist[u][v]=wt
        dist[v][u]=wt

for k in range(n):
    row_k=dist[k]
    for i in range(n):
        row_i=dist[i]
        via=row_i[k]
        if via==INF:
            continue
        for j in range(n):
            d=via+row_k[j]
            if row_i[j]>d:
                row_i[j]=d

ans=[]
for i in range(q):
    u,v=map(int,input().split())
    u-=1
    v-=1
    ans.append(str(dist[u][v] if dist[u][v]!=INF else -1))

print("\n".join(ans))