n,e=list(map(int,input().split()))
vis=[0]*(3*10**6)
import sys
sys.setrecursionlimit(3*10**6)
g=[[] for i in range(n+1)]
for _ in range(e):
    a,b=list(map(int,input().split()))
    g[a].append(b)
    g[b].append(a)
def dfs(i):
    global vis
    if(vis[i]):
        return 0
    vis[i]=1
    for c in g[i]:
        dfs(c)
arr=[]
for i in range(1,n+1):
    if(not vis[i]):
        arr.append(i)
        dfs(i)
print(len(arr)-1)
for i in range(1,len(arr)):
    print(arr[i-1],arr[i])