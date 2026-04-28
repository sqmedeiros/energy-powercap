def dfs(node,vis,adj):
    vis[node]=1
    for i in adj[node]:
        if vis[i]==0:
            dfs(i,vis,adj)
def bfs(node,vis,adj):
    q=[]
    q.append(node)
    while len(q)!=0:
        k=q.pop()
        vis[k]=1
        for i in adj[k]:
            if vis[i]==0:
                q.append(i)
def main(edges,n,m):
    adj=[[] for i in range(n+1)]
    vis=[0 for i in range(n+1)]
    for i,j in edges:
        adj[i].append(j)
        adj[j].append(i)
    c=0
    ans=[]
    for i in range(1,n+1):
        if vis[i]==0:
            c+=1
            if i!=1:
                ans.append([i-1,i])
            bfs(i,vis,adj)
    return ans,c-1
li=[ int(x) for x in input().split()]
n,m=li[0],li[1]
edges=[]
for i in range(m):
    l=[ int(x) for x in input().split()]
    edges.append(l)
k,p=main(edges,n,m)
print(p)
for i in range(len(k)):
    for j in range(len(k[0])):
        print(k[i][j],end=" ")
    print()


