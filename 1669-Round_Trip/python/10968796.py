import sys
sys.setrecursionlimit(10**6) 
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
def dfs(node,vis,path,parent):
    path.append(node)
    for nodes in graph[node]:
        if not vis[nodes]:
            vis[nodes]=True
            ans=dfs(nodes,vis,path,node)
            if(ans):return ans
        else:
            if(nodes!=parent):
                if(len(path)-path.index(nodes)>2):
                    return (path[path.index(nodes):]+[nodes])
    path.pop()
    return False

vis=[False]*n
flag=0
for i in range(n):
    if not vis[i]:
        vis[i]=True
        ans=dfs(i,vis,[],-1)
        if(ans):
            ans=[ans[i]+1 for i in range(len(ans))]
            flag=1
            print(len(ans))
            print(*ans)
            break
if(flag==0):
    print("IMPOSSIBLE") 
